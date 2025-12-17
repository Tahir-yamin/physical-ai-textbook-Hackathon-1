import React from 'react';
import Link from '@docusaurus/Link';

/**
 * Custom Link component that intercepts navigation to docs
 * and enforces authentication
 */
export default function LinkWrapper(props: any): JSX.Element {
    const { to, href, ...rest } = props;
    const destination = to || href;

    // Check if this link goes to docs
    const isDocsLink = destination && typeof destination === 'string' && destination.includes('/docs');

    if (isDocsLink) {
        const handleClick = (e: React.MouseEvent) => {
            // Check authentication
            const user = typeof window !== 'undefined' ? localStorage.getItem('user') : null;

            if (!user) {
                // Prevent navigation
                e.preventDefault();
                e.stopPropagation();

                // Store intended destination
                if (typeof window !== 'undefined') {
                    (window as any).redirectAfterAuth = destination;

                    // Open auth modal in signin mode
                    if ((window as any).openAuth) {
                        (window as any).openAuth('signin');
                    }
                }

                return false;
            }
        };

        return <Link to={destination} {...rest} onClick={handleClick} />;
    }

    // For other links, use default behavior
    return <Link to={destination} {...rest} />;
}
