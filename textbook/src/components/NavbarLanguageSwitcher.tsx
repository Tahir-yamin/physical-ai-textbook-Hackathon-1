import React, { useEffect, useState } from 'react';
import LanguageSwitcher from '@site/src/components/LanguageSwitcher';
import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';
import { useLocation } from '@docusaurus/router';

export default function NavbarLanguageSwitcher() {
    const [mounted, setMounted] = useState(false);
    const location = useLocation();

    useEffect(() => {
        if (!ExecutionEnvironment.canUseDOM) return;

        setMounted(true);

        const injectLanguageSwitcher = () => {
            const navbar = document.querySelector('.navbar__items--right');
            if (navbar && !document.getElementById('custom-language-switcher')) {
                const container = document.createElement('div');
                container.id = 'custom-language-switcher';
                container.style.display = 'flex';
                container.style.alignItems = 'center';
                container.style.marginLeft = '8px';
                container.style.marginRight = '8px';

                // Insert before the last item (usually dark mode toggle)
                const lastItem = navbar.lastElementChild;
                if (lastItem) {
                    navbar.insertBefore(container, lastItem);
                } else {
                    navbar.appendChild(container);
                }

                return true;
            }
            return document.getElementById('custom-language-switcher') !== null;
        };

        // Simple injection - NO setState calls
        const inject = () => {
            return injectLanguageSwitcher();
        };

        // Immediate attempts
        inject();

        // Multiple retry timers
        const timers = [
            setTimeout(inject, 10),
            setTimeout(inject, 50),
            setTimeout(inject, 100),
            setTimeout(inject, 200),
            setTimeout(inject, 300),
            setTimeout(inject, 500),
            setTimeout(inject, 800),
            setTimeout(inject, 1000),
            setTimeout(inject, 1500),
            setTimeout(inject, 2000),
        ];

        // Listen for auth state changes via custom event
        const handleAuthChange = () => {
            console.log('Auth state changed, re-injecting language selector');
            // Remove old container
            const oldContainer = document.getElementById('custom-language-switcher');
            if (oldContainer) {
                oldContainer.remove();
            }
            // Re-inject with delays
            setTimeout(inject, 10);
            setTimeout(inject, 50);
            setTimeout(inject, 100);
            setTimeout(inject, 300);
            setTimeout(inject, 500);
        };

        // Listen for navigation and auth events
        const handleNavigation = () => {
            const oldContainer = document.getElementById('custom-language-switcher');
            if (oldContainer) {
                oldContainer.remove();
            }
            setTimeout(inject, 50);
            setTimeout(inject, 100);
            setTimeout(inject, 300);
        };

        window.addEventListener('authStateChanged', handleAuthChange);
        window.addEventListener('popstate', handleNavigation);
        window.addEventListener('hashchange', handleNavigation);

        // Also listen for storage events (when user data is saved)
        const handleStorage = (e: StorageEvent) => {
            if (e.key === 'user') {
                handleAuthChange();
            }
        };
        window.addEventListener('storage', handleStorage);

        return () => {
            timers.forEach(timer => clearTimeout(timer));
            window.removeEventListener('authStateChanged', handleAuthChange);
            window.removeEventListener('popstate', handleNavigation);
            window.removeEventListener('hashchange', handleNavigation);
            window.removeEventListener('storage', handleStorage);
        };
    }, [location.pathname]); // FIXED: Only location.pathname dependency

    if (!mounted || !ExecutionEnvironment.canUseDOM) return null;

    const container = document.getElementById('custom-language-switcher');
    if (!container) return null;

    // Use React Portal to render into navbar
    const ReactDOM = require('react-dom');
    return ReactDOM.createPortal(<LanguageSwitcher />, container);
}
