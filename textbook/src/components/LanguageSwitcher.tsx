import React from 'react';
import { useTranslation } from 'react-i18next';
import styles from './LanguageSwitcher.module.css';

export default function LanguageSwitcher() {
    const { i18n } = useTranslation();

    const changeLanguage = (lng: string) => {
        i18n.changeLanguage(lng);
        // Set document direction for RTL support
        document.documentElement.dir = lng === 'ur' ? 'rtl' : 'ltr';
        document.documentElement.lang = lng;
    };

    return (
        <div className={styles.languageSwitcher}>
            <select
                value={i18n.language}
                onChange={(e) => changeLanguage(e.target.value)}
                className={styles.select}
                aria-label="Select language"
            >
                <option value="en">🌐 English</option>
                <option value="ur">🌐 اردو</option>
            </select>
        </div>
    );
}
