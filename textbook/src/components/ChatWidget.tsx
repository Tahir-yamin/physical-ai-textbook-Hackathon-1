import React, { useState, useEffect, useRef } from 'react';
import styles from './ChatWidget.module.css';

interface Message {
    role: 'user' | 'assistant';
    content: string;
    timestamp?: string;
    sources?: string[];
}

// Browser-safe backend URL configuration
// In development: uses localhost:8000
// In production: can be configured via window object or defaults to same origin
const getBackendUrl = () => {
    // Check if we're in development (localhost)
    if (typeof window !== 'undefined') {
        const hostname = window.location.hostname;
        if (hostname === 'localhost' || hostname === '127.0.0.1') {
            return 'http://localhost:8000';
        }
        // In production, you can set this via window object in your HTML
        // or it defaults to same origin on port 8000
        return (window as any).BACKEND_URL || 'http://localhost:8000';
    }
    return 'http://localhost:8000';
};

const BACKEND_URL = getBackendUrl();

export default function ChatWidget() {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');
    const [sessionId, setSessionId] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const [selectedText, setSelectedText] = useState<string>('');
    const messagesEndRef = useRef<HTMLDivElement>(null);

    // Create session on mount
    useEffect(() => {
        createNewSession();
    }, []);

    // Detect text selection
    useEffect(() => {
        const handleSelection = () => {
            const selection = window.getSelection();
            const text = selection?.toString().trim() || '';
            if (text && text.length > 10) {
                setSelectedText(text);
            }
        };

        document.addEventListener('mouseup', handleSelection);
        return () => document.removeEventListener('mouseup', handleSelection);
    }, []);

    // Auto-scroll to bottom
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const createNewSession = async () => {
        try {
            const response = await fetch(`${BACKEND_URL}/session/new`, {
                method: 'POST',
            });
            const data = await response.json();
            setSessionId(data.session_id);
        } catch (error) {
            console.error('Error creating session:', error);
        }
    };

    const sendMessage = async () => {
        if (!input.trim() || !sessionId) return;

        const userMessage: Message = {
            role: 'user',
            content: input,
        };

        setMessages((prev) => [...prev, userMessage]);
        setInput('');
        setIsLoading(true);

        try {
            // Get current user from window (set by Root.tsx)
            const currentUser = (window as any).currentUser;

            const response = await fetch(`${BACKEND_URL}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    session_id: sessionId,
                    message: input,
                    selected_text: selectedText || null,
                    user_id: currentUser?.user_id || null,
                    software_background: currentUser?.software_background || 'intermediate',
                    hardware_background: currentUser?.hardware_background || 'beginner',
                }),
            });

            const data = await response.json();

            const assistantMessage: Message = {
                role: 'assistant',
                content: data.message,
                sources: data.sources,
                timestamp: data.timestamp,
            };

            setMessages((prev) => [...prev, assistantMessage]);
            setSelectedText(''); // Clear selected text after use
        } catch (error) {
            console.error('Error sending message:', error);
            const errorMessage: Message = {
                role: 'assistant',
                content: 'Sorry, I encountered an error. Please try again.',
            };
            setMessages((prev) => [...prev, errorMessage]);
        } finally {
            setIsLoading(false);
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    };

    const clearChat = () => {
        setMessages([]);
        createNewSession();
    };

    return (
        <>
            {/* Chat Toggle Button */}
            <button
                className={styles.toggleButton}
                onClick={() => setIsOpen(!isOpen)}
                aria-label="Toggle chat"
            >
                {isOpen ? '✕' : '💬'}
            </button>

            {/* Chat Widget */}
            {isOpen && (
                <div className={styles.chatWidget}>
                    <div className={styles.chatHeader}>
                        <h3>🤖 Physical AI Assistant</h3>
                        <div className={styles.headerActions}>
                            <button onClick={clearChat} className={styles.clearButton} title="New chat">
                                🔄
                            </button>
                        </div>
                    </div>

                    {selectedText && (
                        <div className={styles.selectedTextBanner}>
                            <span>📌 Asking about selected text</span>
                            <button onClick={() => setSelectedText('')}>✕</button>
                        </div>
                    )}

                    <div className={styles.chatMessages}>
                        {messages.length === 0 && (
                            <div className={styles.welcomeMessage}>
                                <h4>👋 Hello! I'm your Physical AI assistant.</h4>
                                <p>Ask me anything about:</p>
                                <ul>
                                    <li>ROS 2 and robot control</li>
                                    <li>Gazebo & Unity simulation</li>
                                    <li>NVIDIA Isaac platform</li>
                                    <li>Vision-Language-Action systems</li>
                                </ul>
                                <p className={styles.tip}>
                                    💡 <strong>Tip:</strong> Select any text from the book and ask me about it!
                                </p>
                            </div>
                        )}

                        {messages.map((msg, idx) => (
                            <div key={idx} className={`${styles.message} ${styles[msg.role]}`}>
                                <div className={styles.messageContent}>
                                    <strong>{msg.role === 'user' ? 'You' : 'Assistant'}:</strong>
                                    <p>{msg.content}</p>
                                    {msg.sources && msg.sources.length > 0 && (
                                        <div className={styles.sources}>
                                            <small>📚 Sources: {msg.sources.slice(0, 3).join(', ')}</small>
                                        </div>
                                    )}
                                </div>
                            </div>
                        ))}

                        {isLoading && (
                            <div className={`${styles.message} ${styles.assistant}`}>
                                <div className={styles.messageContent}>
                                    <strong>Assistant:</strong>
                                    <p className={styles.typing}>Thinking...</p>
                                </div>
                            </div>
                        )}

                        <div ref={messagesEndRef} />
                    </div>

                    <div className={styles.chatInput}>
                        <textarea
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyPress={handleKeyPress}
                            placeholder="Ask a question about the textbook..."
                            rows={2}
                            disabled={isLoading}
                        />
                        <button onClick={sendMessage} disabled={!input.trim() || isLoading}>
                            {isLoading ? '⏳' : '➤'}
                        </button>
                    </div>
                </div>
            )}
        </>
    );
}
