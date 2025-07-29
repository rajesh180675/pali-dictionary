import streamlit as st
import json
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter, defaultdict
import re
from typing import Dict, List, Tuple, Optional
import unicodedata
import time
import os
import py7zr  # Added for 7z support
import tempfile  # Added for temporary file handling

# Page configuration
st.set_page_config(
    page_title="Enhanced Monumental Pali Dictionary",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (unchanged)
def load_css():
    st.markdown("""
    <style>
    /* Main styling */
    .main-header {
        background: linear-gradient(135deg, #8B4513 0%, #D2691E 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.95;
    }
    
    /* Entry card styling */
    .entry-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #D2691E;
        transition: all 0.3s ease;
    }
    
    .entry-card:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    .pali-word {
        color: #8B4513;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        font-family: 'Noto Serif', serif;
    }
    
    .entry-meaning {
        color: #333;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 0.5rem 0;
    }
    
    .entry-type {
        display: inline-block;
        background: #e9ecef;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
    }
    
    .semantic-field {
        display: inline-block;
        background: #fff3cd;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
    }
    
    .register-badge {
        display: inline-block;
        background: #d1ecf1;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
    }
    
    .frequency-badge {
        display: inline-block;
        background: #d4edda;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.85rem;
    }
    
    /* Special Pali characters */
    .pali-special {
        color: #D2691E;
        font-weight: 500;
    }
    
    /* Statistics cards */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        height: 100%;
        transition: transform 0.2s;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #8B4513;
        margin: 0.5rem 0;
    }
    
    .stat-label {
        color: #666;
        font-size: 0.9rem;
    }
    
    /* Components display */
    .component-tag {
        display: inline-block;
        background: #D2691E;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        margin: 0.25rem;
        font-size: 0.9rem;
        cursor: pointer;
        transition: background 0.2s;
    }
    
    .component-tag:hover {
        background: #8B4513;
    }
    
    /* Senses list */
    .sense-item {
        background: #f0f0f0;
        padding: 0.75rem;
        margin: 0.5rem 0;
        border-radius: 5px;
        border-left: 3px solid #D2691E;
    }
    
    .sense-category {
        font-weight: bold;
        color: #8B4513;
        text-transform: capitalize;
    }
    
    /* Related words */
    .related-word {
        display: inline-block;
        background: #6c757d;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        margin: 0.25rem;
        font-size: 0.9rem;
        cursor: pointer;
        transition: background 0.2s;
    }
    
    .related-word:hover {
        background: #5a6268;
    }
    
    /* Grammatical info */
    .grammar-info {
        background: #e8f4f8;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    
    .grammar-label {
        font-weight: 600;
        color: #495057;
        margin-right: 0.5rem;
    }
    
    /* Feature list */
    .feature-item {
        padding: 0.5rem 0;
        border-bottom: 1px solid #eee;
    }
    
    .feature-item:last-child {
        border-bottom: none;
    }
    
    /* Info boxes */
    .info-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
    }
    
    .success-box {
        background: #e8f5e9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
    
    .error-box {
        background: #ffebee;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #f44336;
        margin: 1rem 0;
    }
    
    /* Quality score indicator */
    .quality-score {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-left: 0.5rem;
    }
    
    .quality-excellent { background: #4CAF50; }
    .quality-good { background: #8BC34A; }
    .quality-acceptable { background: #FFC107; }
    .quality-poor { background: #FF5722; }
    </style>
    """, unsafe_allow_html=True)

# Enhanced Dictionary class with 7z support
class EnhancedPaliDictionary:
    def __init__(self):
        self.data = None
        self.entries = {}
        self.metadata = {}
        self.statistics = {}
        self.search_index = {}
        self.loaded = False
        
    @st.cache_data(ttl=3600, show_spinner=False)
    def load_dictionary_from_7z(_self, archive_path):
        """Load dictionary from 7z file with caching"""
        try:
            temp_dir = tempfile.mkdtemp()
            extracted_path = None
            
            # Extract 7z file
            with py7zr.SevenZipFile(archive_path, mode='r') as archive:
                # List all files in the archive
                file_list = archive.getnames()
                
                # Find JSON file in archive
                json_files = [f for f in file_list if f.endswith('.json')]
                
                if not json_files:
                    raise ValueError("No JSON file found in 7z archive")
                
                # Extract the first JSON file found
                json_file = json_files[0]
                archive.extract(path=temp_dir, targets=[json_file])
                extracted_path = os.path.join(temp_dir, json_file)
            
            # Load JSON data
            with open(extracted_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Clean up temporary files
            if os.path.exists(extracted_path):
                os.remove(extracted_path)
            if os.path.exists(temp_dir):
                os.rmdir(temp_dir)
            
            return data
            
        except Exception as e:
            # Clean up on error
            if 'temp_dir' in locals() and temp_dir and os.path.exists(temp_dir):
                import shutil
                shutil.rmtree(temp_dir, ignore_errors=True)
            raise e
        
    @st.cache_data(ttl=3600, show_spinner=False)
    def load_dictionary(_self, file_path):
        """Load dictionary with caching - supports both JSON and 7z files"""
        try:
            # Check if file exists
            if not os.path.exists(file_path):
                # Try alternative paths
                alt_paths = [
                    "data/pali_dictionary.7z",
                    "pali_dictionary.7z",
                    "data/pali_dictionary.json",
                    "pali_dictionary.json",
                    "./data/pali_dictionary.json",
                    "../pali_dictionary.json"
                ]
                for alt_path in alt_paths:
                    if os.path.exists(alt_path):
                        file_path = alt_path
                        break
                else:
                    raise FileNotFoundError(f"Dictionary file not found: {file_path}")
            
            # Check file extension and load accordingly
            if file_path.endswith('.7z'):
                # Load from 7z archive
                return _self.load_dictionary_from_7z(file_path)
            else:
                # Load from JSON file (existing functionality)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data
                
        except Exception as e:
            st.error(f"Error loading dictionary: {str(e)}")
            return None
    
    def initialize(self, file_path):
        """Initialize dictionary"""
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            status_text.text("Loading dictionary file...")
            progress_bar.progress(10)
            
            self.data = self.load_dictionary(file_path)
            
            if self.data:
                status_text.text("Processing dictionary entries...")
                progress_bar.progress(30)
                
                self.entries = self.data.get('dictionary', {})
                self.metadata = self.data.get('metadata', {})
                self.statistics = self.data.get('statistics', {})
                
                status_text.text("Building search index...")
                progress_bar.progress(60)
                
                self.build_search_index()
                
                status_text.text("Finalizing...")
                progress_bar.progress(90)
                
                self.loaded = True
                progress_bar.progress(100)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                return True
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"Failed to initialize dictionary: {str(e)}")
            return False
    
    def build_search_index(self):
        """Build comprehensive search index"""
        self.search_index = {
            'words': {},
            'normalized': {},
            'meanings': defaultdict(set),
            'roots': defaultdict(set),
            'bases': defaultdict(set),
            'components': defaultdict(set),
            'types': defaultdict(set),
            'fields': defaultdict(set),
            'prefixes': defaultdict(set)
        }
        
        for word, entry in self.entries.items():
            # Word index
            word_lower = word.lower()
            self.search_index['words'][word_lower] = word
            
            # Normalized form
            normalized = self.normalize_text(word)
            if normalized not in self.search_index['normalized']:
                self.search_index['normalized'][normalized] = []
            self.search_index['normalized'][normalized].append(word)
            
            # Prefix index for autocomplete
            for i in range(1, min(len(word_lower), 8)):
                prefix = word_lower[:i]
                self.search_index['prefixes'][prefix].add(word)
            
            # Meaning words
            if 'meaning' in entry:
                meaning_words = re.findall(r'\b\w+\b', entry['meaning'].lower())
                for mword in meaning_words:
                    if len(mword) > 3:
                        self.search_index['meanings'][mword].add(word)
            
            # Root index
            if 'root' in entry:
                self.search_index['roots'][entry['root']].add(word)
            
            # Base index
            if 'base' in entry:
                self.search_index['bases'][entry['base']].add(word)
            
            # Components index
            if 'components' in entry and entry['components']:
                for comp in entry['components']:
                    self.search_index['components'][comp].add(word)
            
            # Type index
            if 'type' in entry:
                self.search_index['types'][entry['type']].add(word)
            
            # Semantic field index
            if 'semantic_field' in entry:
                self.search_index['fields'][entry['semantic_field']].add(word)
    
    def normalize_text(self, text):
        """Remove diacritics for search"""
        nfd = unicodedata.normalize('NFD', text.lower())
        return ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')
    
    def search(self, query, search_type='all', filters=None, limit=100):
        """Enhanced search with filters"""
        if not self.loaded:
            return []
        
        query_lower = query.lower()
        query_normalized = self.normalize_text(query)
        results = []
        seen = set()
        
        # Apply search based on type
        search_results = self._perform_search(query, query_lower, query_normalized, search_type)
        
        # Apply filters if provided
        if filters:
            search_results = self._apply_filters(search_results, filters)
        
        # Sort by score and limit
        search_results.sort(key=lambda x: x[2], reverse=True)
        return search_results[:limit]
    
    def _perform_search(self, query, query_lower, query_normalized, search_type):
        """Perform the actual search"""
        results = []
        seen = set()
        
        # Exact match
        if query in self.entries:
            results.append((query, self.entries[query], 100))
            seen.add(query)
        
        # Case-insensitive exact match
        if query_lower in self.search_index['words'] and self.search_index['words'][query_lower] not in seen:
            word = self.search_index['words'][query_lower]
            results.append((word, self.entries[word], 95))
            seen.add(word)
        
        if search_type in ['all', 'prefix']:
            # Prefix search
            if query_lower in self.search_index['prefixes']:
                for word in self.search_index['prefixes'][query_lower]:
                    if word not in seen:
                        score = 90 - (len(word) - len(query)) * 2
                        results.append((word, self.entries[word], score))
                        seen.add(word)
        
        if search_type in ['all', 'contains']:
            # Contains search
            for word in self.entries:
                if word not in seen and query_lower in word.lower():
                    score = 70 - word.lower().index(query_lower) * 2
                    results.append((word, self.entries[word], score))
                    seen.add(word)
        
        if search_type in ['all', 'normalized']:
            # Normalized search
            if query_normalized in self.search_index['normalized']:
                for word in self.search_index['normalized'][query_normalized]:
                    if word not in seen:
                        results.append((word, self.entries[word], 80))
                        seen.add(word)
        
        if search_type in ['all', 'meaning']:
            # Search in meanings
            for mword in query_lower.split():
                if mword in self.search_index['meanings']:
                    for word in self.search_index['meanings'][mword]:
                        if word not in seen:
                            results.append((word, self.entries[word], 60))
                            seen.add(word)
        
        if search_type in ['all', 'root']:
            # Search by root
            if query_lower in self.search_index['roots']:
                for word in self.search_index['roots'][query_lower]:
                    if word not in seen:
                        results.append((word, self.entries[word], 85))
                        seen.add(word)
        
        if search_type in ['all', 'component']:
            # Search in components
            if query_lower in self.search_index['components']:
                for word in self.search_index['components'][query_lower]:
                    if word not in seen:
                        results.append((word, self.entries[word], 75))
                        seen.add(word)
        
        return results
    
    def _apply_filters(self, results, filters):
        """Apply filters to search results"""
        filtered = []
        
        for word, entry, score in results:
            # Type filter
            if 'type' in filters and filters['type']:
                if entry.get('type') != filters['type']:
                    continue
            
            # Semantic field filter
            if 'semantic_field' in filters and filters['semantic_field']:
                if entry.get('semantic_field') != filters['semantic_field']:
                    continue
            
            # Register filter
            if 'register' in filters and filters['register']:
                if entry.get('register') != filters['register']:
                    continue
            
            # Frequency filter
            if 'min_frequency' in filters:
                if entry.get('frequency', 0) < filters['min_frequency']:
                    continue
            
            if 'max_frequency' in filters:
                if entry.get('frequency', 0) > filters['max_frequency']:
                    continue
            
            # Has components filter
            if 'has_components' in filters and filters['has_components']:
                if not entry.get('components'):
                    continue
            
            # Has senses filter
            if 'has_senses' in filters and filters['has_senses']:
                if not entry.get('senses'):
                    continue
            
            filtered.append((word, entry, score))
        
        return filtered
    
    def get_autocomplete_suggestions(self, prefix, limit=10):
        """Get autocomplete suggestions"""
        if len(prefix) < 2:
            return []
        
        prefix_lower = prefix.lower()
        suggestions = []
        
        if prefix_lower in self.search_index['prefixes']:
            words = list(self.search_index['prefixes'][prefix_lower])
            # Sort by length and frequency
            words.sort(key=lambda w: (len(w), -self.entries[w].get('frequency', 0)))
            
            for word in words[:limit]:
                entry = self.entries[word]
                suggestions.append({
                    'word': word,
                    'meaning': entry.get('meaning', '')[:50] + '...',
                    'type': entry.get('type', '')
                })
        
        return suggestions
    
    def get_related_words(self, word, limit=20):
        """Get words related to a given word"""
        if word not in self.entries:
            return []
        
        entry = self.entries[word]
        related = []
        seen = {word}
        
        # Related words from entry
        if 'related_words' in entry and entry['related_words']:
            for rel_word in entry['related_words']:
                if rel_word in self.entries and rel_word not in seen:
                    related.append((rel_word, 'related'))
                    seen.add(rel_word)
        
        # Same root
        if 'root' in entry and entry['root'] in self.search_index['roots']:
            for rel_word in self.search_index['roots'][entry['root']]:
                if rel_word not in seen:
                    related.append((rel_word, 'same root'))
                    seen.add(rel_word)
        
        # Same base
        if 'base' in entry and entry['base'] in self.search_index['bases']:
            for rel_word in self.search_index['bases'][entry['base']]:
                if rel_word not in seen:
                    related.append((rel_word, 'same base'))
                    seen.add(rel_word)
        
        # Contains as component
        if word in self.search_index['components']:
            for compound in self.search_index['components'][word]:
                if compound not in seen:
                    related.append((compound, 'used in compound'))
                    seen.add(compound)
        
        # Has as component
        if 'components' in entry and entry['components']:
            for comp in entry['components']:
                if comp in self.entries and comp not in seen:
                    related.append((comp, 'component'))
                    seen.add(comp)
        
        return related[:limit]
    
    def get_enhanced_statistics(self):
        """Get comprehensive statistics"""
        stats = {
            'total_entries': len(self.entries),
            'metadata': self.metadata,
            'loaded_stats': self.statistics,
            'entry_types': Counter(),
            'semantic_fields': Counter(),
            'registers': Counter(),
            'has_components': 0,
            'has_etymology': 0,
            'has_senses': 0,
            'has_related': 0,
            'quality_scores': Counter(),
            'frequency_distribution': Counter(),
            'word_lengths': [],
            'compound_depths': Counter()
        }
        
        for word, entry in self.entries.items():
            # Type distribution
            if 'type' in entry:
                stats['entry_types'][entry['type']] += 1
            
            # Semantic fields
            if 'semantic_field' in entry:
                stats['semantic_fields'][entry['semantic_field']] += 1
            
            # Registers
            if 'register' in entry:
                stats['registers'][entry['register']] += 1
            
            # Features
            if 'components' in entry and entry['components']:
                stats['has_components'] += 1
                stats['compound_depths'][len(entry['components'])] += 1
            
            if 'etymology' in entry and entry['etymology']:
                stats['has_etymology'] += 1
            
            if 'senses' in entry and entry['senses']:
                stats['has_senses'] += 1
            
            if 'related_words' in entry and entry['related_words']:
                stats['has_related'] += 1
            
            # Quality scores
            if 'quality_score' in entry:
                score = entry['quality_score']
                if score >= 0.9:
                    stats['quality_scores']['excellent'] += 1
                elif score >= 0.7:
                    stats['quality_scores']['good'] += 1
                elif score >= 0.5:
                    stats['quality_scores']['acceptable'] += 1
                else:
                    stats['quality_scores']['poor'] += 1
            
            # Frequency distribution
            if 'frequency' in entry:
                freq = entry['frequency']
                if freq >= 4.5:
                    stats['frequency_distribution']['Very High'] += 1
                elif freq >= 3.5:
                    stats['frequency_distribution']['High'] += 1
                elif freq >= 2.5:
                    stats['frequency_distribution']['Medium'] += 1
                elif freq >= 1.5:
                    stats['frequency_distribution']['Low'] += 1
                else:
                    stats['frequency_distribution']['Very Low'] += 1
            
            # Word length
            stats['word_lengths'].append(len(word))
        
        return stats

# Helper functions (unchanged)
def highlight_pali_chars(text):
    """Highlight special Pali characters"""
    special_chars = 'āīūṭḍṇḷñṅṃṛḷ'
    for char in special_chars:
        text = text.replace(char, f'<span class="pali-special">{char}</span>')
    return text

def format_entry_type(entry_type):
    """Format entry type for display"""
    if not entry_type:
        return "Unknown"
    
    type_map = {
        'base': 'Base Word',
        'inflected_noun': 'Inflected Noun',
        'verb': 'Verb Form',
        'participle': 'Participle',
        'prefixed_verb': 'Prefixed Verb',
        'compound': 'Compound',
        'derivative': 'Derivative',
        'technical_term': 'Technical Term',
        'indeclinable': 'Indeclinable',
        'sandhi_variant': 'Sandhi Variant',
        'dialectical_variant': 'Dialectical Variant',
        'periphrastic_form': 'Periphrastic Form'
    }
    
    # Handle specific compound types
    if entry_type.startswith('compound_'):
        compound_type = entry_type.replace('compound_', '').replace('_', ' ').title()
        return f"{compound_type} Compound"
    
    # Handle specific derivative types
    if entry_type.startswith('derivative_'):
        deriv_type = entry_type.replace('derivative_', '').replace('_', ' ').title()
        return deriv_type
    
    return type_map.get(entry_type, entry_type.replace('_', ' ').title())

def get_frequency_label(frequency):
    """Get frequency label with color"""
    if frequency >= 4.5:
        return "Very High", "#4CAF50"
    elif frequency >= 3.5:
        return "High", "#8BC34A"
    elif frequency >= 2.5:
        return "Medium", "#FFC107"
    elif frequency >= 1.5:
        return "Low", "#FF9800"
    else:
        return "Very Low", "#FF5722"

def display_entry_card(word, entry, show_details=False, show_related=False):
    """Display a single entry as an enhanced card"""
    html = f'<div class="entry-card">'
    
    # Word with quality indicator
    quality_class = ""
    if 'quality_score' in entry:
        score = entry['quality_score']
        if score >= 0.9:
            quality_class = "quality-excellent"
        elif score >= 0.7:
            quality_class = "quality-good"
        elif score >= 0.5:
            quality_class = "quality-acceptable"
        else:
            quality_class = "quality-poor"
    
    html += f'<div class="pali-word">{highlight_pali_chars(word)}'
    if quality_class:
        html += f'<span class="quality-score {quality_class}" title="Quality score"></span>'
    html += '</div>'
    
    # Tags row
    html += '<div style="margin: 0.5rem 0;">'
    
    if 'type' in entry:
        html += f'<span class="entry-type">{format_entry_type(entry["type"])}</span>'
    
    if 'semantic_field' in entry:
        html += f'<span class="semantic-field">{entry["semantic_field"]}</span>'
    
    if 'register' in entry:
        html += f'<span class="register-badge">{entry["register"]}</span>'
    
    if 'frequency' in entry:
        freq_label, freq_color = get_frequency_label(entry['frequency'])
        html += f'<span class="frequency-badge" style="background: {freq_color}20; color: {freq_color};">{freq_label}</span>'
    
    html += '</div>'
    
    # Meaning
    html += f'<div class="entry-meaning">{entry.get("meaning", "No meaning available")}</div>'
    
    if show_details:
        # Senses
        if 'senses' in entry and entry['senses']:
            html += '<div style="margin-top: 1rem;"><strong>Semantic Senses:</strong></div>'
            for category, sense in entry['senses'].items():
                html += f'<div class="sense-item"><span class="sense-category">{category}:</span> {sense}</div>'
        
        # Etymology
        if 'etymology' in entry and entry['etymology']:
            html += f'<div style="margin-top: 1rem;"><strong>Etymology:</strong> {entry["etymology"]}</div>'
        
        # Components
        if 'components' in entry and entry['components']:
            html += '<div style="margin-top: 1rem;"><strong>Components:</strong></div>'
            html += '<div>'
            for comp in entry['components']:
                html += f'<span class="component-tag" onclick="searchWord(\'{comp}\')">{comp}</span>'
            html += '</div>'
        
        # Grammatical information
        gram_fields = ['base', 'root', 'case', 'number', 'gender', 'tense', 'person', 'voice', 
                      'mood', 'participle_type', 'degree', 'prefix', 'suffix']
        gram_info = []
        
        for field in gram_fields:
            if field in entry:
                field_label = field.replace('_', ' ').title()
                gram_info.append(f'<span class="grammar-label">{field_label}:</span> {entry[field]}')
        
        if gram_info:
            html += '<div class="grammar-info">'
            html += ' | '.join(gram_info)
            html += '</div>'
        
        # Related words
        if show_related and 'related_words' in entry and entry['related_words']:
            html += '<div style="margin-top: 1rem;"><strong>Related Words:</strong></div>'
            html += '<div>'
            for rel_word in entry['related_words']:
                html += f'<span class="related-word" onclick="searchWord(\'{rel_word}\')">{rel_word}</span>'
            html += '</div>'
    
    html += '</div>'
    
    # Add JavaScript for word clicking
    html += """
    <script>
    function searchWord(word) {
        // This will be handled by Streamlit's session state
        console.log('Search for:', word);
    }
    </script>
    """
    
    return html

# Initialize session state
if 'dictionary' not in st.session_state:
    st.session_state.dictionary = EnhancedPaliDictionary()
    st.session_state.search_history = []
    st.session_state.bookmarks = set()
    st.session_state.current_word = None
    st.session_state.show_stats = False
    st.session_state.filters = {}

# Load CSS
load_css()

# Main UI
def main():
    # Header with metadata
    metadata = st.session_state.dictionary.metadata
    
    st.markdown(f"""
    <div class="main-header">
        <h1>📖 {metadata.get('name', 'Pali Dictionary')}</h1>
        <p>Version {metadata.get('version', 'Unknown')} • 
           {metadata.get('total_entries', 0):,} entries • 
           Generated: {metadata.get('generated', 'Unknown')[:10]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize dictionary if not loaded
    if not st.session_state.dictionary.loaded:
        with st.spinner("🔄 Initializing dictionary... This may take a moment for large files."):
            dict_path = "data/pali_dictionary.7z"  # Updated to use 7z file
            
            if st.session_state.dictionary.initialize(dict_path):
                st.success("✅ Dictionary loaded successfully!")
                st.balloons()
            else:
                st.error("❌ Failed to load dictionary. Please check the file path.")
                st.info("Expected file location: `data/pali_dictionary.7z` or `data/pali_dictionary.json`")
                
                # File uploader as fallback - now supports 7z
                uploaded_file = st.file_uploader("Or upload your dictionary file:", type=['json', '7z'])
                if uploaded_file is not None:
                    try:
                        # Save uploaded file with correct extension
                        file_extension = '.7z' if uploaded_file.name.endswith('.7z') else '.json'
                        temp_filename = f"temp_dict{file_extension}"
                        
                        with open(temp_filename, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        
                        if st.session_state.dictionary.initialize(temp_filename):
                            st.success("✅ Dictionary loaded from uploaded file!")
                            # Clean up temp file
                            if os.path.exists(temp_filename):
                                os.remove(temp_filename)
                            st.rerun()
                    except Exception as e:
                        st.error(f"Error loading uploaded file: {str(e)}")
                        # Clean up temp file on error
                        if 'temp_filename' in locals() and os.path.exists(temp_filename):
                            os.remove(temp_filename)
                
                st.stop()
    
    # Sidebar (unchanged)
    with st.sidebar:
        st.markdown("### 🔍 Search & Filter")
        
        # Search mode
        search_mode = st.selectbox(
            "Search Mode",
            ["All", "Exact Match", "Prefix", "Contains", "Normalized", "In Meanings", "By Root", "By Component"],
            help="Choose how to search the dictionary"
        )
        
        search_type_map = {
            "All": "all",
            "Exact Match": "exact",
            "Prefix": "prefix",
            "Contains": "contains",
            "Normalized": "normalized",
            "In Meanings": "meaning",
            "By Root": "root",
            "By Component": "component"
        }
        
        # Filters
        st.markdown("#### Filters")
        
        # Type filter
        all_types = list(st.session_state.dictionary.search_index['types'].keys())
        if all_types:
            selected_type = st.selectbox(
                "Entry Type",
                ["All"] + sorted(all_types),
                format_func=lambda x: "All Types" if x == "All" else format_entry_type(x)
            )
            st.session_state.filters['type'] = None if selected_type == "All" else selected_type
        
        # Semantic field filter
        all_fields = list(st.session_state.dictionary.search_index['fields'].keys())
        if all_fields:
            selected_field = st.selectbox(
                "Semantic Field",
                ["All"] + sorted(all_fields),
                format_func=lambda x: "All Fields" if x == "All" else x.title()
            )
            st.session_state.filters['semantic_field'] = None if selected_field == "All" else selected_field
        
        # Frequency filter
        freq_range = st.slider(
            "Frequency Range",
            0.0, 5.0, (0.0, 5.0), 0.5,
            help="Filter by word frequency"
        )
        st.session_state.filters['min_frequency'] = freq_range[0]
        st.session_state.filters['max_frequency'] = freq_range[1]
        
        # Feature filters
        st.markdown("#### Features")
        has_components = st.checkbox("Has Components", value=False)
        has_senses = st.checkbox("Has Multiple Senses", value=False)
        
        st.session_state.filters['has_components'] = has_components
        st.session_state.filters['has_senses'] = has_senses
        
        st.markdown("---")
        
        # Quick Links
        st.markdown("### 🔗 Quick Links")
        quick_words = ["buddha", "dhamma", "saṅgha", "nibbāna", "anicca", "dukkha", "anatta", 
                      "mettā", "karuṇā", "muditā", "upekkhā"]
        
        cols = st.columns(2)
        for i, word in enumerate(quick_words):
            with cols[i % 2]:
                if st.button(word, key=f"quick_{word}", use_container_width=True):
                    st.session_state.search_query = word
                    st.rerun()
        
        st.markdown("---")
        
        # Tools
        st.markdown("### 🛠️ Tools")
        
        if st.button("📊 Dictionary Statistics", use_container_width=True):
            st.session_state.show_stats = not st.session_state.show_stats
            st.rerun()
        
        if st.button("🎲 Random Entry", use_container_width=True):
            import random
            random_word = random.choice(list(st.session_state.dictionary.entries.keys()))
            st.session_state.current_word = random_word
            st.rerun()
        
        # Export bookmarks
        if st.session_state.bookmarks:
            st.markdown("#### 💾 Export")
            if st.button("Download Bookmarks", use_container_width=True):
                bookmarks_data = {
                    'metadata': {
                        'exported': datetime.now().isoformat(),
                        'count': len(st.session_state.bookmarks)
                    },
                    'bookmarks': {}
                }
                
                for word in st.session_state.bookmarks:
                    if word in st.session_state.dictionary.entries:
                        bookmarks_data['bookmarks'][word] = st.session_state.dictionary.entries[word]
                
                json_str = json.dumps(bookmarks_data, ensure_ascii=False, indent=2)
                st.download_button(
                    label="📥 Download JSON",
                    data=json_str,
                    file_name=f"pali_bookmarks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        # Features list
        st.markdown("---")
        st.markdown("### ✨ Features")
        
        features = st.session_state.dictionary.metadata.get('features', [])
        if features:
            with st.expander("View all features", expanded=False):
                for feature in features:
                    st.markdown(f"• {feature}")
    
    # Main content area
    if st.session_state.show_stats:
        show_statistics()
    elif st.session_state.current_word:
        show_word_detail(st.session_state.current_word)
    else:
        show_search_interface()
    
    # Footer with stats
    st.markdown("---")
    stats = st.session_state.dictionary.statistics
    if stats:
        st.markdown(
            f"<div style='text-align: center; color: #666; font-size: 0.9rem;'>"
            f"Dictionary contains: {stats.get('base_words', 0):,} base words • "
            f"{stats.get('compounds', 0):,} compounds • "
            f"{stats.get('derivatives', 0):,} derivatives • "
            f"{stats.get('morphological_forms', 0):,} morphological forms"
            f"</div>",
            unsafe_allow_html=True
        )

def show_search_interface():
    """Show the main search interface"""
    # Search box with autocomplete
    col1, col2 = st.columns([4, 1])
    
    with col1:
        search_query = st.text_input(
            "Search Pali Dictionary",
            value=st.session_state.get('search_query', ''),
            placeholder="Enter Pali word, English meaning, root, or component...",
            help="Try: buddha, enlightenment, √gam, or compound components"
        )
        
        # Autocomplete suggestions
        if search_query and len(search_query) >= 2:
            suggestions = st.session_state.dictionary.get_autocomplete_suggestions(search_query, limit=5)
            if suggestions:
                st.markdown("**Suggestions:**")
                for sugg in suggestions:
                    if st.button(f"{sugg['word']} - {sugg['meaning']}", key=f"sugg_{sugg['word']}"):
                        st.session_state.search_query = sugg['word']
                        st.rerun()
    
    with col2:
        search_clicked = st.button("🔍 Search", type="primary", use_container_width=True)
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.search_query = ""
            st.session_state.current_word = None
            st.rerun()
    
    # Perform search
    if search_clicked or search_query != st.session_state.get('last_search', ''):
        if search_query:
            st.session_state.last_search = search_query
            
            # Add to search history
            if search_query not in st.session_state.search_history:
                st.session_state.search_history.insert(0, search_query)
                st.session_state.search_history = st.session_state.search_history[:20]
            
            # Search with filters
            with st.spinner("Searching..."):
                start_time = time.time()
                
                search_type = search_type_map[search_mode]
                results = st.session_state.dictionary.search(
                    search_query,
                    search_type=search_type,
                    filters=st.session_state.filters,
                    limit=200
                )
                
                search_time = time.time() - start_time
            
            # Display results
            if results:
                st.markdown(f"""
                <div class="success-box">
                    Found <strong>{len(results)}</strong> results for "<strong>{search_query}</strong>" 
                    in {search_time:.3f} seconds
                </div>
                """, unsafe_allow_html=True)
                
                # Results display options
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    results_per_page = st.selectbox(
                        "Results per page",
                        [10, 20, 50, 100],
                        index=1
                    )
                with col2:
                    sort_by = st.selectbox(
                        "Sort by",
                        ["Relevance", "Alphabetical", "Frequency", "Type"]
                    )
                with col3:
                    view_mode = st.radio(
                        "View",
                        ["Detailed", "Compact"],
                        horizontal=True
                    )
                
                # Sort results
                if sort_by == "Alphabetical":
                    results.sort(key=lambda x: x[0])
                elif sort_by == "Frequency":
                    results.sort(key=lambda x: x[1].get('frequency', 0), reverse=True)
                elif sort_by == "Type":
                    results.sort(key=lambda x: x[1].get('type', ''))
                
                # Pagination
                total_pages = (len(results) + results_per_page - 1) // results_per_page
                page = st.number_input(
                    "Page",
                    min_value=1,
                    max_value=total_pages,
                    value=1,
                    step=1,
                    format="%d"
                )
                
                # Display results
                start_idx = (page - 1) * results_per_page
                end_idx = min(start_idx + results_per_page, len(results))
                
                for i in range(start_idx, end_idx):
                    word, entry, score = results[i]
                    
                    # Result container
                    with st.container():
                        col1, col2 = st.columns([5, 1])
                        
                        with col1:
                            if view_mode == "Detailed":
                                st.markdown(
                                    display_entry_card(word, entry, show_details=True, show_related=True),
                                    unsafe_allow_html=True
                                )
                            else:
                                # Compact view
                                entry_type = format_entry_type(entry.get('type', ''))
                                meaning = entry.get('meaning', '')[:100] + '...' if len(entry.get('meaning', '')) > 100 else entry.get('meaning', '')
                                
                                if st.button(
                                    f"**{word}** ({entry_type}) - {meaning}",
                                    key=f"result_{word}_{i}",
                                    use_container_width=True
                                ):
                                    st.session_state.current_word = word
                                    st.rerun()
                        
                        with col2:
                            # Action buttons
                            is_bookmarked = word in st.session_state.bookmarks
                            
                            if st.button(
                                "⭐" if is_bookmarked else "☆",
                                key=f"bookmark_{word}_{i}",
                                help="Remove from bookmarks" if is_bookmarked else "Add to bookmarks",
                                use_container_width=True
                            ):
                                if is_bookmarked:
                                    st.session_state.bookmarks.remove(word)
                                else:
                                    st.session_state.bookmarks.add(word)
                                st.rerun()
                            
                            if st.button(
                                "👁️",
                                key=f"view_{word}_{i}",
                                help="View details",
                                use_container_width=True
                            ):
                                st.session_state.current_word = word
                                st.rerun()
                
                # Page navigation
                if total_pages > 1:
                    st.markdown("---")
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.markdown(f"Page {page} of {total_pages}", unsafe_allow_html=True)
            
            else:
                st.markdown(f"""
                <div class="warning-box">
                    No results found for "<strong>{search_query}</strong>". 
                    <br><br>
                    Try:
                    <ul>
                        <li>Checking your spelling</li>
                        <li>Using simpler search terms</li>
                        <li>Searching without diacritical marks (ā → a, ṇ → n, etc.)</li>
                        <li>Using a different search mode</li>
                        <li>Adjusting filters in the sidebar</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    
    # Search history
    if st.session_state.search_history:
        st.markdown("---")
        st.markdown("### 🕐 Recent Searches")
        
        cols = st.columns(5)
        for i, query in enumerate(st.session_state.search_history[:10]):
            with cols[i % 5]:
                if st.button(query, key=f"history_{i}", use_container_width=True):
                    st.session_state.search_query = query
                    st.rerun()
    
    # Bookmarks section
    if st.session_state.bookmarks:
        st.markdown("---")
        st.markdown("### ⭐ Your Bookmarks")
        
        bookmark_cols = st.columns(3)
        for i, word in enumerate(sorted(st.session_state.bookmarks)[:9]):
            with bookmark_cols[i % 3]:
                if word in st.session_state.dictionary.entries:
                    entry = st.session_state.dictionary.entries[word]
                    st.markdown(
                        display_entry_card(word, entry),
                        unsafe_allow_html=True
                    )
                    
                    if st.button(f"View {word}", key=f"bookmark_view_{word}"):
                        st.session_state.current_word = word
                        st.rerun()

def show_word_detail(word):
    """Show detailed view of a single word"""
    if word not in st.session_state.dictionary.entries:
        st.error(f"Word '{word}' not found in dictionary.")
        if st.button("← Back to search"):
            st.session_state.current_word = None
            st.rerun()
        return
    
    entry = st.session_state.dictionary.entries[word]
    
    # Navigation
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.current_word = None
            st.rerun()
    
    with col3:
        is_bookmarked = word in st.session_state.bookmarks
        if st.button(
            "⭐ Bookmarked" if is_bookmarked else "☆ Bookmark",
            key=f"detail_bookmark_{word}",
            use_container_width=True,
            type="primary" if not is_bookmarked else "secondary"
        ):
            if is_bookmarked:
                st.session_state.bookmarks.remove(word)
            else:
                st.session_state.bookmarks.add(word)
            st.rerun()
    
    # Display full entry
    st.markdown(
        display_entry_card(word, entry, show_details=True, show_related=True),
        unsafe_allow_html=True
    )
    
    # Related words section
    related = st.session_state.dictionary.get_related_words(word)
    if related:
        st.markdown("---")
        st.markdown("### 🔗 Related Words")
        
        related_cols = st.columns(3)
        for i, (rel_word, relation) in enumerate(related):
            with related_cols[i % 3]:
                if rel_word in st.session_state.dictionary.entries:
                    rel_entry = st.session_state.dictionary.entries[rel_word]
                    
                    st.markdown(f"**{relation.title()}:**")
                    st.markdown(
                        display_entry_card(rel_word, rel_entry),
                        unsafe_allow_html=True
                    )
                    
                    if st.button(f"View {rel_word}", key=f"related_{rel_word}_{i}"):
                        st.session_state.current_word = rel_word
                        st.rerun()

def show_statistics():
    """Show comprehensive dictionary statistics"""
    st.markdown("## 📊 Dictionary Statistics & Analytics")
    
    stats = st.session_state.dictionary.get_enhanced_statistics()
    
    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Total Entries</div>
            <div class="stat-number">{stats['total_entries']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Entry Types</div>
            <div class="stat-number">{len(stats['entry_types'])}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Semantic Fields</div>
            <div class="stat-number">{len(stats['semantic_fields'])}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        compound_percentage = (stats['has_components'] / stats['total_entries'] * 100) if stats['total_entries'] > 0 else 0
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Compounds</div>
            <div class="stat-number">{compound_percentage:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Loaded statistics from JSON
    if stats['loaded_stats']:
        st.markdown("### 📈 Generation Statistics")
        
        gen_stats = stats['loaded_stats']
        cols = st.columns(4)
        
        stat_items = [
            ('base_words', 'Base Words'),
            ('morphological_forms', 'Morphological Forms'),
            ('compounds', 'Compounds'),
            ('derivatives', 'Derivatives'),
            ('prefixed_verbs', 'Prefixed Verbs'),
            ('participles', 'Participles'),
            ('sandhi_variants', 'Sandhi Variants'),
            ('technical_terms', 'Technical Terms')
        ]
        
        for i, (key, label) in enumerate(stat_items):
            if key in gen_stats:
                with cols[i % 4]:
                    st.metric(label, f"{gen_stats[key]:,}")
    
    # Charts
    st.markdown("### 📊 Visual Analytics")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Entry Types", "Semantic Fields", "Quality & Frequency", "Word Analysis"])
    
    with tab1:
        # Entry types chart
        if stats['entry_types']:
            top_types = dict(stats['entry_types'].most_common(20))
            
            fig = px.bar(
                x=list(top_types.values()),
                y=[format_entry_type(t) for t in top_types.keys()],
                orientation='h',
                title="Top 20 Entry Types",
                labels={'x': 'Count', 'y': 'Entry Type'},
                color=list(top_types.values()),
                color_continuous_scale='Blues'
            )
            fig.update_layout(height=600, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Semantic fields
        if stats['semantic_fields']:
            top_fields = dict(stats['semantic_fields'].most_common(15))
            
            fig = px.sunburst(
                path=[px.Constant("All Fields")] + list(top_fields.keys()),
                values=[sum(top_fields.values())] + list(top_fields.values()),
                title="Semantic Field Distribution"
            )
            fig.update_layout(height=600)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            # Quality distribution
            if stats['quality_scores']:
                fig = px.pie(
                    values=list(stats['quality_scores'].values()),
                    names=list(stats['quality_scores'].keys()),
                    title="Entry Quality Distribution",
                    color_discrete_map={
                        'excellent': '#4CAF50',
                        'good': '#8BC34A',
                        'acceptable': '#FFC107',
                        'poor': '#FF5722'
                    }
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Frequency distribution
            if stats['frequency_distribution']:
                fig = px.bar(
                    x=list(stats['frequency_distribution'].keys()),
                    y=list(stats['frequency_distribution'].values()),
                    title="Frequency Distribution",
                    labels={'x': 'Frequency Level', 'y': 'Count'},
                    color=list(stats['frequency_distribution'].values()),
                    color_continuous_scale='Reds'
                )
                fig.update_layout(height=400, showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            # Word length distribution
            if stats['word_lengths']:
                fig = px.histogram(
                    x=stats['word_lengths'],
                    nbins=30,
                    title="Word Length Distribution",
                    labels={'x': 'Word Length (characters)', 'y': 'Count'}
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Compound depth distribution
            if stats['compound_depths']:
                fig = px.bar(
                    x=list(stats['compound_depths'].keys()),
                    y=list(stats['compound_depths'].values()),
                    title="Compound Component Count",
                    labels={'x': 'Number of Components', 'y': 'Count'}
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
    
    # Feature statistics
    st.markdown("### 🎯 Feature Coverage")
    
    feature_data = {
        'Feature': ['Has Etymology', 'Has Multiple Senses', 'Has Components', 'Has Related Words'],
        'Count': [stats['has_etymology'], stats['has_senses'], stats['has_components'], stats['has_related']],
        'Percentage': [
            f"{(stats['has_etymology'] / stats['total_entries'] * 100):.1f}%",
            f"{(stats['has_senses'] / stats['total_entries'] * 100):.1f}%",
            f"{(stats['has_components'] / stats['total_entries'] * 100):.1f}%",
            f"{(stats['has_related'] / stats['total_entries'] * 100):.1f}%"
        ]
    }
    
    df = pd.DataFrame(feature_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Metadata display
    if stats['metadata']:
        st.markdown("### ℹ️ Dictionary Metadata")
        
        with st.expander("View metadata", expanded=False):
            st.json(stats['metadata'])
    
    # Close button
    st.markdown("---")
    if st.button("← Back to Search", type="primary"):
        st.session_state.show_stats = False
        st.rerun()

if __name__ == "__main__":
    main()
