"""
Translation Service using deep-translator (Python 3.13 compatible)
Translates textbook content to Urdu
"""

from deep_translator import GoogleTranslator
from typing import Optional

class TranslationService:
    """Handles translation of content to Urdu"""
    
    def __init__(self):
        self.translator = GoogleTranslator(source='en', target='ur')
        self.cache = {}  # Simple in-memory cache
    
    async def translate_to_urdu(self, text: str, use_cache: bool = True) -> str:
        """
        Translate English text to Urdu
        
        Args:
            text: English text to translate
            use_cache: Whether to use cached translations
            
        Returns:
            Translated Urdu text
        """
        # Check cache first
        if use_cache and text in self.cache:
            return self.cache[text]
        
        try:
            # Split large text into chunks (Google Translate has 5000 char limit)
            if len(text) > 4500:
                # Split by sentences
                sentences = text.split('. ')
                translated_sentences = []
                
                for sentence in sentences:
                    if sentence.strip():
                        translated = self.translator.translate(sentence)
                        translated_sentences.append(translated)
                
                urdu_text = '. '.join(translated_sentences)
            else:
                urdu_text = self.translator.translate(text)
            
            # Cache the result
            if use_cache:
                self.cache[text] = urdu_text
            
            return urdu_text
        
        except Exception as e:
            print(f"Translation error: {e}")
            return text  # Return original text if translation fails
    
    def clear_cache(self):
        """Clear translation cache"""
        self.cache.clear()

# Global translator instance
translator_service = TranslationService()
