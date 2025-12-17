import React from 'react';
import DefaultNavbarItem from '@theme-original/NavbarItem/DefaultNavbarItem';
import { useLocation } from '@docusaurus/router';

/**
 * Custom NavbarItem wrapper that intercepts clicks on the Textbook link
 * to enforce authentication before allowing navigation
 */
export default function NavbarItemWrapper(props: any): JSX.Element {
    const location = useLocation();

    // Check if this is the Textbook (docSidebar) link
    const isTextbookLink = props.type === 'docSidebar' && props.label === 'Textbook';

    if (isTextbookLink) {
        // Override the onClick handler to check authentication
        const originalOnClick = props.onClick;

        const handleClick = (e: React.MouseEvent) => {
            // Check if user is authenticated
            const user = typeof window !== 'undefined' ? localStorage.getItem('user') : null;

            if (!user) {
                // Prevent navigation
                e.preventDefault();
                e.stopPropagation();

                // Store intended destination
                if (typeof window !== 'undefined') {
                    (window as any).redirectAfterAuth = '/physical-ai-robotics-textbook/docs/intro';

                    // Open auth modal in signin mode
                    if ((window as any).openAuth) {
                        (window as any).openAuth('signin');
                    }
                }

                return false;
            }

            // If authenticated, allow normal navigation
            if (originalOnClick) {
                originalOnClick(e);
            }
        };

        // Return the item with our custom click handler
        return <DefaultNavbarItem {...props} onClick={handleClick} />;
    }

    // For all other navbar items, use default behavior
    return <DefaultNavbarItem {...props} />;
}
