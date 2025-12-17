import React, { useState } from 'react';
import styles from './AuthModal.module.css';

interface AuthModalProps {
    onClose: () => void;
    onAuthSuccess: (userData: any) => void;
    initialMode?: 'signin' | 'signup';
}

export default function AuthModal({ onClose, onAuthSuccess, initialMode = 'signup' }: AuthModalProps) {
    const [isSignup, setIsSignup] = useState(initialMode === 'signup');
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        name: '',
        software_background: 'intermediate',
        hardware_background: 'beginner'
    });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    // Browser-safe backend URL configuration
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

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        const endpoint = isSignup ? '/auth/signup' : '/auth/signin';
        const payload = isSignup ? formData : {
            email: formData.email,
            password: formData.password
        };

        try {
            const response = await fetch(`${BACKEND_URL}${endpoint}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Authentication failed');
            }

            const data = await response.json();
            localStorage.setItem('user', JSON.stringify(data));
            onAuthSuccess(data);
            onClose();
        } catch (err: any) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className={styles.overlay} onClick={onClose}>
            <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
                <button className={styles.closeButton} onClick={onClose}>×</button>

                <h2>{isSignup ? 'Create Account' : 'Sign In'}</h2>

                <form onSubmit={handleSubmit}>
                    {isSignup && (
                        <input
                            type="text"
                            placeholder="Full Name"
                            value={formData.name}
                            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                            required
                        />
                    )}

                    <input
                        type="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                        required
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        value={formData.password}
                        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                        required
                    />

                    {isSignup && (
                        <>
                            <label>Software Background</label>
                            <select
                                value={formData.software_background}
                                onChange={(e) => setFormData({ ...formData, software_background: e.target.value })}
                            >
                                <option value="beginner">Beginner</option>
                                <option value="intermediate">Intermediate</option>
                                <option value="advanced">Advanced</option>
                            </select>

                            <label>Hardware Background</label>
                            <select
                                value={formData.hardware_background}
                                onChange={(e) => setFormData({ ...formData, hardware_background: e.target.value })}
                            >
                                <option value="beginner">Beginner</option>
                                <option value="intermediate">Intermediate</option>
                                <option value="advanced">Advanced</option>
                            </select>
                        </>
                    )}

                    {error && <div className={styles.error}>{error}</div>}

                    <button type="submit" disabled={loading}>
                        {loading ? 'Please wait...' : (isSignup ? 'Sign Up' : 'Sign In')}
                    </button>
                </form>

                <p className={styles.toggle}>
                    {isSignup ? 'Already have an account?' : "Don't have an account?"}
                    <button onClick={() => setIsSignup(!isSignup)}>
                        {isSignup ? 'Sign In' : 'Sign Up'}
                    </button>
                </p>
            </div>
        </div>
    );
}
