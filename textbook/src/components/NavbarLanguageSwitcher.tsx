import React, { useEffect, useState } from 'react';
import LanguageSwitcher from '@site/src/components/LanguageSwitcher';

export default function NavbarLanguageSwitcher() {
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        // Small delay to ensure navbar DOM is ready
        const timer = setTimeout(() => {
            setMounted(true);
        }, 100);

        return () => clearTimeout(timer);
    }, []);

    // Render directly instead of trying to inject into HTML placeholder
    if (!mounted) return null;

    return (
        <div style={{ display: 'flex', alignItems: 'center', marginLeft: '12px' }}>
            <LanguageSwitcher />
        </div>
    );
}
