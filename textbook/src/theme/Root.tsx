import React, { useState, useEffect } from 'react';
import { useLocation } from '@docusaurus/router';
import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';
import ChatWidget from '../components/ChatWidget';
import AuthModal from '../components/AuthModal';
import NavbarLanguageSwitcher from '../components/NavbarLanguageSwitcher';
import '../i18n/config'; // Initialize i18n

// Swizzled Root component to add global ChatWidget and Auth with protected routes
export default function Root({ children }: { children: React.NodeNode }) {
    const location = useLocation();
    const [showAuthModal, setShowAuthModal] = useState(false);
    const [user, setUser] = useState<any>(null);

    // Load user from localStorage on mount - only in browser
    useEffect(() => {
        if (ExecutionEnvironment.canUseDOM) {
            const savedUser = localStorage.getItem('user');
            if (savedUser) {
                try {
                    setUser(JSON.parse(savedUser));
                } catch (e) {
                    console.error('Error parsing saved user:', e);
                }
            }
        }
    }, []);

    // Check if current route requires authentication
    const requiresAuth = location.pathname.includes('/docs');
    const isAuthenticated = !!user;

    const handleAuthSuccess = (userData: any) => {
        setUser(userData);
        localStorage.setItem('user', JSON.stringify(userData));
        setShowAuthModal(false);
    };

    const handleLogout = () => {
        setUser(null);
        localStorage.removeItem('user');
        // Redirect to homepage on logout
        window.location.href = '/physical-ai-robotics-textbook/';
    };

    // Make auth functions available globally
    useEffect(() => {
        (window as any).openAuth = (mode: 'signin' | 'signup' = 'signup') => {
            setShowAuthModal(true);
        };
        (window as any).logout = handleLogout;
        (window as any).currentUser = user;
    }, [user]);

    // If route requires auth and user is not authenticated, show auth overlay
    if (requiresAuth && !isAuthenticated) {
        return (
            <>
                {/* Blurred background content */}
                <div style={{
                    filter: 'blur(8px)',
                    pointerEvents: 'none',
                    userSelect: 'none',
                    opacity: 0.6
                }}>
                    {children}
                    <NavbarLanguageSwitcher />
                    <ChatWidget />
                </div>

                {/* Auth modal overlay - always visible on protected routes when not authenticated */}
                <AuthModal
                    onClose={() => {
                        // Redirect to homepage when closing modal on protected route
                        window.location.href = '/physical-ai-robotics-textbook/';
                    }}
                    onAuthSuccess={handleAuthSuccess}
                    initialMode="signin"
                />

                {/* Overlay message */}
                <div style={{
                    position: 'fixed',
                    top: '50%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)',
                    zIndex: 999,
                    textAlign: 'center',
                    background: 'rgba(10, 14, 39, 0.95)',
                    padding: '40px',
                    borderRadius: '20px',
                    boxShadow: '0 20px 60px rgba(0, 0, 0, 0.5)',
                    maxWidth: '90%',
                    width: '500px'
                }}>
                    <h2 style={{ color: '#fff', marginBottom: '15px', fontSize: '24px' }}>
                        🔐 Authentication Required
                    </h2>
                    <p style={{ color: '#a0a0a0', marginBottom: '25px', fontSize: '16px' }}>
                        Please sign in to access the Physical AI textbook content.
                    </p>
                    <p style={{ color: '#666', fontSize: '14px' }}>
                        Don't have an account? You can sign up from the login form above.
                    </p>
                </div>
            </>
        );
    }

    // Normal rendering for non-protected routes or authenticated users
    return (
        <>
            {children}
            <NavbarLanguageSwitcher />
            <ChatWidget />

            {showAuthModal && (
                <AuthModal
                    onClose={() => setShowAuthModal(false)}
                    onAuthSuccess={handleAuthSuccess}
                    initialMode="signup"
                />
            )}

            {/* Floating auth button - moved to bottom-left to avoid navbar overlap */}
            {!user && (
                <button
                    onClick={() => setShowAuthModal(true)}
                    style={{
                        position: 'fixed',
                        bottom: '80px',  // Above chat widget
                        left: '20px',    // Left side
                        zIndex: 1000,
                        padding: '12px 24px',
                        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                        color: 'white',
                        border: 'none',
                        borderRadius: '25px',
                        cursor: 'pointer',
                        fontSize: '15px',
                        fontWeight: 'bold',
                        boxShadow: '0 4px 15px rgba(102, 126, 234, 0.4)',
                        transition: 'all 0.3s ease',
                    }}
                    onMouseEnter={(e) => {
                        e.currentTarget.style.transform = 'translateY(-2px)';
                        e.currentTarget.style.boxShadow = '0 6px 20px rgba(102, 126, 234, 0.6)';
                    }}
                    onMouseLeave={(e) => {
                        e.currentTarget.style.transform = 'translateY(0)';
                        e.currentTarget.style.boxShadow = '0 4px 15px rgba(102, 126, 234, 0.4)';
                    }}
                >
                    🔐 Sign In
                </button>
            )}

            {user && (
                <div
                    style={{
                        position: 'fixed',
                        bottom: '80px',  // Above chat widget
                        left: '20px',    // Left side
                        zIndex: 1000,
                        padding: '12px 20px',
                        background: 'linear-gradient(135deg, #00ff88 0%, #00dd77 100%)',
                        color: '#0A0E27',
                        borderRadius: '25px',
                        fontSize: '15px',
                        display: 'flex',
                        gap: '12px',
                        alignItems: 'center',
                        boxShadow: '0 4px 15px rgba(0, 255, 136, 0.4)',
                        fontWeight: '600',
                    }}
                >
                    <span>👤 {user.name}</span>
                    <button
                        onClick={handleLogout}
                        style={{
                            background: 'rgba(10, 14, 39, 0.15)',
                            border: 'none',
                            color: '#0A0E27',
                            padding: '6px 12px',
                            borderRadius: '12px',
                            cursor: 'pointer',
                            fontSize: '13px',
                            fontWeight: 'bold',
                            transition: 'all 0.2s ease',
                        }}
                        onMouseEnter={(e) => {
                            e.currentTarget.style.background = 'rgba(10, 14, 39, 0.25)';
                        }}
                        onMouseLeave={(e) => {
                            e.currentTarget.style.background = 'rgba(10, 14, 39, 0.15)';
                        }}
                    >
                        Logout
                    </button>
                </div>
            )}
        </>
    );
}
