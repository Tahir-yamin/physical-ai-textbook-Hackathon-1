import React from 'react';
import { useTranslation } from 'react-i18next';

// Wrapper component for translatable docs content
export default function TranslatableDoc({ children, urduContent }) {
    const { i18n } = useTranslation();

    // Show Urdu content if language is Urdu, otherwise show English (children)
    if (i18n.language === 'ur' && urduContent) {
        return <div className="urdu-content">{urduContent}</div>;
    }

    return <>{children}</>;
}
