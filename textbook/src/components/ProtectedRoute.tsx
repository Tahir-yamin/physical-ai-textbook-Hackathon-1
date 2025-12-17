import React, { useEffect } from 'react';
import { useLocation } from '@docusaurus/router';

/**
 * ProtectedRoute component that wraps docs content
 * Checks if user is authenticated before allowing access
 */
export default function ProtectedRoute({ children }: { children: React.ReactNode }) {
    const location = useLocation();

    useEffect(() => {
        // Check if user is authenticated
        const checkAuth = () => {
            const user = localStorage.getItem('user');

            // If no user and we're on a docs page
            if (!user && location.pathname.includes('/docs')) {
                // Trigger auth modal
                if (typeof window !== 'undefined' && (window as any).openAuth) {
                    (window as any).redirectAfterAuth = location.pathname;
                    (window as any).openAuth();
                }

                // Navigate back to homepage
                if (typeof window !== 'undefined') {
                    window.location.href = '/physical-ai-robotics-textbook/';
                }
            }
        };

        checkAuth();
    }, [location]);

    // Check authentication before rendering
    const user = typeof window !== 'undefined' ? localStorage.getItem('user') : null;

    if (!user && typeof window !== 'undefined' && location.pathname.includes('/docs')) {
        return (
            <div style={{
                padding: '40px',
                textAlign: 'center',
                minHeight: '400px',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center'
            }}>
                <h2>🔐 Authentication Required</h2>
                <p>Please sign in to access the textbook content.</p>
                <button
                    onClick={() => {
                        if ((window as any).openAuth) {
                            (window as any).openAuth();
                        }
                    }}
                    style={{
                        marginTop: '20px',
                        padding: '12px 24px',
                        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                        color: 'white',
                        border: 'none',
                        borderRadius: '25px',
                        cursor: 'pointer',
                        fontSize: '16px',
                        fontWeight: 'bold'
                    }}
                >
                    Sign In
                </button>
            </div>
        );
    }

    return <>{children}</>;
}
