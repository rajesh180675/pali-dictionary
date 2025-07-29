import unicodedata
from typing import List, Tuple, Dict
import streamlit as st

class SearchEngine:
    """Optimized search engine for Pali dictionary"""
    
    @staticmethod
    def normalize_text(text: str) -> str:
        """Remove diacritics for search"""
        nfd = unicodedata.normalize('NFD', text.lower())
        return ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')
    
    @staticmethod
    @st.cache_data(ttl=300)
    def build_search_index(entries: Dict) -> Dict:
        """Build search index with caching"""
        index = {
            'words': {},
            'normalized': {},
            'prefixes': {},
            'meanings': {}
        }
        
        for word, entry in entries.items():
            # Word index
            word_lower = word.lower()
            index['words'][word_lower] = word
            
            # Normalized index
            normalized = SearchEngine.normalize_text(word)
            if normalized not in index['normalized']:
                index['normalized'][normalized] = []
            index['normalized'][normalized].append(word)
            
            # Prefix index (for autocomplete)
            for i in range(1, min(len(word_lower), 10)):
                prefix = word_lower[:i]
                if prefix not in index['prefixes']:
                    index['prefixes'][prefix] = []
                index['prefixes'][prefix].append(word)
            
            # Meaning index
            if 'meaning' in entry:
                words = entry['meaning'].lower().split()
                for w in words:
                    if len(w) > 3:
                        if w not in index['meanings']:
                            index['meanings'][w] = []
                        index['meanings'][w].append(word)
        
        return index
