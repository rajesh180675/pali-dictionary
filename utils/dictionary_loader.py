import json
import streamlit as st
from typing import Dict, Optional

class DictionaryLoader:
    """Handles dictionary loading with caching"""
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def load_from_file(file_path: str) -> Optional[Dict]:
        """Load dictionary from JSON file with caching"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            st.error(f"Dictionary file not found: {file_path}")
            return None
        except json.JSONDecodeError:
            st.error(f"Invalid JSON in dictionary file: {file_path}")
            return None
        except Exception as e:
            st.error(f"Error loading dictionary: {str(e)}")
            return None
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def load_from_url(url: str) -> Optional[Dict]:
        """Load dictionary from URL with caching"""
        import requests
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"Error downloading dictionary: {str(e)}")
            return None
        except json.JSONDecodeError:
            st.error("Invalid JSON in downloaded dictionary")
            return None
