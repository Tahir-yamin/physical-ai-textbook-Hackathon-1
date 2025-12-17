import React, { useState } from 'react';
import styles from './TranslateButton.module.css';

const getBackendUrl = () => {
    if (typeof window !== 'undefined') {
        const hostname = window.location.hostname;
        if (hostname === 'localhost' || hostname === '127.0.0.1') {
            return 'http://localhost:8000';
        }
        return (window as any).BACKEND_URL || 'http://localhost:8000';
    }
    return 'http://localhost:8000';
};

const BACKEND_URL = getBackendUrl();

export default function TranslateButton() {
    const [isTranslated, setIsTranslated] = useState(false);
    const [isTranslating, setIsTranslating] = useState(false);
    const [originalContent, setOriginalContent] = useState<string>('');

    const translatePage = async () => {
        if (isTranslating) return;

        if (isTranslated) {
            // Restore original content
            restoreOriginal();
            return;
        }

        setIsTranslating(true);

        try {
            // Get main article content
            const article = document.querySelector('article');
            if (!article) {
                alert('Content not found');
                return;
            }

            // Save original HTML
            setOriginalContent(article.innerHTML);

            // Get all text from the article
            const allText = article.innerText;

            // Translate the entire content
            const response = await fetch(`${BACKEND_URL}/translate?text=${encodeURIComponent(allText)}`, {
                method: 'POST',
            });

            const data = await response.json();

            if (!data.translated_text) {
                alert('Translation failed');
                return;
            }

            // Function to recursively get all text nodes
            const getAllTextNodes = (node: Node): Text[] => {
                const textNodes: Text[] = [];

                // Skip script and style tags
                if (node.nodeName === 'SCRIPT' || node.nodeName === 'STYLE') {
                    return textNodes;
                }

                if (node.nodeType === Node.TEXT_NODE) {
                    const text = node.textContent?.trim();
                    if (text && text.length > 0) {
                        textNodes.push(node as Text);
                    }
                } else if (node.nodeType === Node.ELEMENT_NODE) {
                    node.childNodes.forEach(child => {
                        textNodes.push(...getAllTextNodes(child));
                    });
                }

                return textNodes;
            };

            // Get all text nodes
            const textNodes = getAllTextNodes(article);

            // Create array of all text content
            const textContents = textNodes.map(node => node.textContent?.trim() || '');

            // Translate each piece of text individually for better accuracy
            const translations: string[] = [];

            // Batch translate in chunks to avoid too many API calls
            const chunkSize = 10;
            for (let i = 0; i < textContents.length; i += chunkSize) {
                const chunk = textContents.slice(i, i + chunkSize);
                const combinedText = chunk.join('\n|||SEPARATOR|||\n');

                try {
                    const chunkResponse = await fetch(`${BACKEND_URL}/translate?text=${encodeURIComponent(combinedText)}`, {
                        method: 'POST',
                    });
                    const chunkData = await chunkResponse.json();
                    const translatedChunk = chunkData.translated_text.split('\n|||SEPARATOR|||\n');
                    translations.push(...translatedChunk);
                } catch (error) {
                    console.error('Translation chunk error:', error);
                    // Fallback to original text if translation fails
                    translations.push(...chunk);
                }
            }

            // Replace each text node with its translation
            textNodes.forEach((node, index) => {
                if (translations[index]) {
                    node.textContent = translations[index];
                }
            });

            // Add RTL styling for Urdu
            article.style.direction = 'rtl';
            article.style.textAlign = 'right';
            article.style.fontFamily = '"Noto Nastaliq Urdu", "Jameel Noori Nastaleeq", serif';

            setIsTranslated(true);

        } catch (error) {
            console.error('Translation error:', error);
            alert('Translation failed. Please try again.');
        } finally {
            setIsTranslating(false);
        }
    };

    const restoreOriginal = () => {
        const article = document.querySelector('article');
        if (article && originalContent) {
            article.innerHTML = originalContent;
            article.style.direction = 'ltr';
            article.style.textAlign = 'left';
            article.style.fontFamily = '';
        }
        setIsTranslated(false);
    };

    return (
        <button
            className={styles.translateButton}
            onClick={translatePage}
            disabled={isTranslating}
            title={isTranslated ? "Switch to English" : "Translate to Urdu"}
        >
            {isTranslating ? '⏳ Translating...' : isTranslated ? '🇬🇧 English' : '🇵🇰 اردو'}
        </button>
    );
}
