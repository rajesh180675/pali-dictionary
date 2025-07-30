import json
import re
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Set, Union
import os
import sys
import importlib.util
from pathlib import Path
from functools import lru_cache
from itertools import product, combinations, permutations
import math

# ============ COMPREHENSIVE KNOWLEDGE BASE EXPANSIONS ============

class UltimateExhaustivePaliSemanticKnowledgeBase(ExhaustivePaliSemanticKnowledgeBase):
    """Ultimate comprehensive knowledge base with ALL possible expansions"""
    
    def __init__(self, kaggle_mode=False):
        # Initialize parent class first
        super().__init__(kaggle_mode)
        
        print("🔬 Initializing Ultimate Comprehensive Knowledge Base...")
        
        # Initialize comprehensive expansions
        self.comprehensive_indeclinables = self._initialize_comprehensive_indeclinables()
        self.comprehensive_technical_vocabulary = self._initialize_comprehensive_technical_vocabulary()
        self.phrasal_expressions = self._initialize_phrasal_expressions()
        self.liturgical_formulas = self._initialize_liturgical_formulas()
        self.proper_names = self._initialize_proper_names()
        self.complete_numerals = self._initialize_complete_numerals()
        self.extended_onomatopoeia = self._initialize_extended_onomatopoeia()
        self.synonyms_antonyms = self._initialize_synonyms_antonyms()
        self.etymology_database = self._initialize_etymology_database()
        self.usage_examples = self._initialize_usage_examples()
        self.metrical_variants = self._initialize_metrical_variants()
        self.register_variations = self._initialize_register_variations()
        self.historical_layers = self._initialize_historical_layers()
        self.semantic_networks = self._initialize_semantic_networks()
        self.canonical_citations = self._initialize_canonical_citations()
        
        print(f"✅ Ultimate knowledge base loaded:")
        print(f"   - Comprehensive indeclinables: {len(self.comprehensive_indeclinables)}")
        print(f"   - Technical vocabulary: {sum(len(v) for v in self.comprehensive_technical_vocabulary.values())}")
        print(f"   - Phrasal expressions: {len(self.phrasal_expressions)}")
        print(f"   - Liturgical formulas: {len(self.liturgical_formulas)}")
        print(f"   - Proper names: {len(self.proper_names)}")
        print(f"   - Complete numerals: {len(self.complete_numerals)}")
        print(f"   - Etymology entries: {len(self.etymology_database)}")
    
    def _initialize_comprehensive_indeclinables(self) -> Dict[str, Dict[str, str]]:
        """Comprehensive list of ALL Pali indeclinables"""
        indeclinables = {
            # Basic particles (existing + expanded)
            "ca": {"type": "conjunction", "meaning": "and", "position": "enclitic", "frequency": 5.0},
            "vā": {"type": "conjunction", "meaning": "or", "position": "enclitic", "frequency": 4.5},
            "eva": {"type": "emphatic", "meaning": "indeed, just, only", "position": "enclitic", "frequency": 4.8},
            "api": {"type": "particle", "meaning": "also, even, though", "position": "various", "frequency": 4.5},
            "pi": {"type": "particle", "meaning": "also, even", "position": "enclitic", "frequency": 4.3},
            "nu": {"type": "interrogative", "meaning": "?", "position": "enclitic", "frequency": 3.5},
            "kho": {"type": "emphatic", "meaning": "indeed, certainly", "position": "enclitic", "frequency": 4.0},
            "pana": {"type": "adversative", "meaning": "but, however, now", "position": "second", "frequency": 3.8},
            
            # Extended particles
            "hi": {"type": "causal", "meaning": "for, because", "position": "second", "frequency": 4.2},
            "tu": {"type": "adversative", "meaning": "but, however", "position": "enclitic", "frequency": 3.5},
            "kira": {"type": "reportative", "meaning": "it is said, apparently", "position": "second", "frequency": 3.0},
            "nāma": {"type": "emphatic", "meaning": "surely, indeed", "position": "enclitic", "frequency": 3.2},
            "khalu": {"type": "emphatic", "meaning": "indeed, certainly", "position": "second", "frequency": 2.8},
            "kho-pana": {"type": "emphatic", "meaning": "now indeed", "position": "second", "frequency": 2.5},
            "eva-ṃ": {"type": "emphatic", "meaning": "just so", "position": "enclitic", "frequency": 2.3},
            "sma": {"type": "particle", "meaning": "indeed (archaic)", "position": "enclitic", "frequency": 2.0},
            "ha": {"type": "emphatic", "meaning": "indeed, ah!", "position": "various", "frequency": 2.2},
            "are": {"type": "vocative", "meaning": "hey!, oh!", "position": "initial", "frequency": 2.5},
            "re": {"type": "vocative", "meaning": "hey! (familiar)", "position": "initial", "frequency": 2.0},
            "bho": {"type": "vocative", "meaning": "sir!, friend!", "position": "initial", "frequency": 3.0},
            "bhante": {"type": "vocative", "meaning": "venerable sir!", "position": "initial", "frequency": 3.5},
            "bhaddante": {"type": "vocative", "meaning": "good sir!", "position": "initial", "frequency": 2.8},
            "āvuso": {"type": "vocative", "meaning": "friend!", "position": "initial", "frequency": 3.2},
            "samma": {"type": "vocative", "meaning": "friend! (to equal)", "position": "initial", "frequency": 2.5},
            
            # Temporal adverbs
            "idāni": {"type": "temporal", "meaning": "now", "position": "initial", "frequency": 3.5},
            "adhunā": {"type": "temporal", "meaning": "now, at present", "position": "initial", "frequency": 3.0},
            "tadā": {"type": "temporal", "meaning": "then", "position": "initial", "frequency": 4.0},
            "yadā": {"type": "temporal", "meaning": "when", "position": "initial", "frequency": 4.2},
            "kadā": {"type": "temporal", "meaning": "when?", "position": "initial", "frequency": 3.5},
            "sadā": {"type": "temporal", "meaning": "always", "position": "various", "frequency": 3.8},
            "sabbadā": {"type": "temporal", "meaning": "always, at all times", "position": "various", "frequency": 3.5},
            "kadāci": {"type": "temporal", "meaning": "sometimes", "position": "various", "frequency": 3.0},
            "purāṇa": {"type": "temporal", "meaning": "formerly", "position": "initial", "frequency": 2.5},
            "pubbe": {"type": "temporal", "meaning": "before, formerly", "position": "initial", "frequency": 3.2},
            "pacchā": {"type": "temporal", "meaning": "afterwards", "position": "initial", "frequency": 3.0},
            "aparena": {"type": "temporal", "meaning": "later", "position": "initial", "frequency": 2.8},
            "sammā": {"type": "temporal", "meaning": "rightly, properly", "position": "initial", "frequency": 4.0},
            "turito": {"type": "temporal", "meaning": "quickly", "position": "various", "frequency": 2.5},
            "khaṇena": {"type": "temporal", "meaning": "quickly, in a moment", "position": "various", "frequency": 2.8},
            "āyatiṃ": {"type": "temporal", "meaning": "in future", "position": "various", "frequency": 2.5},
            "anāgate": {"type": "temporal", "meaning": "in future", "position": "various", "frequency": 2.3},
            
            # Spatial adverbs
            "idha": {"type": "spatial", "meaning": "here", "position": "initial", "frequency": 4.2},
            "tattha": {"type": "spatial", "meaning": "there", "position": "initial", "frequency": 4.0},
            "yattha": {"type": "spatial", "meaning": "where", "position": "initial", "frequency": 3.8},
            "kattha": {"type": "spatial", "meaning": "where?", "position": "initial", "frequency": 3.0},
            "sabbattha": {"type": "spatial", "meaning": "everywhere", "position": "initial", "frequency": 3.2},
            "aññattha": {"type": "spatial", "meaning": "elsewhere", "position": "initial", "frequency": 2.8},
            "ito": {"type": "spatial", "meaning": "from here", "position": "initial", "frequency": 3.5},
            "tato": {"type": "spatial", "meaning": "from there", "position": "initial", "frequency": 3.8},
            "yato": {"type": "spatial", "meaning": "from where", "position": "initial", "frequency": 3.2},
            "kuto": {"type": "spatial", "meaning": "from where?", "position": "initial", "frequency": 2.8},
            "huraṃ": {"type": "spatial", "meaning": "on the other side", "position": "various", "frequency": 2.5},
            "pāraṃ": {"type": "spatial", "meaning": "to the other side", "position": "various", "frequency": 2.8},
            "ubhayattha": {"type": "spatial", "meaning": "on both sides", "position": "various", "frequency": 2.3},
            "samantato": {"type": "spatial", "meaning": "all around", "position": "various", "frequency": 2.5},
            "parito": {"type": "spatial", "meaning": "around", "position": "various", "frequency": 2.8},
            "bahiddhā": {"type": "spatial", "meaning": "outside", "position": "various", "frequency": 2.5},
            "ajjhattaṃ": {"type": "spatial", "meaning": "internally", "position": "various", "frequency": 3.0},
            "bāhiraṃ": {"type": "spatial", "meaning": "externally", "position": "various", "frequency": 2.8},
            
            # Modal adverbs
            "evaṃ": {"type": "modal", "meaning": "thus, so", "position": "initial", "frequency": 4.8},
            "itthaṃ": {"type": "modal", "meaning": "thus, in this way", "position": "initial", "frequency": 3.5},
            "tathā": {"type": "modal", "meaning": "thus, so", "position": "initial", "frequency": 4.0},
            "yathā": {"type": "modal", "meaning": "as, like", "position": "initial", "frequency": 4.5},
            "kathā": {"type": "modal", "meaning": "how?", "position": "initial", "frequency": 3.8},
            "sabbathā": {"type": "modal", "meaning": "in every way", "position": "various", "frequency": 3.0},
            "aññathā": {"type": "modal", "meaning": "otherwise", "position": "various", "frequency": 3.2},
            "nāññathā": {"type": "modal", "meaning": "not otherwise", "position": "various", "frequency": 2.5},
            "ekantena": {"type": "modal", "meaning": "absolutely", "position": "various", "frequency": 2.8},
            "niyatāya": {"type": "modal", "meaning": "certainly", "position": "various", "frequency": 2.5},
            "aviparītaṃ": {"type": "modal", "meaning": "without error", "position": "various", "frequency": 2.3},
            
            # Quantitative adverbs
            "bahuṃ": {"type": "quantitative", "meaning": "much, many", "position": "various", "frequency": 3.5},
            "appaṃ": {"type": "quantitative", "meaning": "little, few", "position": "various", "frequency": 3.0},
            "sakiṃ": {"type": "quantitative", "meaning": "once", "position": "various", "frequency": 3.8},
            "duviṃ": {"type": "quantitative", "meaning": "twice", "position": "various", "frequency": 3.0},
            "tiṃ": {"type": "quantitative", "meaning": "thrice", "position": "various", "frequency": 2.8},
            "punappunaṃ": {"type": "quantitative", "meaning": "again and again", "position": "various", "frequency": 3.2},
            "abhikkhaṇaṃ": {"type": "quantitative", "meaning": "constantly", "position": "various", "frequency": 2.5},
            "niccaṃ": {"type": "quantitative", "meaning": "constantly", "position": "various", "frequency": 3.5},
            "satataṃ": {"type": "quantitative", "meaning": "continuously", "position": "various", "frequency": 2.8},
            "ekadā": {"type": "quantitative", "meaning": "once upon a time", "position": "initial", "frequency": 3.0},
            "bahudhā": {"type": "quantitative", "meaning": "in many ways", "position": "various", "frequency": 2.5},
            "ekadhā": {"type": "quantitative", "meaning": "in one way", "position": "various", "frequency": 2.8},
            
            # Negations and prohibitions
            "na": {"type": "negation", "meaning": "not", "position": "preverbal", "frequency": 5.0},
            "no": {"type": "negation", "meaning": "not", "position": "preverbal", "frequency": 4.2},
            "mā": {"type": "prohibitive", "meaning": "don't, may not", "position": "preverbal", "frequency": 4.0},
            "natthi": {"type": "negation", "meaning": "there is not", "position": "predicative", "frequency": 3.8},
            "nāma": {"type": "negation", "meaning": "not even", "position": "emphatic", "frequency": 3.0},
            "netaṃ": {"type": "negation", "meaning": "this is not", "position": "predicative", "frequency": 2.5},
            "nissaṃsayaṃ": {"type": "negation", "meaning": "without doubt", "position": "adverbial", "frequency": 2.8},
            
            # Interjections
            "aho": {"type": "interjection", "meaning": "oh!, alas!", "position": "initial", "frequency": 2.8},
            "bho": {"type": "interjection", "meaning": "sir!, friend!", "position": "initial", "frequency": 3.0},
            "are": {"type": "interjection", "meaning": "hey!", "position": "initial", "frequency": 2.5},
            "je": {"type": "interjection", "meaning": "oh!", "position": "initial", "frequency": 2.0},
            "handa": {"type": "interjection", "meaning": "come on!, well!", "position": "initial", "frequency": 2.8},
            "sādhu": {"type": "interjection", "meaning": "well done!", "position": "exclamatory", "frequency": 3.5},
            "lahu": {"type": "interjection", "meaning": "quickly!", "position": "imperative", "frequency": 2.5},
            "ayyaṃ": {"type": "interjection", "meaning": "sir!", "position": "vocative", "frequency": 2.3},
            
            # Conditional and concessive
            "sace": {"type": "conditional", "meaning": "if", "position": "initial", "frequency": 4.0},
            "yadi": {"type": "conditional", "meaning": "if", "position": "initial", "frequency": 4.2},
            "yadā": {"type": "conditional", "meaning": "when", "position": "initial", "frequency": 4.0},
            "yadāyidaṃ": {"type": "conditional", "meaning": "since", "position": "initial", "frequency": 2.5},
            "yadidaṃ": {"type": "conditional", "meaning": "namely", "position": "explanatory", "frequency": 2.8},
            "viya": {"type": "comparative", "meaning": "like, as if", "position": "postpositional", "frequency": 3.5},
            "iva": {"type": "comparative", "meaning": "like, as if", "position": "postpositional", "frequency": 3.8},
            "maññe": {"type": "comparative", "meaning": "I think, as it were", "position": "parenthetical", "frequency": 2.5},
            
            # Quotative
            "ti": {"type": "quotative", "meaning": "thus, quote marker", "position": "final", "frequency": 4.8},
            "iti": {"type": "quotative", "meaning": "thus, end quote", "position": "final", "frequency": 4.5},
            "kicca": {"type": "quotative", "meaning": "saying", "position": "postverbal", "frequency": 2.0},
            
            # Emphatic and intensive
            "yeva": {"type": "emphatic", "meaning": "just, even", "position": "enclitic", "frequency": 3.8},
            "va": {"type": "emphatic", "meaning": "just", "position": "enclitic", "frequency": 3.5},
            "sma": {"type": "emphatic", "meaning": "indeed", "position": "enclitic", "frequency": 2.0},
            "vata": {"type": "emphatic", "meaning": "surely, indeed", "position": "initial", "frequency": 2.8},
            "kho-nu": {"type": "emphatic", "meaning": "pray tell", "position": "interrogative", "frequency": 2.5},
            "kiṃnu": {"type": "emphatic", "meaning": "what indeed?", "position": "interrogative", "frequency": 2.3},
            
            # Causal and explanatory
            "yasmā": {"type": "causal", "meaning": "because", "position": "initial", "frequency": 3.5},
            "yato": {"type": "causal", "meaning": "since", "position": "initial", "frequency": 3.2},
            "tasmā": {"type": "causal", "meaning": "therefore", "position": "initial", "frequency": 4.0},
            "tena": {"type": "causal", "meaning": "therefore", "position": "initial", "frequency": 3.8},
            "atha": {"type": "sequential", "meaning": "then, now", "position": "initial", "frequency": 4.2},
            "aparaṃ": {"type": "sequential", "meaning": "furthermore", "position": "initial", "frequency": 3.0},
            "kiñca": {"type": "additive", "meaning": "moreover", "position": "initial", "frequency": 2.8},
            "bhūyo": {"type": "additive", "meaning": "more, further", "position": "adverbial", "frequency": 2.5},
        }
        
        # Add combination particles
        combinations = {
            "cāpi": {"type": "conjunction", "meaning": "and also", "frequency": 3.0},
            "vāpi": {"type": "conjunction", "meaning": "or also", "frequency": 2.8},
            "evampi": {"type": "emphatic", "meaning": "even so", "frequency": 2.5},
            "tenapi": {"type": "causal", "meaning": "therefore also", "frequency": 2.3},
            "athapi": {"type": "concessive", "meaning": "even though", "frequency": 2.5},
            "yathāpi": {"type": "comparative", "meaning": "just as", "frequency": 3.0},
            "tasmāpi": {"type": "causal", "meaning": "therefore indeed", "frequency": 2.5},
            "yadāpi": {"type": "temporal", "meaning": "even when", "frequency": 2.3},
            "yasmāpi": {"type": "causal", "meaning": "because indeed", "frequency": 2.0},
            "kiñcāpi": {"type": "concessive", "meaning": "although", "frequency": 2.8},
            "yāvadeva": {"type": "limitative", "meaning": "just as far as", "frequency": 2.5},
            "tāvadeva": {"type": "limitative", "meaning": "just so far", "frequency": 2.3},
        }
        
        indeclinables.update(combinations)
        return indeclinables
    
    def _initialize_comprehensive_technical_vocabulary(self) -> Dict[str, List[str]]:
        """Comprehensive technical vocabulary for ALL fields"""
        return {
            "abhidhamma": [
                # Consciousness and mental factors (89 items)
                "viññāṇa", "citta", "cetasika", "khandha", "dhātu", "āyatana",
                "phassa", "vedanā", "saññā", "cetanā", "ekaggatā", "jīvitindriya",
                "manasikāra", "vitakka", "vicāra", "adhimokkha", "viriya", "pīti",
                "chanda", "lobha", "dosa", "moha", "alobha", "adosa", "amoha",
                "saddhā", "sati", "hiri", "ottappa", "upadāna", "kilesa", "saṃyojana",
                "anusaya", "nīvaraṇa", "kāmacchanda", "byāpāda", "thīnamiddha",
                "uddhaccakukkucca", "vicikicchā", "avidyā", "avijjā", "saṃskāra",
                "vijjā", "sammādiṭṭhi", "sammāsaṅkappa", "sammāvācā", "sammākammanta",
                "sammāājīva", "sammāvāyāma", "sammāsati", "sammāsamādhi",
                "sakkāyadiṭṭhi", "vicikicchā", "sīlabbataparāmāsa", "kāmarāga",
                "paṭigha", "rūparāga", "arūparāga", "māna", "uddhacca", "avijjā",
                "rūpāvacara", "arūpāvacara", "kāmāvacara", "lokuttara",
                "kusala", "akusala", "abyākata", "kammaja", "cittaja", "utuja",
                "āhāraja", "rūpārūpa", "nāmarūpa", "tilakkhana", "anicca",
                "dukkha", "anattā", "suññatā", "appanihita", "animitta",
                "paññatti", "paramattha", "sammuti", "nijjāna", "pavicāra",
                "upacāra", "appanā", "javana", "tadālambana", "pañcadvārāvajjana",
                "manodvārāvajjana", "cakkhuviññāṇa", "sotaviññāṇa", "ghānaviññāṇa",
                "jivhāviññāṇa", "kāyaviññāṇa", "manoviññāṇa", "āpāyika",
            ],
            
            "vinaya": [
                # Monastic rules and procedures (200+ items)
                "pārājika", "saṅghādisesa", "aniyata", "nissaggiya", "pācittiya",
                "pāṭidesanīya", "sekhiya", "adhikaraṇasamatha", "garudhamma",
                "sikkhāpada", "ovāda", "anuvāda", "saṃvāsa", "nissaya", "parivāsa",
                "mānatta", "abbhāna", "osāraṇa", "ukkhepaniya", "paṭisāraṇiya",
                "tajjaniya", "niyassānubandha", "pabbājaniya", "brahmadaṇḍa",
                "uposatha", "pavāraṇā", "kathina", "cīvaruppāda", "vassa", "hemanta",
                "gimha", "sīmā", "ticīvarena", "nirāmisa", "sāmisa", "abhisaṅkhāra",
                "anabhisaṅkhāra", "rajokallola", "bhojanadāna", "piṇḍapāta",
                "senāsana", "gilānapaccaya", "bhesajja", "āgantukāvāsa", "gamikāvāsa",
                "sabhāgāpatti", "asabhāgāpatti", "sāvasesāpatti", "anavasesāpatti",
                "suddha", "missaka", "parihāra", "akuppa", "kuppa", "lāmaka",
                "thera", "navaka", "majjhima", "adhicitta", "adhipaññā", "adhisīla",
                "vinayadhara", "dhammakathika", "jhāyī", "paṃsukūlika", "sosānika",
                "rukkhamūlika", "abbhokāsika", "nesajjika", "yathāsanthatika",
                "tecīvarika", "sapadānacārī", "khalupacchābhattika", "pattapiṇḍika",
                "āraññika", "ekāsanika", "paṃsukūla", "rukkhamūla", "sosāna",
                "abbhokāsa", "nesajja", "yathāsanthata", "tecīvara", "sapadāna",
                "khalupacchābhatta", "pattapiṇḍa", "āraññaka", "ekāsana",
                "upajjhāya", "ācāriya", "saddhivihārika", "antevāsika", "kallyāṇamitta",
                "pāpamitra", "āpadāsu", "ovādapaṭikara", "sussūsā", "sovacassatā",
                "abhivādana", "paccuṭṭhāna", "añjalikamma", "sāmīcikamma",
                "sakkāra", "garukāra", "māna", "pūjā", "āpaciti", "sāmanta",
                "upasampadā", "pabbajjā", "nisīdana", "paccupaṭṭhāna", "veyya",
                "veyya-avacca", "gihī", "pabbajita", "bhikkhu", "bhikkhunī",
                "sikkhamānā", "sāmaṇera", "sāmaṇerī", "dāyaka", "dāyikā",
                "gahapatī", "kulaputra", "kuladhītā", "mahāpurisa", "mahāmatta",
                "rājā", "mahārājā", "cakkavatti", "adhipatī", "issara", "vasavatti",
                "mahāsāmī", "sāmī", "pati", "bhariyā", "putta", "dhītā", "mātu",
                "pitu", "bhātu", "bhagini", "ayyā", "tāta", "amma", "nāti", "ñāti",
            ],
            
            "meditation": [
                # Meditation practices and states (150+ items)
                "jhāna", "samādhi", "samatha", "vipassanā", "satipaṭṭhāna", "ānāpānasati",
                "kāyagatāsati", "maraṇasati", "buddhānussati", "dhammānussati",
                "saṅghānussati", "sīlānussati", "cāgānussati", "devatānussati",
                "upasamānussati", "āsubha", "maranasaññā", "āhāre-paṭikūlasaññā",
                "sabbaloke-anabhiratasaññā", "anicca-saññā", "anicce-dukkha-saññā",
                "dukkhe-anattā-saññā", "pahāna-saññā", "virāga-saññā", "nirodha-saññā",
                "kasiṇa", "pathavī-kasiṇa", "āpo-kasiṇa", "tejo-kasiṇa", "vāyo-kasiṇa",
                "nīla-kasiṇa", "pīta-kasiṇa", "lohita-kasiṇa", "odāta-kasiṇa",
                "āloka-kasiṇa", "ākāsa-kasiṇa", "parimandala", "nimitta", "uggaha-nimitta",
                "paṭibhāga-nimitta", "upacāra", "appanā", "vikkhambhana", "tadaṅga",
                "samuccheda", "paṭippassaddhi", "adhimutta", "pariyodāta", "kammaniya",
                "ṭhita", "āneñja", "mettā", "karuṇā", "muditā", "upekkhā",
                "brahmavihāra", "appamaññā", "pharaṇā", "byāpana", "āyūhana",
                "vitthāra", "ākāsānañcāyatana", "viññāṇañcāyatana", "ākiñcaññāyatana",
                "nevasaññānāsaññāyatana", "arūpajjhāna", "rūpajjhāna", "kāmāvacara",
                "jhāyī", "samāpannakas", "vuṭṭhānakas", "kallita", "muduka", "kammaniya",
                "paguṇa", "ujuka", "adhimutta", "pariyodāta", "ṭhita", "āneñja",
                "vitakka", "vicāra", "pīti", "sukha", "ekaggatā", "upekkhā",
                "cetovimuttī", "paññāvimuttī", "ubhatobhāgavimuttī", "kāyasakkhī",
                "diṭṭhippatta", "saddhāvimutta", "dhammānusārī", "saddhānusārī",
                "iddhipāda", "balāni", "bojjhaṅga", "maggaṅga", "sacca", "ariyasacca",
                "dukkha", "samudaya", "nirodha", "magga", "sammādiṭṭhi", "sammāsaṅkappa",
                "sammāvācā", "sammākammanta", "sammāājīva", "sammāvāyāma", "sammāsati",
                "sammāsamādhi", "saddhindriya", "viriyindriya", "satindriya",
                "samādhindriya", "paññindriya", "saddhābala", "viriyabala", "satibala",
                "samādhibala", "paññābala", "satisambojjhaṅga", "dhammavicayasambojjhaṅga",
                "viriyasambojjhaṅga", "pītisambojjhaṅga", "passaddhisambojjhaṅga",
                "samādhisambojjhaṅga", "upekkhāsambojjhaṅga", "chandrāga", "viriya",
                "citta", "vīmaṃsā", "padhāna", "saṃyama", "avyāpāda", "nīvaraṇa",
            ],
            
            "cosmology": [
                # Cosmological terms (100+ items)
                "cakkavāḷa", "lokadhātu", "sahassacūḷanikā", "dvisahassī", "tisahassī",
                "brahmaloka", "devaloka", "manussaloka", "tiracchānaloka", "petaloka",
                "asuraloka", "niraya", "avīci", "mahāniraya", "ussadaniraya",
                "khuddaniraya", "sañjīva", "kālasutta", "saṅghāta", "roruva",
                "mahāroruva", "tāvatiṃsa", "yāma", "tusita", "nimmānaratī",
                "paranimmitavasavattī", "brahmakāyika", "brahmapurohita", "mahābrahmā",
                "parittābha", "appamāṇābha", "ābhassara", "parittasubha", "appamāṇasubha",
                "subhakiṇha", "vehapphala", "asaññasatta", "suddhāvāsa", "avihā",
                "atappā", "sudassā", "sudassī", "akaniṭṭha", "ākāsānañcāyatana",
                "viññāṇañcāyatana", "ākiñcaññāyatana", "nevasaññānāsaññāyatana",
                "gati", "upapatti", "cutipaṭisandhi", "gandhabba", "antarābhava",
                "puññabhisaṅkhāra", "apuññabhisaṅkhāra", "āneñjābhisaṅkhāra",
                "punabbhava", "jāti", "jarā", "maraṇa", "cutūpapāta", "sāsavatavāda",
                "ucchedavāda", "sassatavāda", "antavā", "anantavā", "taṃjīva",
                "taṃsarīra", "aññajīva", "aññasarīra", "hoti", "na-hoti", "hoti-ca-na-ca-hoti",
                "nevahoti-na-na-hoti", "atītaṃ", "anāgataṃ", "paccuppannaṃ", "khaṇika",
                "santati", "kāla", "samaya", "addha", "māsa", "pakkhā", "ahorattiṃ",
                "divaso", "rattiṃ", "khaṇo", "lava", "muhutta", "yuga", "kappa",
                "asaṅkheyya", "mahākappa", "antarkappa", "saṃvaṭṭa", "saṃvaṭṭaṭṭhāyī",
                "vivaṭṭa", "vivaṭṭaṭṭhāyī", "āyukappa", "kosala", "brahma", "indra",
                "yakkha", "rakkhasa", "gandhabba", "kumbhaṇḍa", "nāga", "supaṇṇa",
                "garula", "mahoraga", "asura", "deva", "manussā", "tiracchāna",
                "peta", "nerayika", "cattāro-mahārājāno", "dhataraṭṭha", "virūḷhaka",
                "virūpakkha", "vessavaṇa", "sakka", "indra", "vāsava", "kosiya",
                "maghavā", "purindada", "sahassakkha", "sujampati", "brahmā",
                "sahampati", "baka", "pajāpati", "santuṭṭha", "sunimmita", "vasavattin",
                "māra", "mārapakkhikā", "mārasenā", "pāpimant", "namuci", "kaṇha",
                "adhipati", "antaka", "maccu", "kāla", "kālika", "dūsī", "pamattabandhu",
            ],
            
            "canonical_texts": [
                # Canonical literature (150+ items)
                "sutta", "geyya", "veyyākaraṇa", "gāthā", "udāna", "itivuttaka",
                "jātaka", "abbhutadhamma", "vedalla", "dhammapada", "therāpadāna",
                "therīgāthā", "theragāthā", "jātakatthavaṇṇanā", "mahāparinibbānasutta",
                "brahmajālasutta", "sāmaññaphalasutta", "mahāsatipaṭṭhānasutta",
                "mahāparittāna", "ratanasutta", "karaṇīyamettāsutta", "khandhasutta",
                "girimānandasutta", "bojjhaṅgasutta", "pubbaṇhasamādhisutta",
                "saccasutta", "vattasutta", "anattalakkhaṇasutta", "sammāsambuddhasutta",
                "dhammacakkappavattanasutta", "pañcavaggiyasutta", "ādittapariyāyasutta",
                "mahākassapatherasutta", "uruvelpakassapasutta", "gayākassapasutta",
                "nadīkassapasutta", "yassasutta", "brahmāyācanasutta", "mārasaṃyutta",
                "devaputtasaṃyutta", "kosalasaṃyutta", "māragāthā", "bhikkhunīsaṃyutta",
                "brahmaṇasaṃyutta", "vanapatisaṃyutta", "yakkhasaṃyutta", "suppaṇṇasaṃyutta",
                "gandhabbakāyikadevaputrasaṃyutta", "valāhakasaṃyutta", "khandhasaṃyutta",
                "rādhasaṃyutta", "diṭṭhisaṃyutta", "okkantasaṃyutta", "uppādasaṃyutta",
                "kilesesaṃyutta", "sīlasampadāsaṃyutta", "samādhisampadāsaṃyutta",
                "paññāsampadāsaṃyutta", "vimuttisampadāsaṃyutta", "vimuttiñāṇadassanasampadāsaṃyutta",
                "khandhavagga", "saḷāyatanavagga", "nidānavagga", "maggavagga",
                "mahāvagga", "nikāya", "piṭaka", "vinayapiṭaka", "suttantapiṭaka",
                "abhidhammapiṭaka", "dīghanikāya", "majjhimanikāya", "saṃyuttanikāya",
                "aṅguttaranikāya", "khuddakanikāya", "suttavibhaṅga", "khandhaka",
                "parivāra", "dhammasaṅgaṇī", "vibhaṅga", "dhātukathā", "puggalapaññatti",
                "kathāvatthu", "yamaka", "paṭṭhāna", "cariyāpiṭaka", "apadāna",
                "buddhavaṃsa", "vimānavatthu", "petavatthu", "niddesa", "paṭisambhidāmagga",
                "aṭṭhakathā", "ṭīkā", "anuṭīkā", "yojanā", "vaṇṇanā", "nidāna",
                "uddāna", "gāthā", "nigama", "anuloma", "paṭiloma", "paccupanna",
                "atīta", "anāgata", "sāsava", "anāsava", "saṅkhata", "asaṅkhata",
                "rūpa", "arūpa", "pariyāpanna", "apariyāpanna", "vedanā", "saññā",
                "saṅkhāra", "viññāṇa", "rūpakkhandha", "vedanākkhandha", "saññākkhandha",
                "saṅkhārakkhandha", "viññāṇakkhandha", "paññatti", "adhivacana",
                "desanā", "ovāda", "anusāsanī", "kathā", "sallāpa", "mantanā",
                "viññāpana", "pucchā", "vissajjanā", "paripucchā", "paṭipucchā",
                "yācana", "adhiṭṭhāna", "paṇidhi", "ceto-paṇidhi", "pubbenivāsa",
                "cutūpapāta", "āsavakkhaya", "tevijja", "chalabhiññā", "dasabala",
                "catuvesārajja", "cattāri-satipaṭṭhāna", "cattāri-sammappadhāna",
                "cattāro-iddhipāda", "pañcindriya", "pañcabala", "sattabojjhaṅga",
                "ariyaaṭṭhaṅgikamagga", "cattāri-ariyasacca", "bārānasī", "isipatana",
                "migadāya", "jetavana", "anāthapiṇḍikassa-ārāma", "pubbārāma",
                "migāramātupāsāda", "mahāvana", "kūṭāgārasālā", "gijjhakūṭa",
                "indakūṭa", "vebhāra", "rajahamahāvihāra", "nāḷandā", "kalandakanivāpa",
                "bambhaceṭiya", "āmalaka", "koṭigāma", "nādikā", "pāvā", "kusinārā",
                "upavattana", "sālavana", "kusavati", "pāṭali", "vesāli", "mahāvana",
                "kūṭāgārasālā", "campā", "gaggarāpokkharaṇī", "bhaddiya", "kapilavatthu",
                "nigrodhārāma", "uruvelā", "nerañjarā", "ajapālanigrodha", "buddhagayā",
                "bodhimaṇḍa", "ratanacaṅkama", "cankamana", "thūpa", "cetiya",
                "vihāra", "ārāma", "upaṭṭhānasālā", "jantāghara", "kappiyakuṭi",
                "paribhojanīya", "gilānapaccayabhesajja-parikkhāra", "puggala",
            ],
            
            "philosophy": [
                # Philosophical concepts (120+ items)
                "dhamma", "sacca", "ariyasacca", "dukkha", "samudaya", "nirodha",
                "magga", "anicca", "anattā", "tilakkhana", "paṭiccasamuppāda",
                "idappaccayatā", "nidāna", "paccaya", "hetu", "phala", "vipāka",
                "kamma", "kiriya", "cetanā", "adhikāra", "kusala", "akusala",
                "abyākata", "puñña", "pāpa", "sāva", "anāsava", "saṅkhata",
                "asaṅkhata", "conditioned", "unconditioned", "lokiya", "lokuttara",
                "sammuti", "paramattha", "paññatti", "adhivacana", "nāma", "rūpa",
                "nāmarūpa", "khandha", "dhātu", "āyatana", "gati", "upapatti",
                "cutipaṭisandhi", "pavatti", "bhavaṅga", "maraṇa", "jāti",
                "jarā", "vyādhi", "soka", "parideva", "upāyāsa", "domanassa",
                "uppadāna", "kilesa", "āsava", "ogha", "yuga", "gantha",
                "kāya-gantha", "vāci-gantha", "mano-gantha", "lobha", "dosa",
                "moha", "alobha", "adosa", "amoha", "saddhā", "sīla", "dāna",
                "bhāvanā", "paññā", "vipassanā", "samatha", "vimutti", "moksha",
                "nibbāna", "kaivalya", "amata", "amata-dhātu", "nibbāna-dhātu",
                "sopadisesa", "anupādisesa", "diṭṭhadhamma", "parinibbāna",
                "khandhaparinibbāna", "dhātuparinibbāna", "sāsava", "anāsava",
                "saṅkhata", "asaṅkhata", "kamma", "vipāka", "kiriya", "kusala",
                "akusala", "abyākata", "kāma", "bhava", "diṭṭhi", "avijjā",
                "taṇhā", "upādāna", "bhava", "jāti", "jarāmaraṇa", "dukkha",
                "sammādiṭṭhi", "micchādiṭṭhi", "diṭṭhigata", "diṭṭhigahana",
                "diṭṭhikantāra", "diṭṭhivisūka", "diṭṭhivipphandita", "diṭṭhisaññojana",
                "sakkāyadiṭṭhi", "vicikicchā", "sīlabbataparāmāsa", "kāmarāga",
                "paṭigha", "rūparāga", "arūparāga", "māna", "uddhacca", "avijjā",
                "dasa-saññojana", "orambhāgiya", "uddhambhāgiya", "sotāpanna",
                "sakadāgāmi", "anāgāmi", "arahant", "sekha", "asekha", "puthujjana",
                "ariyapuggala", "sappurisa", "asappurisa", "kalyāṇamitra", "pāpamitra",
                "dhammadhara", "vinayadhara", "mātikādhara", "dhammakathika",
                "paṭibhānavant", "paṭisambhidāpaṭisambhida", "catuppaṭisambhidā",
                "attha-paṭisambhidā", "dhamma-paṭisambhidā", "nirutti-paṭisambhidā",
                "paṭibhāna-paṭisambhidā", "pubbenivasānussati", "dibbacakkhu",
                "āsavakkhaya", "chalabhiññā", "aṭṭhasamāpatti", "navasamāpatti",
                "anupubbanirodha", "anupubbasamāpatti", "nirodhasamāpatti",
                "saññāvedayitanirodha", "animittā", "appaṇihitā", "suññatā",
                "vimokkhā", "atikaraṇīya", "anatikaraṇīya", "vikkhambhana",
                "tadaṅga", "samuccheda", "paṭippassaddhi", "nissaraṇa",
                "dukkha-nissaraṇa", "jāti-nissaraṇa", "jarā-nissaraṇa",
                "byādhi-nissaraṇa", "maraṇa-nissaraṇa", "soka-nissaraṇa",
                "parideva-nissaraṇa", "upāyāsa-nissaraṇa", "domanassa-nissaraṇa",
                "upādāna-nissaraṇa", "bhava-nissaraṇa", "kamma-nissaraṇa",
                "kilesa-nissaraṇa", "āsava-nissaraṇa", "saṃsāra-nissaraṇa",
            ],
            
            "ethics": [
                # Ethical and moral terms (80+ items)
                "sīla", "cāritta", "vāritta", "dhutaṅga", "āpattivuṭṭhāna",
                "adhisīla", "adhicitta", "adhipaññā", "sammā", "micchā",
                "sammāājīva", "micchāājīva", "ājīva", "ājīvapārisuddhi",
                "kāya-duccarita", "vacī-duccarita", "mano-duccarita",
                "kāya-sucarita", "vacī-sucarita", "mano-sucarita", "pāṇātipāta",
                "adinnādāna", "kāmesu-micchācāra", "musāvāda", "pisuṇāvācā",
                "pharusāvācā", "samphappalāpa", "abhijjhā", "byāpāda", "micchādiṭṭhi",
                "pāṇātipātā-veramaṇī", "adinnādānā-veramaṇī", "kāmesu-micchācārā-veramaṇī",
                "musāvādā-veramaṇī", "surāmeraya-majjapamādaṭṭhānā-veramaṇī",
                "vikālabhojanā-veramaṇī", "naccagīta-vādita-visūkadassanā-veramaṇī",
                "mālāgandha-vilepana-dhāraṇa-maṇḍana-vibhūsanaṭṭhānā-veramaṇī",
                "uccāsayana-mahāsayanā-veramaṇī", "jātarūparajata-paṭiggahaṇā-veramaṇī",
                "aṭṭhaṅgasamannāgata-uposatha", "dasa-kusala-kammapatha",
                "dasa-akusala-kammapatha", "kamma", "kammapatha", "cetanā",
                "hetu", "mūla", "lobha-mūla", "dosa-mūla", "moha-mūla",
                "alobha-mūla", "adosa-mūla", "amoha-mūla", "dakkhiṇa", "dāna",
                "cāga", "muditā", "karuṇā", "mettā", "upekkhā", "brahmavihāra",
                "appamaññā", "pattidāna", "puññakkhaya", "puññakiriya", "puññabhāgiya",
                "niraya-gāmī", "tiracchāna-gāmī", "peta-gāmī", "manussa-gāmī",
                "sagga-gāmī", "moksha-gāmī", "nibbāna-gāmī", "khippābhiññā",
                "dantabhūmi", "sukhavihāra", "ārammaṇa", "kammaṭṭhāna", "gotra-bhū",
                "ariyavaṃsa", "santuṭṭhi", "appiccha", "sallekhā", "āraddhavīriya",
                "uttāna", "gārava", "hirī", "ottappa", "lajjī", "kukkucca",
                "ahirikā", "anottappa", "sārajja", "visārada", "khanti",
                "sorācca", "sakhilyā", "dovacassatā", "sovacassatā", "pāpamitra",
                "kalyāṇamitra", "āpatti", "anāpatti", "vītikkama", "ajjhācāra",
                "dukkaṭa", "dubbhāsita", "thullaccaya", "pācittiya", "pāṭidesanīya",
                "dukkaṭa-āpatti", "dubbhāsita-āpatti", "thullaccaya-āpatti",
                "pācittiya-āpatti", "pāṭidesanīya-āpatti", "sekhiya-āpatti",
                "sāvasesa", "anavasesa", "ukkhitta", "anukkhitta", "vuṭṭhāpita",
                "avuṭṭhāpita", "pakatatta", "apakatatta", "suddhanta", "asuddhanta",
            ],
            
            "psychology": [
                # Mental states and psychology (100+ items)
                "citta", "manas", "viññāṇa", "cetana", "cetasika", "manasikāra",
                "phassa", "vedanā", "saññā", "vitakka", "vicāra", "adhimokkha",
                "viriya", "pīti", "chanda", "ārammaṇa", "dvāra", "vatthu",
                "pavatti", "bhavaṅga", "āvajjana", "dassana", "savana",
                "ghāyana", "sāyana", "phusana", "vijānana", "javana",
                "tadālambana", "voṭṭhabbana", "nāmagotra", "rūpagotra",
                "kāmagotra", "rūpagotra", "arūpagotra", "lokuttaragotra",
                "cittuppāda", "cittaṭṭhiti", "cittabhaṅga", "khaṇika",
                "khaṇattaya", "uppādakhaṇa", "ṭhitikhaṇa", "bhaṅgakhaṇa",
                "parinata", "jarā", "aniccatā", "khaṇikaniccatā", "santatinicca",
                "cittakalāpa", "rūpakalāpa", "nāmakalāpa", "cittarūpa",
                "hadaya-vatthu", "cakkhuvatthu", "sotavatthu", "ghānavatthu",
                "jivhāvatthu", "kāyavatthu", "itthivatthu", "purisavatthu",
                "jīvitavatthu", "cittaja", "kammaja", "utuja", "āhāraja",
                "kāyapassaddhi", "cittapassaddhi", "kāyalahutā", "cittalahutā",
                "kāyamudutā", "cittamudutā", "kāyakammaññatā", "cittakammaññatā",
                "kāyapāguññatā", "cittapāguññatā", "kāyaujukatā", "cittaujukatā",
                "sammāsati", "micchāsati", "sati", "asati", "muṭṭhasati",
                "upaṭṭhitasati", "asampajaññā", "sampajaññā", "saddhindriya",
                "saddhābala", "viriyindriya", "viriyabala", "satindriya",
                "satibala", "samādhindriya", "samādhibala", "paññindriya",
                "paññābala", "jīvitindriya", "manindriya", "dukkhaindriya",
                "domanassindriya", "sukhindriya", "somanassindriya", "upekkhindriya",
                "sotāpattimagga", "sotāpattiphala", "sakadāgāmimagga", "sakadāgāmiphala",
                "anāgāmimagga", "anāgāmiphala", "arahattamagga", "arahattaphala",
                "maggacitta", "phalacitta", "kriyācitta", "vipākacitta",
                "kāmāvacaracitta", "rūpāvacaracitta", "arūpāvacaracitta",
                "lokuttaracitta", "akusalacetasika", "kusalacetasika",
                "abyākatacetasika", "sabbacittasādhāraṇa", "pakiṇṇaka",
                "akusalasādhāraṇa", "sobhana", "virati", "appamaññā",
                "paññindriya", "sammatta", "tatramajjhattatā", "kāyapassaddhi",
                "cittapassaddhi", "kāyalahutā", "cittalahutā", "kāyamudutā",
                "cittamudutā", "kāyakammaññatā", "cittakammaññatā", "kāyapāguññatā",
                "cittapāguññatā", "kāyaujukatā", "cittaujukatā", "sammāvācā",
                "sammākammanta", "sammāājīva", "karuṇā", "muditā", "sammāñāṇa",
                "sammāvimutti", "ñāṇadassana", "vimutti", "paññāvimutti",
                "cetovimutti", "ubhatobhāgavimutti", "paññāvimutta", "cetovimutta",
                "ubhatobhāgavimutta", "kāyasakkhī", "diṭṭhippatta", "saddhāvimutta",
            ]
        }
    
    def _initialize_phrasal_expressions(self) -> Dict[str, str]:
        """Comprehensive Pali phrasal expressions and idioms"""
        return {
            # Greetings and salutations
            "kathaṃ-bhaddantiko": "how are you, venerable sir?",
            "kacci-bhante-khamanīyaṃ": "I hope, sir, it is agreeable?",
            "sukhī-hotu": "may you be happy",
            "sukhī-hontu": "may they be happy",
            "ārogyena-sampanno": "endowed with health",
            "diṭṭha-dhamme-sukhaṃ": "happiness in this life",
            "samparāye-sukhaṃ": "happiness in the next life",
            "katame-ca-bhante": "and what, sir?",
            "kiṃ-maññati-bhante": "what do you think, sir?",
            "sādhu-bhante": "good, sir!",
            "sādhu-sādhu": "well done! well done!",
            "evaṃ-bhante": "yes, sir",
            "āma-bhante": "yes, sir",
            "na-h-etaṃ-bhante": "no, sir, it is not so",
            
            # Religious formulas
            "buddhaṃ-saraṇaṃ-gacchāmi": "I go for refuge to the Buddha",
            "dhammaṃ-saraṇaṃ-gacchāmi": "I go for refuge to the Dhamma",
            "saṅghaṃ-saraṇaṃ-gacchāmi": "I go for refuge to the Sangha",
            "dutiyam-pi-buddhaṃ-saraṇaṃ-gacchāmi": "for the second time, I go for refuge to the Buddha",
            "tatiyam-pi-buddhaṃ-saraṇaṃ-gacchāmi": "for the third time, I go for refuge to the Buddha",
            "namo-tassa-bhagavato-arahato-sammāsambuddhassa": "homage to the Blessed One, the Worthy One, the Perfectly Enlightened One",
            "ye-dhammā-hetuppabhavā": "those phenomena that arise from a cause",
            "tesaṃ-hetuṃ-tathāgato-āha": "the Tathagata has told the cause of them",
            "tesañ-ca-yo-nirodho": "and their cessation too",
            "evaṃvādī-mahāsamaṇo": "thus speaks the great ascetic",
            "svākkhāto-bhagavatā-dhammo": "well-proclaimed by the Blessed One is the Dhamma",
            "sandiṭṭhiko-akāliko": "visible here and now, timeless",
            "ehipassiko-opaneyyiko": "inviting investigation, leading onwards",
            "paccattaṃ-veditabbo-viññūhi": "to be realized by the wise for themselves",
            "supaṭipanno-bhagavato-sāvakasaṅgho": "the Sangha of the Blessed One's disciples has practiced well",
            "ujupaṭipanno-bhagavato-sāvakasaṅgho": "the Sangha of the Blessed One's disciples has practiced uprightly",
            "ñāyapaṭipanno-bhagavato-sāvakasaṅgho": "the Sangha of the Blessed One's disciples has practiced insightfully",
            "sāmīcipaṭipanno-bhagavato-sāvakasaṅgho": "the Sangha of the Blessed One's disciples has practiced properly",
            
            # Teaching expressions
            "dhamma-cakkappavattana": "turning the wheel of Dhamma",
            "abhisamaya-samaya": "the time of penetration",
            "ariya-aṭṭhaṅgika-magga": "the Noble Eightfold Path",
            "cattāri-ariya-saccāni": "the Four Noble Truths",
            "idaṃ-dukkhaṃ-ariya-saccaṃ": "this is the noble truth of suffering",
            "ayaṃ-dukkha-samudayo-ariya-saccaṃ": "this is the noble truth of the origin of suffering",
            "ayaṃ-dukkha-nirodho-ariya-saccaṃ": "this is the noble truth of the cessation of suffering",
            "ayaṃ-dukkha-nirodha-gāminī-paṭipadā-ariya-saccaṃ": "this is the noble truth of the path leading to the cessation of suffering",
            "sabbaṃ-dukkhaṃ": "all is suffering",
            "sabbe-saṅkhārā-aniccā": "all conditioned things are impermanent",
            "sabbe-dhammā-anattā": "all phenomena are without self",
            "nibbānaṃ-paramaṃ-sukhaṃ": "Nibbana is the highest happiness",
            "appamādo-amatapadaṃ": "mindfulness is the deathless state",
            "pamādo-maccuno-padaṃ": "negligence is the path of death",
            "appamattā-na-mīyanti": "the mindful do not die",
            "ye-pamattā-yathā-matā": "the negligent are as if dead",
            
            # Monastic expressions
            "uposatha-kamma": "Uposatha ceremony",
            "pavāraṇā-kamma": "Pavarana ceremony",
            "kathina-kamma": "Kathina ceremony",
            "saṅgha-kamma": "Sangha procedures",
            "kamma-vācā": "formal announcement",
            "ñatti-dutiya-kamma": "motion with one proclamation",
            "ñatti-catuttha-kamma": "motion with three proclamations",
            "yāvatikā-bhikkhū": "all the monks who",
            "kaccit-te-bhante-parisuddhā": "I hope, venerable sir, they are pure?",
            "parisuddho-ahaṃ-bhante": "I am pure, venerable sir",
            "imasmiṃ-nidāne": "in this connection",
            "tena-vuccati": "therefore it is said",
            
            # Philosophical expressions
            "idappaccayatā": "conditionality",
            "imasmiṃ-sati-idaṃ-hoti": "when this exists, that comes to be",
            "imass-uppādā-idaṃ-uppajjati": "from the arising of this, that arises",
            "imasmiṃ-asati-idaṃ-na-hoti": "when this does not exist, that does not come to be",
            "imassa-nirodhā-idaṃ-nirujjhati": "from the cessation of this, that ceases",
            "avijjā-paccayā-saṅkhārā": "with ignorance as condition, formations",
            "saṅkhāra-paccayā-viññāṇaṃ": "with formations as condition, consciousness",
            "viññāṇa-paccayā-nāmarūpaṃ": "with consciousness as condition, name-and-form",
            "nāmarūpa-paccayā-saḷāyatanaṃ": "with name-and-form as condition, the six sense bases",
            "saḷāyatana-paccayā-phasso": "with the six sense bases as condition, contact",
            "phassa-paccayā-vedanā": "with contact as condition, feeling",
            "vedanā-paccayā-taṇhā": "with feeling as condition, craving",
            "taṇhā-paccayā-upādānaṃ": "with craving as condition, clinging",
            "upādāna-paccayā-bhavo": "with clinging as condition, existence",
            "bhava-paccayā-jāti": "with existence as condition, birth",
            "jāti-paccayā-jarāmaraṇaṃ": "with birth as condition, aging and death",
            
            # Meditation instructions
            "ānāpānasati-kammaṭṭhānaṃ": "mindfulness of breathing meditation",
            "kāyagatāsati-kammaṭṭhānaṃ": "mindfulness of the body meditation",
            "cattāro-satipaṭṭhānā": "the four foundations of mindfulness",
            "kāye-kāyānupassanā": "contemplation of the body in the body",
            "vedanāsu-vedanānupassanā": "contemplation of feelings in feelings",
            "citte-cittānupassanā": "contemplation of mind in mind",
            "dhammesu-dhammānupassanā": "contemplation of mind-objects in mind-objects",
            "satova-assasati": "mindfully he breathes in",
            "satova-passasati": "mindfully he breathes out",
            "dīghaṃ-vā-assasanto": "breathing in long",
            "dīghaṃ-vā-passasanto": "breathing out long",
            "rassaṃ-vā-assasanto": "breathing in short",
            "rassaṃ-vā-passasanto": "breathing out short",
            "sabbakāyapaṭisaṃvedī": "experiencing the whole body",
            "passambhayaṃ-kāyasaṅkhāraṃ": "calming bodily fabrication",
            
            # Ethical expressions
            "pāṇātipātā-veramaṇī": "abstaining from killing living beings",
            "adinnādānā-veramaṇī": "abstaining from taking what is not given",
            "kāmesu-micchācārā-veramaṇī": "abstaining from sexual misconduct",
            "musāvādā-veramaṇī": "abstaining from false speech",
            "surāmeraya-majjapamādaṭṭhānā-veramaṇī": "abstaining from intoxicants",
            "mettāya-cittena": "with a mind of loving-kindness",
            "karuṇāya-cittena": "with a mind of compassion",
            "muditāya-cittena": "with a mind of appreciative joy",
            "upekkhāya-cittena": "with a mind of equanimity",
            "sabbā-disā-pharitvā": "having pervaded all directions",
            "vipulaṃ-mahagataṃ": "abundant, exalted",
            "appamāṇaṃ-averaṃ": "immeasurable, without hostility",
            "abyāpajjhaṃ-cittaṃ": "without ill-will mind",
            "bhāveti": "he develops",
            
            # Canonical phrases
            "evaṃ-me-sutaṃ": "thus have I heard",
            "ekaṃ-samayaṃ": "on one occasion",
            "bhagavā-viharati": "the Blessed One was staying",
            "sāvatthiyaṃ-jetavane": "at Savatthi in Jeta's Grove",
            "anāthapiṇḍikassa-ārāme": "in Anathapindika's monastery",
            "atha-kho": "then",
            "tena-samayena": "at that time",
            "assosi-kho": "he heard",
            "yena-bhagavā-tenupasaṅkami": "he approached the Blessed One",
            "upasaṅkamitvā-bhagavantaṃ-abhivādetvā": "having approached and paid respect to the Blessed One",
            "ekamantaṃ-nisīdi": "he sat to one side",
            "ekamantaṃ-nisinno-kho": "sitting to one side",
            "bhagavantaṃ-etad-avoca": "he said this to the Blessed One",
            "sādhu-bhante": "good, venerable sir",
            "bhāsitaṃ-abhinanditvā": "having delighted in the statement",
            "anumoditvā": "having approved",
            "uṭṭhāyāsanā": "rising from his seat",
            "bhagavantaṃ-abhivādetvā": "having paid respect to the Blessed One",
            "padakkhiṇaṃ-katvā": "having gone around to the right",
            "pakkāmi": "he departed",
            "idaṃ-vatvā": "having said this",
            "sugato-ahosi": "the well-gone one became",
            "idam-avoca-bhagavā": "this said the Blessed One",
            "attamanā-te-bhikkhū": "satisfied, those monks",
            "bhagavato-bhāsitaṃ-abhinanduṃ": "delighted in the Blessed One's words",
            
            # Completion formulas
            "iti-kho-panetaṃ-vuccati": "thus indeed this is called",
            "tasmātiha": "therefore here",
            "tenāha-bhagavā": "therefore the Blessed One said",
            "yaṃ-taṃ-sammā-vadamāno-vadeyya": "one speaking rightly would say",
            "iti-hetaṃ": "thus this",
            "dakkhiṇeyyo": "worthy of offerings",
            "āhuneyyo": "worthy of hospitality",
            "pāhuneyyo": "worthy of gifts",
            "añjalikaraṇīyo": "worthy of reverential salutation",
            "anuttaraṃ-puññakkhettaṃ": "unsurpassed field of merit",
            "lokassa": "for the world",
            
            # Aspirational phrases
            "iminā-puññakammena": "by this meritorious deed",
            "upajjhāyā-guṇaṃ": "may the virtue of teachers",
            "sabbesattānaṃ": "of all beings",
            "hotu": "may there be",
            "sukhitā-hontu": "may they be happy",
            "niddukkha-hontu": "may they be free from suffering",
            "avera-hontu": "may they be free from enmity",
            "abyāpajjā-hontu": "may they be free from ill-will",
            "anīghā-hontu": "may they be free from trouble",
            "sukhī-attānaṃ-pariharantu": "may they look after themselves happily",
            "sabbe-sattā-sadā-hontu": "may all beings always be",
            "averā-sukhajīvino": "free from enmity and living happily",
            "kataṃ-puññaphalaṃ": "the fruit of the merit done",
            "mayhaṃ-sabbe-upakārahontu": "may all be helpful to me",
            "ye-santāne-hinā-sattā": "those beings who are inferior in the stream of existence",
            "te-sabbe-tārayāmyahaṃ": "I shall help them all across",
            
            # Protective formulas
            "jayanto-bodhiyā-mūle": "victorious at the foot of the Bodhi tree",
            "sakyānaṃ-nandivaḍḍhano": "increasing the joy of the Sakyans",
            "evam-ādiguṇa-dharo": "possessing such virtues and so forth",
            "buddho-me-rakkhatu": "may the Buddha protect me",
            "dhammo-me-rakkhatu": "may the Dhamma protect me",
            "saṅgho-me-rakkhatu": "may the Sangha protect me",
            "buddhādhiṭṭhitena": "blessed by the Buddha",
            "dhammādhiṭṭhitena": "blessed by the Dhamma",
            "saṅghādhiṭṭhitena": "blessed by the Sangha",
            "buddharatanena": "by the Buddha-jewel",
            "dhammaratanena": "by the Dhamma-jewel",
            "saṅgharatanena": "by the Sangha-jewel",
            "tiratanena": "by the Triple Gem",
            "sādhu-sādhu-sādhu": "well done! well done! well done!",
        }
    
    def _initialize_liturgical_formulas(self) -> Dict[str, str]:
        """Buddhist liturgical and ceremonial formulas"""
        return {
            # Triple Gem formulas
            "buddha-vandanā": "veneration to the Buddha",
            "dhamma-vandanā": "veneration to the Dhamma",
            "saṅgha-vandanā": "veneration to the Sangha",
            "ratanattaya-vandanā": "veneration to the Triple Gem",
            "buddha-guṇa-gāthā": "verses on Buddha's qualities",
            "dhamma-guṇa-gāthā": "verses on Dhamma's qualities",
            "saṅgha-guṇa-gāthā": "verses on Sangha's qualities",
            
            # Paritta (protective chants)
            "ratana-sutta-paritta": "Ratana Sutta protection",
            "karaṇīya-mettā-sutta-paritta": "Karaniya Metta Sutta protection",
            "khandha-paritta": "aggregate protection",
            "mora-paritta": "peacock protection",
            "vaṭṭa-paritta": "quail protection",
            "dhajagga-paritta": "banner protection",
            "āṭānāṭiya-paritta": "Atanatiya protection",
            "aṅgulimāla-paritta": "Angulimala protection",
            "bojjhaṅga-paritta": "enlightenment factor protection",
            "pubbaṇha-paritta": "morning protection",
            "sāyanha-paritta": "evening protection",
            "rattibhāga-paritta": "night protection",
            "caturārakkhā-paritta": "four protections",
            "pañcārakkhā-paritta": "five protections",
            "sattārakkhā-paritta": "seven protections",
            "navārakkhā-paritta": "nine protections",
            "mahā-paritta": "great protection",
            
            # Blessing formulas
            "bhavatu-sabba-maṅgalaṃ": "may there be all blessings",
            "rakkhantu-sabba-devatā": "may all deities protect",
            "sadā-sotthī-bhavantu-te": "may you always be safe",
            "nidukkho-bhava": "be free from suffering",
            "yathā-icchitaṃ": "as desired",
            "tathā-bhavatu": "so may it be",
            "sukhī-homi": "may I be happy",
            "niddukkho-homi": "may I be free from suffering",
            "avero-homi": "may I be free from enmity",
            "abyāpajjo-homi": "may I be free from ill-will",
            "anīgho-homi": "may I be free from trouble",
            "sukhī-attānaṃ-pariharāmi": "may I look after myself happily",
            "sabba-sattā-sukhī-hontu": "may all beings be happy",
            "sabba-sattā-averā-hontu": "may all beings be free from enmity",
            "sabba-sattā-abyāpajjā-hontu": "may all beings be free from ill-will",
            "sabba-sattā-anīghā-hontu": "may all beings be free from trouble",
            "sabba-sattā-sukhī-attānaṃ-pariharantu": "may all beings look after themselves happily",
            
            # Merit dedication
            "puññaṃ-pasādayāmi": "I dedicate merit",
            "idaṃ-me-puññaṃ": "this merit of mine",
            "āsavakkhayāvahaṃ-hotu": "may it lead to the destruction of taints",
            "idaṃ-me-puññaṃ-nibbānassa-paccayo-hotu": "may this merit of mine be a condition for Nibbana",
            "mama-puññabhāgaṃ": "my share of merit",
            "sabba-sattānaṃ-bhājemi": "I share with all beings",
            "te-sabbe-me-samaṃ": "may they all equally with me",
            "puññabhāgaṃ-labhantu": "receive a share of merit",
            "sādhu-anumodanā": "good appreciation",
            "sādhu-sādhu-anumodāmi": "I appreciate well, well",
            
            # Forgiveness and confession
            "kāyena-vācāya": "by body and speech",
            "manasā-vā": "or by mind",
            "buddhe-kukammaṃ": "wrong action towards the Buddha",
            "pakataṃ-mayā": "done by me",
            "buddho-paṭiggaṇhātu": "may the Buddha accept",
            "accayaṃ-me-bhante": "my transgression, venerable sir",
            "khamatu-me-bhante": "forgive me, venerable sir",
            "bhagavā-khamatu": "may the Blessed One forgive",
            "desetu-me-bhante": "teach me, venerable sir",
            "ovādaṃ-anusiṭṭhiṃ": "advice and instruction",
            "karomase-bhante": "we do, venerable sir",
            
            # Ceremony formulas
            "uposatha-sīla": "Uposatha precepts",
            "aṭṭhaṅga-samannāgataṃ": "endowed with eight factors",
            "imañ-ca-rattiṃ": "this night",
            "imañ-ca-divasaṃ": "this day",
            "sammā-deva": "rightly indeed",
            "ajja-mayā": "today by me",
            "uposathaṃ": "Uposatha",
            "kāretabbaṃ": "should be done",
            "uposathassa": "of Uposatha",
            "pāripūriyā": "for the completion",
            "tisaraṇa-gamanaṃ": "going to the Three Refuges",
            "pañca-sīla-samādānaṃ": "undertaking the Five Precepts",
            "aṭṭha-sīla-samādānaṃ": "undertaking the Eight Precepts",
            "dasa-sīla-samādānaṃ": "undertaking the Ten Precepts",
            
            # Teaching formulas
            "dhamma-desanā": "Dhamma teaching",
            "dhamma-kathā": "Dhamma talk",
            "dhamma-savaṇa": "hearing the Dhamma",
            "suttanta-desanā": "discourse teaching",
            "geyya-desanā": "verse teaching",
            "veyyākaraṇa-desanā": "explanatory teaching",
            "ovāda-anusāsanī": "advice and instruction",
            "dhamma-cakka-pavattana": "turning the wheel of Dhamma",
            "paṭhama-desanā": "first teaching",
            "majjhima-desanā": "middle teaching",
            "pacchima-desanā": "final teaching",
            "sāsana-kicca": "teaching duty",
            "buddha-vacana": "word of the Buddha",
            "dhamma-vinaya": "Dhamma and Discipline",
            
            # Monastic formulas
            "pabbajjā-kamma": "going forth ceremony",
            "upasampadā-kamma": "full ordination ceremony",
            "nissaya-dāna": "giving dependence",
            "nissaya-mutti": "release from dependence",
            "ovāda-pāṭimokkha": "admonition of the Patimokkha",
            "pāṭimokkha-uddesaka": "reciter of the Patimokkha",
            "vinaya-kamma": "disciplinary procedure",
            "saṅgha-kamma": "Sangha procedure",
            "uposatha-kamma": "Uposatha procedure",
            "pavāraṇā-kamma": "Pavarana procedure",
            "kathina-atthāra": "spreading the Kathina",
            "kathina-uddharaṇa": "lifting the Kathina",
            "cīvara-kāla": "robe season",
            "vassa-kāla": "rains season",
            "hemanta-kāla": "cool season",
            "gima-kāla": "hot season",
        }
    
    def _initialize_proper_names(self) -> Dict[str, Dict[str, str]]:
        """Proper names with declension information"""
        return {
            # Buddha's names
            "Buddha": {"meaning": "Awakened One", "gender": "m", "declension": "a_masculine", "type": "title"},
            "Siddhattha": {"meaning": "one whose goal is accomplished", "gender": "m", "declension": "a_masculine", "type": "personal"},
            "Gotama": {"meaning": "best ox", "gender": "m", "declension": "a_masculine", "type": "clan"},
            "Bhagavant": {"meaning": "Blessed One", "gender": "m", "declension": "ant_masculine", "type": "title"},
            "Tathāgata": {"meaning": "Thus-gone One", "gender": "m", "declension": "a_masculine", "type": "title"},
            "Sammāsambuddha": {"meaning": "Perfectly Self-Enlightened One", "gender": "m", "declension": "a_masculine", "type": "title"},
            "Sugata": {"meaning": "Well-gone One", "gender": "m", "declension": "a_masculine", "type": "title"},
            "Lokavidū": {"meaning": "Knower of the World", "gender": "m", "declension": "u_masculine", "type": "title"},
            "Anuttarapurisadammasārathi": {"meaning": "Unsurpassed Leader of Persons to be Tamed", "gender": "m", "declension": "i_masculine", "type": "title"},
            "Satthādevamanussānaṃ": {"meaning": "Teacher of Devas and Humans", "gender": "m", "declension": "ar_masculine", "type": "title"},
            
            # Places
            "Kapilavatthu": {"meaning": "city of Kapila", "gender": "n", "declension": "u_neuter", "type": "city"},
            "Lumbinī": {"meaning": "Lumbini garden", "gender": "f", "declension": "ii_feminine", "type": "place"},
            "Buddhagayā": {"meaning": "Buddha's Gaya", "gender": "f", "declension": "aa_feminine", "type": "place"},
            "Isipatana": {"meaning": "place where sages land", "gender": "n", "declension": "a_neuter", "type": "place"},
            "Migadāya": {"meaning": "deer park", "gender": "m", "declension": "a_masculine", "type": "place"},
            "Bārāṇasī": {"meaning": "Varanasi", "gender": "f", "declension": "ii_feminine", "type": "city"},
            "Sāvatthī": {"meaning": "Savatthi", "gender": "f", "declension": "ii_feminine", "type": "city"},
            "Jetavana": {"meaning": "Jeta's grove", "gender": "n", "declension": "a_neuter", "type": "monastery"},
            "Anāthapiṇḍikassa-ārāma": {"meaning": "Anathapindika's monastery", "gender": "m", "declension": "a_masculine", "type": "monastery"},
            "Pubbārāma": {"meaning": "Eastern monastery", "gender": "m", "declension": "a_masculine", "type": "monastery"},
            "Migāramātupāsāda": {"meaning": "Migara's mother's mansion", "gender": "m", "declension": "a_masculine", "type": "building"},
            "Gijjhakūṭa": {"meaning": "Vulture Peak", "gender": "m", "declension": "a_masculine", "type": "mountain"},
            "Veḷuvana": {"meaning": "Bamboo Grove", "gender": "n", "declension": "a_neuter", "type": "monastery"},
            "Kalandakanivāpa": {"meaning": "Squirrel's feeding place", "gender": "m", "declension": "a_masculine", "type": "place"},
            "Rājagaha": {"meaning": "King's house", "gender": "n", "declension": "a_neuter", "type": "city"},
            "Vesāli": {"meaning": "Vesali", "gender": "f", "declension": "ii_feminine", "type": "city"},
            "Mahāvana": {"meaning": "Great Grove", "gender": "n", "declension": "a_neuter", "type": "place"},
            "Kūṭāgārasālā": {"meaning": "Peaked Hall", "gender": "f", "declension": "aa_feminine", "type": "building"},
            "Kusinārā": {"meaning": "Kusinara", "gender": "f", "declension": "aa_feminine", "type": "city"},
            "Upavattana": {"meaning": "Upavattana", "gender": "n", "declension": "a_neuter", "type": "place"},
            "Sālavana": {"meaning": "Sala Grove", "gender": "n", "declension": "a_neuter", "type": "place"},
            
            # Important disciples
            "Sāriputta": {"meaning": "son of Sari", "gender": "m", "declension": "a_masculine", "type": "monk"},
            "Moggallāna": {"meaning": "descendant of Moggalla", "gender": "m", "declension": "a_masculine", "type": "monk"},
            "Mahākassapa": {"meaning": "Great Kassapa", "gender": "m", "declension": "a_masculine", "type": "monk"},
            "Ānanda": {"meaning": "joy", "gender": "m", "declension": "a_masculine", "type": "monk"},
            "Upāli": {"meaning": "protector", "gender": "m", "declension": "i_masculine", "type": "monk"},
            "Anuruddha": {"meaning": "not obstructed", "gender": "m", "declension": "a_masculine", "type": "monk"},
            "Rāhula": {"meaning": "fetter", "gender": "m", "declension": "a_masculine", "type": "monk"},
            "Devadatta": {"meaning": "given by gods", "gender": "m", "declension": "a_masculine", "type": "monk"},
            "Mahāpajāpatī": {"meaning": "Great Pajapati", "gender": "f", "declension": "ii_feminine", "type": "nun"},
            "Khemā": {"meaning": "security", "gender": "f", "declension": "aa_feminine", "type": "nun"},
            "Uppalavaṇṇā": {"meaning": "lotus-colored", "gender": "f", "declension": "aa_feminine", "type": "nun"},
            "Bhaddakaccānā": {"meaning": "fortunate Kaccana", "gender": "f", "declension": "aa_feminine", "type": "nun"},
            "Paṭācārā": {"meaning": "one with a bowl", "gender": "f", "declension": "aa_feminine", "type": "nun"},
            "Kisāgotamī": {"meaning": "lean Gotami", "gender": "f", "declension": "ii_feminine", "type": "nun"},
            
            # Kings and rulers
            "Bimbisāra": {"meaning": "moon's essence", "gender": "m", "declension": "a_masculine", "type": "king"},
            "Ajātasattu": {"meaning": "enemy before birth", "gender": "m", "declension": "u_masculine", "type": "king"},
            "Pasenadi": {"meaning": "Pasenadi", "gender": "m", "declension": "i_masculine", "type": "king"},
            "Suddhodana": {"meaning": "pure rice", "gender": "m", "declension": "a_masculine", "type": "king"},
            "Mahāmāyā": {"meaning": "Great Maya", "gender": "f", "declension": "aa_feminine", "type": "queen"},
            "Yasodharā": {"meaning": "bearer of fame", "gender": "f", "declension": "aa_feminine", "type": "princess"},
            
            # Celestial beings
            "Sakka": {"meaning": "able one", "gender": "m", "declension": "a_masculine", "type": "deva"},
            "Indra": {"meaning": "lord", "gender": "m", "declension": "a_masculine", "type": "deva"},
            "Brahmā": {"meaning": "sacred utterance", "gender": "m", "declension": "a_masculine", "type": "brahma"},
            "Sahampati": {"meaning": "lord of the retinue", "gender": "m", "declension": "i_masculine", "type": "brahma"},
            "Māra": {"meaning": "death", "gender": "m", "declension": "a_masculine", "type": "mara"},
            
            # Other important figures
            "Yasa": {"meaning": "fame", "gender": "m", "declension": "a_masculine", "type": "lay_disciple"},
            "Anāthapiṇḍika": {"meaning": "feeder of the destitute", "gender": "m", "declension": "a_masculine", "type": "lay_disciple"},
            "Visākhā": {"meaning": "Visakha", "gender": "f", "declension": "aa_feminine", "type": "lay_disciple"},
            "Migāramātā": {"meaning": "Migara's mother", "gender": "f", "declension": "ar_feminine", "type": "lay_disciple"},
            "Jīvaka": {"meaning": "life", "gender": "m", "declension": "a_masculine", "type": "physician"},
            "Ambapāli": {"meaning": "mango keeper", "gender": "f", "declension": "ii_feminine", "type": "courtesan"},
            "Aṅgulimāla": {"meaning": "finger garland", "gender": "m", "declension": "a_masculine", "type": "former_bandit"},
            "Pukkusa": {"meaning": "Pukkusa", "gender": "m", "declension": "a_masculine", "type": "malla"},
            "Cunda": {"meaning": "Cunda", "gender": "m", "declension": "a_masculine", "type": "smith"},
        }
    
    def _initialize_complete_numerals(self) -> Dict[str, Dict[str, str]]:
        """Complete numeral system with all variants"""
        return {
            # Cardinals
            "eka": {"type": "cardinal", "value": 1, "meaning": "one", "gender": "all"},
            "dvi": {"type": "cardinal", "value": 2, "meaning": "two", "gender": "all"},
            "duve": {"type": "cardinal", "value": 2, "meaning": "two (feminine)", "gender": "f"},
            "ti": {"type": "cardinal", "value": 3, "meaning": "three", "gender": "all"},
            "tisso": {"type": "cardinal", "value": 3, "meaning": "three (feminine)", "gender": "f"},
            "catu": {"type": "cardinal", "value": 4, "meaning": "four", "gender": "all"},
            "catasso": {"type": "cardinal", "value": 4, "meaning": "four (feminine)", "gender": "f"},
            "pañca": {"type": "cardinal", "value": 5, "meaning": "five", "gender": "all"},
            "cha": {"type": "cardinal", "value": 6, "meaning": "six", "gender": "all"},
            "satta": {"type": "cardinal", "value": 7, "meaning": "seven", "gender": "all"},
            "aṭṭha": {"type": "cardinal", "value": 8, "meaning": "eight", "gender": "all"},
            "nava": {"type": "cardinal", "value": 9, "meaning": "nine", "gender": "all"},
            "dasa": {"type": "cardinal", "value": 10, "meaning": "ten", "gender": "all"},
            "ekādasa": {"type": "cardinal", "value": 11, "meaning": "eleven", "gender": "all"},
            "dvādasa": {"type": "cardinal", "value": 12, "meaning": "twelve", "gender": "all"},
            "terasa": {"type": "cardinal", "value": 13, "meaning": "thirteen", "gender": "all"},
            "cuddasa": {"type": "cardinal", "value": 14, "meaning": "fourteen", "gender": "all"},
            "paṇṇarasa": {"type": "cardinal", "value": 15, "meaning": "fifteen", "gender": "all"},
            "soḷasa": {"type": "cardinal", "value": 16, "meaning": "sixteen", "gender": "all"},
            "sattarasa": {"type": "cardinal", "value": 17, "meaning": "seventeen", "gender": "all"},
            "aṭṭhārasa": {"type": "cardinal", "value": 18, "meaning": "eighteen", "gender": "all"},
            "ekūnavīsati": {"type": "cardinal", "value": 19, "meaning": "nineteen", "gender": "all"},
            "vīsati": {"type": "cardinal", "value": 20, "meaning": "twenty", "gender": "all"},
            "ekatīsa": {"type": "cardinal", "value": 21, "meaning": "twenty-one", "gender": "all"},
            "dvātīsa": {"type": "cardinal", "value": 22, "meaning": "twenty-two", "gender": "all"},
            "tiṃsati": {"type": "cardinal", "value": 30, "meaning": "thirty", "gender": "all"},
            "cattālīsa": {"type": "cardinal", "value": 40, "meaning": "forty", "gender": "all"},
            "paññāsa": {"type": "cardinal", "value": 50, "meaning": "fifty", "gender": "all"},
            "saṭṭhi": {"type": "cardinal", "value": 60, "meaning": "sixty", "gender": "all"},
            "sattati": {"type": "cardinal", "value": 70, "meaning": "seventy", "gender": "all"},
            "asīti": {"type": "cardinal", "value": 80, "meaning": "eighty", "gender": "all"},
            "navuti": {"type": "cardinal", "value": 90, "meaning": "ninety", "gender": "all"},
            "sata": {"type": "cardinal", "value": 100, "meaning": "hundred", "gender": "all"},
            "ekasata": {"type": "cardinal", "value": 101, "meaning": "one hundred one", "gender": "all"},
            "dvisata": {"type": "cardinal", "value": 200, "meaning": "two hundred", "gender": "all"},
            "tisata": {"type": "cardinal", "value": 300, "meaning": "three hundred", "gender": "all"},
            "catusata": {"type": "cardinal", "value": 400, "meaning": "four hundred", "gender": "all"},
            "pañcasata": {"type": "cardinal", "value": 500, "meaning": "five hundred", "gender": "all"},
            "chasata": {"type": "cardinal", "value": 600, "meaning": "six hundred", "gender": "all"},
            "sattasata": {"type": "cardinal", "value": 700, "meaning": "seven hundred", "gender": "all"},
            "aṭṭhasata": {"type": "cardinal", "value": 800, "meaning": "eight hundred", "gender": "all"},
            "navasata": {"type": "cardinal", "value": 900, "meaning": "nine hundred", "gender": "all"},
            "sahassa": {"type": "cardinal", "value": 1000, "meaning": "thousand", "gender": "all"},
            "dasasahassa": {"type": "cardinal", "value": 10000, "meaning": "ten thousand", "gender": "all"},
            "satasahassa": {"type": "cardinal", "value": 100000, "meaning": "one hundred thousand", "gender": "all"},
            "lakkha": {"type": "cardinal", "value": 100000, "meaning": "lakh", "gender": "all"},
            "dasalakkha": {"type": "cardinal", "value": 1000000, "meaning": "ten lakh", "gender": "all"},
            "koṭi": {"type": "cardinal", "value": 10000000, "meaning": "crore", "gender": "all"},
            "aṭṭha-koṭi": {"type": "cardinal", "value": 80000000, "meaning": "eight crores", "gender": "all"},
            "nahuta": {"type": "cardinal", "value": 1000000000, "meaning": "billion", "gender": "all"},
            "ninnahuta": {"type": "cardinal", "value": 10000000000, "meaning": "ten billion", "gender": "all"},
            "akkhobhinī": {"type": "cardinal", "value": 100000000000, "meaning": "hundred billion", "gender": "all"},
            "bindu": {"type": "cardinal", "value": 1000000000000, "meaning": "trillion", "gender": "all"},
            "abbuda": {"type": "cardinal", "value": 10000000000000, "meaning": "ten trillion", "gender": "all"},
            "nirabbuda": {"type": "cardinal", "value": 100000000000000, "meaning": "hundred trillion", "gender": "all"},
            "ahaha": {"type": "cardinal", "value": 1000000000000000, "meaning": "quadrillion", "gender": "all"},
            "ababa": {"type": "cardinal", "value": 10000000000000000, "meaning": "ten quadrillion", "gender": "all"},
            "aṭaṭa": {"type": "cardinal", "value": 100000000000000000, "meaning": "hundred quadrillion", "gender": "all"},
            "sogandhika": {"type": "cardinal", "value": 1000000000000000000, "meaning": "quintillion", "gender": "all"},
            "uppala": {"type": "cardinal", "value": 10000000000000000000, "meaning": "ten quintillion", "gender": "all"},
            "kumuda": {"type": "cardinal", "value": 100000000000000000000, "meaning": "hundred quintillion", "gender": "all"},
            "puṇḍarīka": {"type": "cardinal", "value": 1000000000000000000000, "meaning": "sextillion", "gender": "all"},
            "paduma": {"type": "cardinal", "value": 10000000000000000000000, "meaning": "ten sextillion", "gender": "all"},
            "kathana": {"type": "cardinal", "value": 100000000000000000000000, "meaning": "hundred sextillion", "gender": "all"},
            "mahākathana": {"type": "cardinal", "value": 1000000000000000000000000, "meaning": "septillion", "gender": "all"},
            "asaṅkheyya": {"type": "cardinal", "value": "∞", "meaning": "incalculable", "gender": "all"},
            
            # Ordinals
            "paṭhama": {"type": "ordinal", "value": 1, "meaning": "first", "gender": "all"},
            "dutiya": {"type": "ordinal", "value": 2, "meaning": "second", "gender": "all"},
            "tatiya": {"type": "ordinal", "value": 3, "meaning": "third", "gender": "all"},
            "catuttha": {"type": "ordinal", "value": 4, "meaning": "fourth", "gender": "all"},
            "pañcama": {"type": "ordinal", "value": 5, "meaning": "fifth", "gender": "all"},
            "chaṭṭha": {"type": "ordinal", "value": 6, "meaning": "sixth", "gender": "all"},
            "sattama": {"type": "ordinal", "value": 7, "meaning": "seventh", "gender": "all"},
            "aṭṭhama": {"type": "ordinal", "value": 8, "meaning": "eighth", "gender": "all"},
            "navama": {"type": "ordinal", "value": 9, "meaning": "ninth", "gender": "all"},
            "dasama": {"type": "ordinal", "value": 10, "meaning": "tenth", "gender": "all"},
            "ekādasama": {"type": "ordinal", "value": 11, "meaning": "eleventh", "gender": "all"},
            "dvādasama": {"type": "ordinal", "value": 12, "meaning": "twelfth", "gender": "all"},
            "vīsatima": {"type": "ordinal", "value": 20, "meaning": "twentieth", "gender": "all"},
            "tiṃsatima": {"type": "ordinal", "value": 30, "meaning": "thirtieth", "gender": "all"},
            "satama": {"type": "ordinal", "value": 100, "meaning": "hundredth", "gender": "all"},
            "sahassama": {"type": "ordinal", "value": 1000, "meaning": "thousandth", "gender": "all"},
            "pacchima": {"type": "ordinal", "value": "last", "meaning": "last, final", "gender": "all"},
            "antima": {"type": "ordinal", "value": "last", "meaning": "last, final", "gender": "all"},
            
            # Multiplicatives
            "ekaka": {"type": "multiplicative", "value": 1, "meaning": "single, solitary", "gender": "all"},
            "dvika": {"type": "multiplicative", "value": 2, "meaning": "double, pair", "gender": "all"},
            "tika": {"type": "multiplicative", "value": 3, "meaning": "triple, triad", "gender": "all"},
            "catukka": {"type": "multiplicative", "value": 4, "meaning": "quadruple, tetrad", "gender": "all"},
            "pañcaka": {"type": "multiplicative", "value": 5, "meaning": "fivefold, pentad", "gender": "all"},
            "chakka": {"type": "multiplicative", "value": 6, "meaning": "sixfold, hexad", "gender": "all"},
            "sattaka": {"type": "multiplicative", "value": 7, "meaning": "sevenfold", "gender": "all"},
            "aṭṭhaka": {"type": "multiplicative", "value": 8, "meaning": "eightfold", "gender": "all"},
            "navaka": {"type": "multiplicative", "value": 9, "meaning": "ninefold", "gender": "all"},
            "dasaka": {"type": "multiplicative", "value": 10, "meaning": "tenfold", "gender": "all"},
            "sataka": {"type": "multiplicative", "value": 100, "meaning": "hundredfold", "gender": "all"},
            "sahassaka": {"type": "multiplicative", "value": 1000, "meaning": "thousandfold", "gender": "all"},
            
            # Distributives
            "ekeka": {"type": "distributive", "value": 1, "meaning": "one by one", "gender": "all"},
            "dvīdvā": {"type": "distributive", "value": 2, "meaning": "two by two", "gender": "all"},
            "tayo-tayo": {"type": "distributive", "value": 3, "meaning": "three by three", "gender": "all"},
            "cattāro-cattāro": {"type": "distributive", "value": 4, "meaning": "four by four", "gender": "all"},
            "pañca-pañca": {"type": "distributive", "value": 5, "meaning": "five by five", "gender": "all"},
            "cha-cha": {"type": "distributive", "value": 6, "meaning": "six by six", "gender": "all"},
            "satta-satta": {"type": "distributive", "value": 7, "meaning": "seven by seven", "gender": "all"},
            "aṭṭha-aṭṭha": {"type": "distributive", "value": 8, "meaning": "eight by eight", "gender": "all"},
            "nava-nava": {"type": "distributive", "value": 9, "meaning": "nine by nine", "gender": "all"},
            "dasa-dasa": {"type": "distributive", "value": 10, "meaning": "ten by ten", "gender": "all"},
            
            # Fractionals
            "aḍḍha": {"type": "fractional", "value": 0.5, "meaning": "half", "gender": "all"},
            "pāda": {"type": "fractional", "value": 0.25, "meaning": "quarter", "gender": "all"},
            "tiya": {"type": "fractional", "value": 0.33, "meaning": "third", "gender": "all"},
            "catutthabhāga": {"type": "fractional", "value": 0.25, "meaning": "fourth part", "gender": "all"},
            "pañcamabhāga": {"type": "fractional", "value": 0.2, "meaning": "fifth part", "gender": "all"},
            "chaṭṭhabhāga": {"type": "fractional", "value": 0.17, "meaning": "sixth part", "gender": "all"},
            "sattamabhāga": {"type": "fractional", "value": 0.14, "meaning": "seventh part", "gender": "all"},
            "aṭṭhamabhāga": {"type": "fractional", "value": 0.125, "meaning": "eighth part", "gender": "all"},
            "navamabhāga": {"type": "fractional", "value": 0.11, "meaning": "ninth part", "gender": "all"},
            "dasamabhāga": {"type": "fractional", "value": 0.1, "meaning": "tenth part", "gender": "all"},
            "vīsatimabhāga": {"type": "fractional", "value": 0.05, "meaning": "twentieth part", "gender": "all"},
            "satamabhāga": {"type": "fractional", "value": 0.01, "meaning": "hundredth part", "gender": "all"},
            
            # Temporal numbers
            "sakiṃ": {"type": "temporal", "value": 1, "meaning": "once", "gender": "all"},
            "duviṃ": {"type": "temporal", "value": 2, "meaning": "twice", "gender": "all"},
            "tiṃ": {"type": "temporal", "value": 3, "meaning": "thrice", "gender": "all"},
            "catuṃ": {"type": "temporal", "value": 4, "meaning": "four times", "gender": "all"},
            "pañcakkhattaṃ": {"type": "temporal", "value": 5, "meaning": "five times", "gender": "all"},
            "chakkhattaṃ": {"type": "temporal", "value": 6, "meaning": "six times", "gender": "all"},
            "sattakkhattaṃ": {"type": "temporal", "value": 7, "meaning": "seven times", "gender": "all"},
            "aṭṭhakkhattaṃ": {"type": "temporal", "value": 8, "meaning": "eight times", "gender": "all"},
            "navakkhattaṃ": {"type": "temporal", "value": 9, "meaning": "nine times", "gender": "all"},
            "dasakkhattaṃ": {"type": "temporal", "value": 10, "meaning": "ten times", "gender": "all"},
            "satakkhattaṃ": {"type": "temporal", "value": 100, "meaning": "hundred times", "gender": "all"},
            "sahassakkhattaṃ": {"type": "temporal", "value": 1000, "meaning": "thousand times", "gender": "all"},
            "koṭisatasakkhattaṃ": {"type": "temporal", "value": 1000000000, "meaning": "billion times", "gender": "all"},
            "asaṅkhyeyyakkhattaṃ": {"type": "temporal", "value": "∞", "meaning": "incalculable times", "gender": "all"},
            
            # Measurement numbers
            "aṅgula": {"type": "measurement", "value": "finger", "meaning": "finger-width", "gender": "all"},
            "vitthāra": {"type": "measurement", "value": "span", "meaning": "span", "gender": "all"},
            "hattha": {"type": "measurement", "value": "cubit", "meaning": "cubit", "gender": "all"},
            "kamma": {"type": "measurement", "value": "step", "meaning": "pace", "gender": "all"},
            "usabha": {"type": "measurement", "value": "fathom", "meaning": "fathom", "gender": "all"},
            "dhanu": {"type": "measurement", "value": "bow", "meaning": "bow-length", "gender": "all"},
            "nāḷī": {"type": "measurement", "value": "measure", "meaning": "measure", "gender": "all"},
            "āḷhaka": {"type": "measurement", "value": "bushel", "meaning": "bushel", "gender": "all"},
            "doṇa": {"type": "measurement", "value": "measure", "meaning": "measure", "gender": "all"},
            "khāri": {"type": "measurement", "value": "cartload", "meaning": "cartload", "gender": "all"},
            "vāha": {"type": "measurement", "value": "cartload", "meaning": "cartload", "gender": "all"},
        }
    
    def _initialize_extended_onomatopoeia(self) -> Dict[str, str]:
        """Extended onomatopoeia and sound symbolism"""
        return {
            # Sound of bells and music
            "kiṅkiṇi": "tinkling of small bells",
            "jhañjhañ": "clanging of large bells",
            "ṭhañṭhaṇ": "beating of drums",
            "diṅdiṅ": "ringing sound",
            "siṅsiṅ": "whistling sound",
            "ninnanaṃ": "humming sound",
            "sarasara": "rustling, soft sound",
            "sirisiri": "sizzling sound",
            
            # Animal sounds
            "ambā": "bleating of goats",
            "bhaṃbhaṃ": "lowing of cattle",
            "hiṅhiṅ": "neighing of horses",
            "kikira": "crowing of cocks",
            "kukkū": "cooing of doves",
            "kākakā": "cawing of crows",
            "sikhī": "crying of peacocks",
            "bhambhara": "buzzing of bees",
            "jhiṅjhiṅ": "chirping of insects",
            "siṃsimāya": "roaring of lions",
            
            # Natural sounds
            "gaḍagaḍa": "rumbling of thunder",
            "garugaru": "thundering sound",
            "jalajala": "splashing of water",
            "calacala": "flowing of water",
            "sāsā": "whistling of wind",
            "sussu": "hissing sound",
            "phussa": "whispering sound",
            "matmatāya": "crackling of fire",
            "cicciṭa": "crackling sound",
            "dhamdhamāya": "throbbing sound",
            
            # Human sounds
            "kila": "shouting",
            "kilakila": "laughing heartily",
            "rudrudrāya": "weeping",
            "rodarodā": "crying",
            "assa": "sighing",
            "hāhā": "laughing",
            "huhuṅkāra": "grunting",
            "khipakkhipa": "chattering",
            "bhabbhabba": "babbling",
            "phussa": "whispering",
            
            # Movement sounds
            "khalakhala": "clattering",
            "ṭhaṭhaṭha": "pattering",
            "dhapphadhappa": "flapping",
            "papphalaphala": "flopping",
            "cuṅcuṅ": "jingling",
            "phutphut": "puffing",
            "dhutadhuta": "shaking",
            "pallallapa": "trembling",
            
            # Breaking and impact sounds
            "bhañjabhañja": "breaking",
            "khaṇḍakhaṇḍa": "shattering",
            "phalaphalā": "splitting",
            "ṭhapphaṭhappa": "slapping",
            "dhapphadhappa": "beating",
            "phussaphassa": "touching lightly",
            "ghaṭṭaghaṭṭa": "rubbing",
            "khajjakhajja": "gnawing",
            
            # Liquid sounds
            "bubbuḷa": "bubbling",
            "udakulī": "gurgling",
            "plāplā": "splashing lightly",
            "dhārādhārā": "streaming",
            "picchilapicchila": "dripping",
            "tapphatappa": "dripping quickly",
            "visavisā": "oozing",
            "sandasanda": "flowing",
            
            # Mental states (sound symbolism)
            "tuṅhī": "silent, speechless",
            "nissadda": "soundless",
            "nibbijaṅkāra": "without murmur",
            "appasadda": "with little sound",
            "uccāsadda": "loud, noisy",
            "mahāsadda": "very loud",
            "vitthārasadda": "extended sound",
            "vikatthanā": "boasting",
            
            # Ritual sounds
            "svāhā": "ritual exclamation",
            "sādhu": "expression of approval",
            "aho": "expression of wonder",
            "handa": "come on!",
            "khaṇḍa": "breaking sound in ritual",
            "maṅgala": "auspicious sound",
            "jayā": "victory cry",
            "jīva": "long live!",
            
            # Emotional expressions
            "ucchaleti": "jumps with joy",
            "kampeti": "trembles",
            "vedhati": "thrills",
            "pulakita": "thrilled (hair standing)",
            "lomahattho": "hair-raising",
            "sārambha": "enthusiastic sound",
            "utsāha": "energetic expression",
            "vismaya": "wondering sound",
            
            # Temporal sound patterns
            "ṭhapetvā": "placed sound",
            "ugghāṭana": "opening sound",
            "pihana": "closing sound",
            "vivaraṇa": "uncovering sound",
            "chādana": "covering sound",
            "sampadāna": "completion sound",
            "ārabbhana": "beginning sound",
            "niṭṭhāpana": "finishing sound",
        }
    
    def _initialize_synonyms_antonyms(self) -> Dict[str, Dict[str, List[str]]]:
        """Comprehensive synonyms and antonyms"""
        return {
            "synonyms": {
                "buddha": ["tathāgata", "sugata", "bhagavā", "sammāsambuddha", "jina", "dasabala"],
                "dhamma": ["desanā", "sāsana", "vacana", "ovāda", "anusāsanī", "naya"],
                "saṅgha": ["gaṇa", "pūga", "nikāya", "parisa", "samūha", "maṇḍala"],
                "nibbāna": ["amata", "moksa", "vimutti", "viveka", "santa", "siva"],
                "dukkha": ["domanassa", "dukkhitā", "ābādha", "vighāta", "upaddava", "vipatti"],
                "sukha": ["somanassa", "rati", "mudā", "pāmojja", "tuṭṭhi", "santuṭṭhi"],
                "citta": ["mano", "hadaya", "ura", "ceto", "manas", "viññāṇa"],
                "paññā": ["ñāṇa", "vijjā", "prajñā", "buddhi", "medhā", "pāṭava"],
                "mettā": ["mudā", "sneha", "pemā", "dayā", "karuṇā", "anukampā"],
                "sīla": ["ācāra", "caraṇa", "caritta", "vrata", "niyama", "saṃvara"],
                "samādhi": ["samatha", "jhāna", "ekaggatā", "cittassa-ekaggitā", "yoga", "upasama"],
                "magga": "patha", "paṭipadā", "naya", "gati", "añjasa", "ujuka"],
                "phala": ["vipāka", "attha", "ānisaṃsa", "paccupaṭṭhāna", "lābha", "sampatti"],
                "kamma": ["kiriyā", "karaṇa", "ceṭṭā", "payoga", "vāyāma", "ussāha"],
            },
            "antonyms": {
                "sukha": ["dukkha", "domanassa", "dukkhitā", "ābādha", "vighāta"],
                "kusala": ["akusala", "pāpa", "kamma", "duccarita", "aparāddha"],
                "ñāṇa": ["avijjā", "aññāṇa", "moha", "sammūḷha", "andha"],
                "sīla": ["dussīla", "duccarita", "micchācāra", "aparāddha", "āpatti"],
                "santo": ["asanto", "calita", "uddha", "vikkhitta", "vighāta"],
                "kusalā": ["akusalā", "aṭhī", "nipuṇā", "paṇḍitā", "medhāvī"],
                "dāna": ["macchariya", "kadariya", "thīna", "kasāva", "matsarya"],
                "mettā": ["dosa", "vera", "byāpāda", "paṭigha", "kodha"],
                "sammā": ["micchā", "viparīta", "vipallāsa", "vipanna", "parāmuttha"],
                "āraddha": ["kusīta", "alasa", "anussuka", "anuṭṭhita", "pamatta"],
                "sata": ["pamatta", "muṭṭhasati", "asampajāna", "amanasikāra", "pamāda"],
                "ekagga": ["vikkhitta", "vūpasanta", "luddha", "parāmuttha", "visaṃyutta"],
            }
        }
    
    def _initialize_etymology_database(self) -> Dict[str, Dict[str, str]]:
        """Etymology and word formation information"""
        return {
            "buddha": {
                "root": "√budh",
                "meaning": "wake up, understand",
                "formation": "past_participle",
                "cognates": ["Sanskrit: buddha", "Hindi: buddh"],
                "development": "Vedic √budh > Pali buddha"
            },
            "dhamma": {
                "root": "√dhar",
                "meaning": "hold, bear, support",
                "formation": "action_noun",
                "cognates": ["Sanskrit: dharma", "Hindi: dharm"],
                "development": "Vedic dharma > Pali dhamma"
            },
            "saṅgha": {
                "root": "√saṃ-gam",
                "meaning": "come together",
                "formation": "collective_noun",
                "cognates": ["Sanskrit: saṅgha", "Hindi: sangh"],
                "development": "Vedic saṅgha > Pali saṅgha"
            },
            "nibbāna": {
                "root": "√nir-vā",
                "meaning": "blow out, extinguish",
                "formation": "past_participle",
                "cognates": ["Sanskrit: nirvāṇa", "Hindi: nirvan"],
                "development": "Vedic nirvāṇa > Pali nibbāna"
            },
            "kamma": {
                "root": "√kar",
                "meaning": "do, make",
                "formation": "action_noun",
                "cognates": ["Sanskrit: karma", "Hindi: karm"],
                "development": "Vedic karma > Pali kamma"
            },
        }
    
    def _initialize_usage_examples(self) -> Dict[str, List[str]]:
        """Usage examples from canonical texts"""
        return {
            "buddha": [
                "Buddho bhagavā arahaṃ sammāsambuddho",
                "Namo tassa bhagavato arahato sammāsambuddhassa",
                "Buddhaṃ saraṇaṃ gacchāmi"
            ],
            "dhamma": [
                "Svākkhāto bhagavatā dhammo",
                "Dhammaṃ saraṇaṃ gacchāmi",
                "Dhammacakkappavattana"
            ],
            "saṅgha": [
                "Supaṭipanno bhagavato sāvakasaṅgho",
                "Saṅghaṃ saraṇaṃ gacchāmi",
                "Saṅghe buddhaputtesu"
            ],
        }
    
    def _initialize_metrical_variants(self) -> Dict[str, List[str]]:
        """Alternative forms for metrical purposes"""
        return {
            "nibbāna": ["nibbāṇa", "nibbāṇaṃ", "nibbuti"],
            "buddha": ["buddho", "buddhassa", "budhassa"],
            "dhamma": ["dhammo", "dhammassa", "dhāma"],
            "paññā": ["paññaṃ", "paññāya", "pañño"],
            "citta": ["cittaṃ", "ceto", "cetaṃ"],
            "rūpa": ["rūpaṃ", "rūvo", "rūvassa"],
        }
    
    def _initialize_register_variations(self) -> Dict[str, Dict[str, str]]:
        """Register variations (formal/informal/poetic/etc.)"""
        return {
            "formal": {
                "buddha": "bhagavā sammāsambuddho",
                "monk": "mahāthera bhaddanta",
                "eat": "bhuñjati āhāraṃ",
                "go": "gacchati yena",
                "speak": "bhāsati vacanaṃ"
            },
            "informal": {
                "buddha": "buddha",
                "monk": "bhikkhu",
                "eat": "khādati",
                "go": "gacchati",
                "speak": "vadati"
            },
            "poetic": {
                "buddha": "jina dasabala",
                "monk": "bhikkhusaṅgha",
                "eat": "bhuñjanta āhāra",
                "go": "yāyanta magga",
                "speak": "bhāsamāna dhamma"
            },
            "archaic": {
                "buddha": "tathāgata sugata",
                "monk": "samaṇa brāhmaṇa",
                "eat": "bhuñjamāna",
                "go": "gacchamāna",
                "speak": "vadamāna"
            }
        }
    
    def _initialize_historical_layers(self) -> Dict[str, Dict[str, str]]:
        """Historical development layers"""
        return {
            "early_pali": {
                "buddha": "buddha",
                "dhamma": "dhamma", 
                "meditation": "jhāna",
                "wisdom": "paññā"
            },
            "middle_pali": {
                "buddha": "bhagavā",
                "dhamma": "sāsana",
                "meditation": "samādhi",
                "wisdom": "ñāṇa"
            },
            "late_pali": {
                "buddha": "sammāsambuddha",
                "dhamma": "buddhavacana",
                "meditation": "bhāvanā",
                "wisdom": "vijjā"
            }
        }
    
    def _initialize_semantic_networks(self) -> Dict[str, Dict[str, List[str]]]:
        """Semantic relationship networks"""
        return {
            "enlightenment": {
                "core": ["buddha", "bodhi", "nibbāna", "vimutti"],
                "path": ["magga", "paṭipadā", "sīla", "samādhi", "paññā"],
                "obstacles": ["kilesa", "āsava", "saṃyojana", "nīvaraṇa"],
                "qualities": ["karuṇā", "mettā", "muditā", "upekkhā"]
            },
            "meditation": {
                "practices": ["satipaṭṭhāna", "ānāpānasati", "jhāna", "vipassanā"],
                "states": ["samādhi", "ekaggatā", "passaddhi", "sukha"],
                "objects": ["kasiṇa", "ānāpāna", "kāyagatāsati", "mettā"],
                "stages": ["vitakka", "vicāra", "pīti", "sukha", "ekaggatā"]
            }
        }
    
    def _initialize_canonical_citations(self) -> Dict[str, List[str]]:
        """Canonical text citations for words"""
        return {
            "buddha": ["DN 14", "MN 26", "SN 56.11", "Dhp 183-185"],
            "dhamma": ["DN 16", "MN 141", "SN 22.85", "Dhp 1-2"],
            "saṅgha": ["DN 16", "MN 118", "AN 4.4", "Dhp 194-196"],
            "nibbāna": ["SN 43.1-44", "Ud 8.1-4", "It 37-43"],
            "satipaṭṭhāna": ["DN 22", "MN 10", "SN 47.1-104"],
        }

# ============ ULTIMATE COMPOUND SEMANTIC COMPOSITOR ============

class UltimateCompoundSemanticCompositor(CompoundSemanticCompositor):
    """Ultimate compound generator with unlimited capacity"""
    
    def __init__(self, kb):
        super().__init__(kb)
        
        # Enhanced patterns for massive generation
        self.massive_generation_patterns = self._initialize_massive_patterns()
        self.systematic_combinations = self._initialize_systematic_combinations()
        
    def _initialize_massive_patterns(self):
        """Patterns for massive systematic generation"""
        return {
            "religious_systematic": {
                "buddha_compounds": ["buddha+X", "X+buddha", "buddha+X+Y"],
                "dhamma_compounds": ["dhamma+X", "X+dhamma", "dhamma+X+Y"],
                "saṅgha_compounds": ["saṅgha+X", "X+saṅgha", "saṅgha+X+Y"],
                "tiratana_compounds": ["buddha+dhamma+X", "dhamma+saṅgha+X", "buddha+saṅgha+X"]
            },
            "philosophical_systematic": {
                "truth_compounds": ["sacca+X", "X+sacca", "ariya+sacca+X"],
                "path_compounds": ["magga+X", "X+magga", "aṭṭhaṅgika+magga+X"],
                "liberation_compounds": ["vimutti+X", "X+vimutti", "cetaso+vimutti+X"],
                "wisdom_compounds": ["paññā+X", "X+paññā", "sammā+paññā+X"]
            },
            "meditation_systematic": {
                "jhana_compounds": ["jhāna+X", "X+jhāna", "paṭhama+jhāna+X"],
                "samadhi_compounds": ["samādhi+X", "X+samādhi", "samma+samādhi+X"],
                "sati_compounds": ["sati+X", "X+sati", "samma+sati+X"],
                "bhavana_compounds": ["bhāvanā+X", "X+bhāvanā", "citta+bhāvanā+X"]
            }
        }
    
    def _initialize_systematic_combinations(self):
        """All possible systematic combinations"""
        return {
            "adjective_noun": "all_adjectives × all_nouns",
            "noun_noun": "all_nouns × all_nouns",
            "number_noun": "all_numbers × all_countable_nouns",
            "prefix_word": "all_prefixes × all_suitable_words",
            "quality_entity": "all_qualities × all_entities",
            "action_object": "all_actions × all_objects",
            "temporal_noun": "all_temporal × all_nouns",
            "spatial_noun": "all_spatial × all_nouns"
        }
    
    def generate_unlimited_compounds(self, semantic_fields, max_total=100000):
        """Generate unlimited compounds systematically"""
        compounds = {}
        
        print("   📝 Phase 1: Basic systematic combinations...")
        basic_compounds = self._generate_all_basic_combinations(semantic_fields, max_total // 4)
        compounds.update(basic_compounds)
        
        print("   📝 Phase 2: Religious/philosophical compounds...")
        religious_compounds = self._generate_religious_philosophical_compounds(semantic_fields, max_total // 4)
        compounds.update(religious_compounds)
        
        print("   📝 Phase 3: Technical/specialized compounds...")
        technical_compounds = self._generate_technical_specialized_compounds(semantic_fields, max_total // 4)
        compounds.update(technical_compounds)
        
        print("   📝 Phase 4: Multi-level recursive compounds...")
        recursive_compounds = self._generate_multi_level_recursive_compounds(compounds, max_total // 4)
        compounds.update(recursive_compounds)
        
        return compounds
    
    def _generate_all_basic_combinations(self, semantic_fields, max_count):
        """Generate ALL basic two-word combinations"""
        compounds = {}
        count = 0
        
        # Get all words by category
        all_words = []
        for field, words in semantic_fields.items():
            all_words.extend(words)
        
        # Remove duplicates
        all_words = list(set(all_words))
        
        # Generate all meaningful combinations
        for i, word1 in enumerate(all_words):
            if count >= max_count:
                break
                
            for j, word2 in enumerate(all_words):
                if i == j or count >= max_count:
                    continue
                
                # Check if combination is meaningful
                if self._is_meaningful_combination(word1, word2):
                    # Apply sandhi
                    compound = self._apply_compound_sandhi([word1, word2])
                    
                    if (compound not in compounds and 
                        compound not in self.generated_compounds):
                        
                        # Determine compound type
                        compound_type = self._determine_compound_type(word1, word2)
                        
                        # Generate meaning
                        meaning = self.compose_meaning([word1, word2], compound_type)
                        
                        compounds[compound] = {
                            "components": [word1, word2],
                            "type": compound_type,
                            "meaning": meaning,
                            "frequency": self._calculate_combination_frequency(word1, word2)
                        }
                        
                        self.generated_compounds.add(compound)
                        count += 1
        
        return compounds
    
    def _generate_religious_philosophical_compounds(self, semantic_fields, max_count):
        """Generate all religious and philosophical compounds"""
        compounds = {}
        count = 0
        
        # Core religious terms
        religious_cores = ["buddha", "dhamma", "saṅgha", "nibbāna", "kamma", "sīla", "samādhi", "paññā"]
        philosophical_cores = ["sacca", "magga", "phala", "vimutti", "bodhi", "ñāṇa", "karuṇā", "mettā"]
        
        # All other suitable words
        all_others = []
        for field, words in semantic_fields.items():
            if field not in ["particles", "prefixes"]:
                all_others.extend(words)
        
        all_others = list(set(all_others))
        
        # Generate religious compounds
        for core in religious_cores + philosophical_cores:
            if count >= max_count:
                break
                
            for other in all_others:
                if count >= max_count:
                    break
                
                # Try both orders
                for word1, word2 in [(core, other), (other, core)]:
                    if word1 == word2:
                        continue
                    
                    compound = self._apply_compound_sandhi([word1, word2])
                    
                    if (compound not in compounds and 
                        compound not in self.generated_compounds):
                        
                        compound_type = self._determine_religious_compound_type(word1, word2, core)
                        meaning = self._compose_religious_meaning([word1, word2], compound_type, core)
                        
                        compounds[compound] = {
                            "components": [word1, word2],
                            "type": f"religious_{compound_type}",
                            "meaning": meaning,
                            "religious_core": core,
                            "frequency": 3.5
                        }
                        
                        self.generated_compounds.add(compound)
                        count += 1
        
        return compounds
    
    def _generate_technical_specialized_compounds(self, semantic_fields, max_count):
        """Generate technical and specialized compounds"""
        compounds = {}
        count = 0
        
        # Technical vocabulary
        technical_vocab = []
        if hasattr(self.kb, 'comprehensive_technical_vocabulary'):
            for field, terms in self.kb.comprehensive_technical_vocabulary.items():
                technical_vocab.extend(terms)
        
        # Generate technical compounds
        for i, term1 in enumerate(technical_vocab):
            if count >= max_count:
                break
                
            for j, term2 in enumerate(technical_vocab):
                if i == j or count >= max_count:
                    continue
                
                compound = self._apply_compound_sandhi([term1, term2])
                
                if (compound not in compounds and 
                    compound not in self.generated_compounds):
                    
                    meaning = f"technical compound of {term1} and {term2}"
                    
                    compounds[compound] = {
                        "components": [term1, term2],
                        "type": "technical_compound",
                        "meaning": meaning,
                        "frequency": 2.5
                    }
                    
                    self.generated_compounds.add(compound)
                    count += 1
        
        return compounds
    
    def _generate_multi_level_recursive_compounds(self, existing_compounds, max_count):
        """Generate 3, 4, and 5 word compounds"""
        compounds = {}
        count = 0
        
        # Select base compounds for recursion
        suitable_bases = [
            (comp, info) for comp, info in existing_compounds.items()
            if len(info["components"]) == 2
        ]
        
        # Additional elements for extension
        extensions = ["ñāṇa", "dassana", "vimutti", "magga", "phala", "sampatti", 
                     "paṭilābha", "adhigama", "paṭiveda", "sacchikiriyā"]
        
        # Generate 3-word compounds
        for base_compound, base_info in suitable_bases[:1000]:  # Limit base compounds
            if count >= max_count:
                break
                
            for ext in extensions:
                if count >= max_count:
                    break
                
                # Create 3-word compound
                components = base_info["components"] + [ext]
                compound = self._apply_compound_sandhi(components)
                
                if (compound not in compounds and 
                    compound not in self.generated_compounds):
                    
                    base_meaning = base_info["meaning"]
                    ext_meaning = self._get_word_meaning(ext)
                    full_meaning = f"{ext_meaning} of {base_meaning}"
                    
                    compounds[compound] = {
                        "components": components,
                        "type": "three_word_compound",
                        "meaning": full_meaning,
                        "base_compound": base_compound,
                        "depth": 3,
                        "frequency": 2.0
                    }
                    
                    self.generated_compounds.add(compound)
                    count += 1
        
        # Generate 4-word compounds from 3-word compounds
        three_word_compounds = [
            (comp, info) for comp, info in compounds.items()
            if info.get("depth") == 3
        ]
        
        for base_compound, base_info in three_word_compounds[:500]:
            if count >= max_count:
                break
            
            for ext in extensions[:3]:  # Limit extensions for 4-word
                if count >= max_count:
                    break
                
                components = base_info["components"] + [ext]
                compound = self._apply_compound_sandhi(components)
                
                if (compound not in compounds and 
                    compound not in self.generated_compounds):
                    
                    base_meaning = base_info["meaning"]
                    ext_meaning = self._get_word_meaning(ext)
                    full_meaning = f"{ext_meaning} involving {base_meaning}"
                    
                    compounds[compound] = {
                        "components": components,
                        "type": "four_word_compound",
                        "meaning": full_meaning,
                        "base_compound": base_compound,
                        "depth": 4,
                        "frequency": 1.8
                    }
                    
                    self.generated_compounds.add(compound)
                    count += 1
        
        return compounds
    
    def _is_meaningful_combination(self, word1, word2):
        """Check if two words can form a meaningful compound"""
        # Get semantic fields for both words
        fields1 = self._get_semantic_fields(word1)
        fields2 = self._get_semantic_fields(word2)
        
        # Avoid meaningless combinations
        meaningless_combinations = [
            (["particles"], ["particles"]),
            (["prefixes"], ["prefixes"]),
            (["numbers"], ["numbers"]),
        ]
        
        for combo in meaningless_combinations:
            if (any(f in combo[0] for f in fields1) and 
                any(f in combo[1] for f in fields2)):
                return False
        
        # Encourage meaningful combinations
        meaningful_combinations = [
            (["qualities"], ["beings"]),
            (["action"], ["objects"]),
            (["temporal"], ["events"]),
            (["spatial"], ["entities"]),
            (["mind"], ["qualities"]),
            (["enlightenment"], ["path"]),
            (["ethics"], ["practice"]),
        ]
        
        for combo in meaningful_combinations:
            if (any(f in combo[0] for f in fields1) and 
                any(f in combo[1] for f in fields2)):
                return True
        
        # Default: allow if not explicitly meaningless
        return True
    
    def _determine_compound_type(self, word1, word2):
        """Determine compound type based on semantic analysis"""
        fields1 = self._get_semantic_fields(word1)
        fields2 = self._get_semantic_fields(word2)
        
        # Tatpuruṣa patterns
        if any(f in ["beings", "society"] for f in fields1):
            return "tatpurusa"
        
        # Karmadhāraya patterns
        if any(f in ["qualities", "colors"] for f in fields1):
            return "karmadharaya"
        
        # Bahuvrīhi patterns
        if any(f in ["body", "faculties"] for f in fields2):
            return "bahuvrihi"
        
        # Dvandva patterns
        if fields1 == fields2:
            return "dvandva"
        
        # Default
        return "tatpurusa"
    
    def _determine_religious_compound_type(self, word1, word2, core):
        """Determine type for religious compounds"""
        if core == word1:
            return "core_modifier"  # buddha+X
        elif core == word2:
            return "modifier_core"  # X+buddha
        else:
            return "religious_tatpurusa"
    
    def _compose_religious_meaning(self, components, compound_type, core):
        """Compose meaning for religious compounds"""
        meanings = [self._get_word_meaning(comp) for comp in components]
        
        if compound_type == "core_modifier":
            return f"{meanings[0]}'s {meanings[1]}"
        elif compound_type == "modifier_core":
            return f"{meanings[1]} of {meanings[0]}"
        else:
            return f"{meanings[1]} related to {meanings[0]}"
    
    def _calculate_combination_frequency(self, word1, word2):
        """Calculate frequency for word combinations"""
        # Get base frequencies
        freq1 = self._get_word_frequency(word1)
        freq2 = self._get_word_frequency(word2)
        
        # Calculate combined frequency
        combined = (freq1 + freq2) / 2
        
        # Apply combination penalty
        return combined * 0.8
    
    def _get_word_frequency(self, word):
        """Get frequency for a word"""
        if word in self.kb.base_meanings:
            return self.kb.base_meanings[word].get("frequency", 3.0)
        elif hasattr(self.kb, 'comprehensive_indeclinables') and word in self.kb.comprehensive_indeclinables:
            return self.kb.comprehensive_indeclinables[word].get("frequency", 3.0)
        else:
            return 3.0

# ============ ULTIMATE MONUMENTAL PALI DICTIONARY GENERATOR ============

class UltimateMonumentalPaliDictionaryGenerator(MonumentalPaliDictionaryGenerator):
    """The ultimate, complete, and definitive implementation"""
    
    def __init__(self, kaggle_mode=False):
        print("🔬 Initializing ULTIMATE Monumental Pali Dictionary Generator...")
        
        # Detect environment
        self.kaggle_mode = kaggle_mode or os.path.exists('/kaggle/input')
        
        # Initialize ULTIMATE knowledge base
        self.kb = UltimateExhaustivePaliSemanticKnowledgeBase(self.kaggle_mode)
        
        # Initialize ULTIMATE generators
        print("🔧 Initializing Ultimate Generators...")
        self.compound_compositor = UltimateCompoundSemanticCompositor(self.kb)
        self.morphological_generator = MorphologicalSemanticGenerator(self.kb)
        self.derivational_generator = DerivationalSemanticGenerator(self.kb)
        self.validator = SemanticValidator()
        
        # Dictionary storage
        self.generated_dict = {}
        self.generation_stats = defaultdict(int)
        self.quality_stats = defaultdict(int)
        
        # NO LIMITS - Ultimate generation
        self.limits = {
            "morphological_forms_per_word": 1000,    # All possible forms
            "verbal_forms_per_root": 1000,           # All tenses/persons/numbers
            "compounds_per_type": 50000,             # Massive compound generation
            "derivatives_per_pattern": 10000,        # All derivatives
            "sandhi_variants_per_word": 100,         # Comprehensive sandhi
            "max_recursive_depth": 5,                # Deep recursion
            "max_total_target": 1000000              # 1 million entries target
        }
        
        # Load existing dictionary
        self.existing_dict_path = "pali_dictionary.json"
        self.existing_words = set()
        self._load_existing_dictionary()
    
    def generate_ultimate_dictionary(self):
        """Generate the ultimate complete dictionary"""
        print("\n🚀 GENERATING ULTIMATE MONUMENTAL PALI DICTIONARY")
        print("=" * 80)
        print("Target: 1,000,000+ entries with perfect quality")
        
        start_time = datetime.now()
        
        # Phase 1: Generate ALL base entries with all variants
        print("\n📍 Phase 1: Ultimate Base Entries")
        self._generate_ultimate_base_entries()
        
        # Phase 2: Generate ALL morphological forms (no limits)
        print("\n📍 Phase 2: Complete Morphological Universe")
        self._generate_complete_morphological_universe()
        
        # Phase 3: Generate ALL prefixed forms
        print("\n📍 Phase 3: Complete Prefixed Form Universe")
        self._generate_complete_prefixed_universe()
        
        # Phase 4: Generate ALL compounds with unlimited recursion
        print("\n📍 Phase 4: Unlimited Compound Generation")
        self._generate_unlimited_compounds()
        
        # Phase 5: Generate ALL derivatives and secondary derivatives
        print("\n📍 Phase 5: Complete Derivational Universe")
        self._generate_complete_derivational_universe()
        
        # Phase 6: Generate ALL technical vocabulary
        print("\n📍 Phase 6: Complete Technical Vocabulary")
        self._generate_complete_technical_vocabulary()
        
        # Phase 7: Generate ALL phrasal expressions
        print("\n📍 Phase 7: Complete Phrasal Universe")
        self._generate_complete_phrasal_universe()
        
        # Phase 8: Generate ALL numerical expressions
        print("\n📍 Phase 8: Complete Numerical Universe")
        self._generate_complete_numerical_universe()
        
        # Phase 9: Generate ALL sandhi variants
        print("\n📍 Phase 9: Complete Sandhi Universe")
        self._generate_complete_sandhi_universe()
        
        # Phase 10: Generate proper name declensions
        print("\n📍 Phase 10: Complete Proper Name Universe")
        self._generate_complete_proper_name_universe()
        
        # Phase 11: Ultimate validation and enhancement
        print("\n📍 Phase 11: Ultimate Validation and Enhancement")
        self._ultimate_validation_and_enhancement()
        
        # Calculate generation time
        end_time = datetime.now()
        generation_time = (end_time - start_time).total_seconds()
        
        # Final statistics
        print(f"\n📊 ULTIMATE GENERATION COMPLETE!")
        print(f"   Total entries: {len(self.generated_dict):,}")
        print(f"   Generation time: {generation_time:.2f} seconds")
        print(f"   Entries per second: {len(self.generated_dict)/generation_time:.0f}")
        
        # Quality analysis
        quality_percentage = (self.quality_stats.get("excellent", 0) + 
                            self.quality_stats.get("good", 0)) / len(self.generated_dict) * 100
        print(f"   Quality (good+excellent): {quality_percentage:.1f}%")
        
        print(f"\n   Ultimate breakdown by category:")
        for category, count in sorted(self.generation_stats.items()):
            if category not in ["invalid_removed", "meanings_enhanced", "average_quality"]:
                print(f"   - {category}: {count:,}")
        
        return self.generated_dict
    
    def _generate_ultimate_base_entries(self):
        """Generate all possible base entries"""
        count = 0
        
        # Process ALL base words
        for word, info in self.kb.base_meanings.items():
            if word not in self.existing_words:
                # Create comprehensive entry
                entry = self._create_comprehensive_base_entry(word, info)
                self.generated_dict[word] = entry
                count += 1
                
                # Generate ALL contextual variants
                if hasattr(self.kb, 'contextual_meanings') and word in self.kb.contextual_meanings:
                    context_count = self._generate_all_contextual_variants(word, self.kb.contextual_meanings[word])
                    count += context_count
                
                # Generate ALL register variants
                if hasattr(self.kb, 'register_variations'):
                    register_count = self._generate_all_register_variants(word, info)
                    count += register_count
                
                # Generate ALL historical variants
                if hasattr(self.kb, 'historical_layers'):
                    historical_count = self._generate_all_historical_variants(word, info)
                    count += historical_count
        
        # Process ALL indeclinables
        if hasattr(self.kb, 'comprehensive_indeclinables'):
            for word, info in self.kb.comprehensive_indeclinables.items():
                if word not in self.existing_words and word not in self.generated_dict:
                    entry = {
                        "word": word,
                        "meaning": self.validator.enhance_meaning(info["meaning"]),
                        "type": "indeclinable",
                        "subtype": info["type"],
                        "position": info.get("position", "various"),
                        "frequency": info.get("frequency", 3.0),
                        "indeclinable": True
                    }
                    self.generated_dict[word] = entry
                    count += 1
        
        print(f"   ✅ Generated {count} ultimate base entries")
        self.generation_stats["base_words"] = count
    
    def _generate_complete_morphological_universe(self):
        """Generate ALL possible morphological forms"""
        count = 0
        
        # Phase A: ALL nominal forms (no limits)
        print("   📝 Generating ALL nominal forms (unlimited)...")
        count += self._generate_unlimited_nominal_forms()
        
        # Phase B: ALL verbal forms (no limits)
        print("   📝 Generating ALL verbal forms (unlimited)...")
        count += self._generate_unlimited_verbal_forms()
        
        # Phase C: ALL participle forms (complete system)
        print("   📝 Generating complete participle system...")
        count += self._generate_complete_participle_system()
        
        # Phase D: ALL comparison forms
        print("   📝 Generating ALL comparison forms...")
        count += self._generate_all_comparison_forms()
        
        # Phase E: ALL denominative forms
        print("   📝 Generating ALL denominative forms...")
        count += self._generate_all_denominative_forms()
        
        print(f"   ✅ Generated {count} morphological forms total")
        self.generation_stats["morphological_forms"] = count
    
    def _generate_unlimited_nominal_forms(self):
        """Generate ALL nominal forms for ALL words"""
        count = 0
        cases = ["nominative", "accusative", "instrumental", "dative", 
                "ablative", "genitive", "locative", "vocative"]
        numbers = ["singular", "dual", "plural"]
        
        # Process ALL words that can be declined
        declinable_words = []
        
        # Add base words
        for word, info in self.kb.base_meanings.items():
            if info.get("semantic_field") not in ["particles", "prefixes"]:
                declinable_words.append((word, info))
        
        # Add proper names
        if hasattr(self.kb, 'proper_names'):
            for word, info in self.kb.proper_names.items():
                declinable_words.append((word, info))
        
        # Add technical terms
        if hasattr(self.kb, 'comprehensive_technical_vocabulary'):
            for field, terms in self.kb.comprehensive_technical_vocabulary.items():
                for term in terms:
                    if term not in [w[0] for w in declinable_words]:
                        # Create basic info
                        info = {
                            "semantic_field": field,
                            "register": "technical",
                            "gender": "m",  # Default
                            "declension": "a_masculine"  # Default
                        }
                        declinable_words.append((term, info))
        
        # Generate ALL forms for ALL words
        for base, info in declinable_words:
            # Determine possible genders
            genders = self._determine_all_genders(base, info)
            
            for gender in genders:
                for case in cases:
                    for number in numbers:
                        # Skip certain combinations
                        if self._should_skip_form(case, number, info):
                            continue
                        
                        # Generate form
                        form = self._apply_nominal_morphology(base, case, number, gender)
                        
                        if (form and form != base and 
                            form not in self.existing_words and 
                            form not in self.generated_dict and
                            len(form) > 1):
                            
                            # Generate meaning
                            meaning = self.morphological_generator.generate_nominal_meaning(
                                base, case, number, gender
                            )
                            
                            # Validate meaning
                            is_valid, _ = self.validator.validate_meaning(meaning)
                            if is_valid:
                                entry = {
                                    "word": form,
                                    "meaning": self.validator.enhance_meaning(meaning),
                                    "type": "inflected_noun",
                                    "base": base,
                                    "case": case,
                                    "number": number,
                                    "gender": gender,
                                    "semantic_field": info.get("semantic_field", "general"),
                                    "frequency": self._calculate_form_frequency(base, case, number)
                                }
                                
                                # Add additional info
                                if "register" in info:
                                    entry["register"] = info["register"]
                                
                                self.generated_dict[form] = entry
                                count += 1
        
        return count
    
    def _generate_unlimited_verbal_forms(self):
        """Generate ALL verbal forms for ALL roots"""
        count = 0
        persons = ["1st", "2nd", "3rd"]
        numbers = ["singular", "dual", "plural"]
        tenses = ["present", "aorist", "perfect", "future", "imperative", "optative", "conditional"]
        voices = ["active", "middle", "passive", "causative", "desiderative", "intensive", "denominative"]
        
        # Process ALL roots
        for root, info in self.kb.root_meanings.items():
            for voice in voices:
                # Skip impossible combinations
                if not self._is_valid_voice_combination(voice, tenses):
                    continue
                
                for tense in tenses:
                    # Skip invalid combinations
                    if not self._is_valid_tense_voice_combination(tense, voice):
                        continue
                    
                    for person in persons:
                        for number in numbers:
                            # Skip certain combinations
                            if self._should_skip_verbal_form(tense, person, number, voice):
                                continue
                            
                            # Generate form
                            form = self._apply_verbal_morphology(root, person, number, tense, voice)
                            
                            if (form and form not in self.existing_words and 
                                form not in self.generated_dict and
                                len(form) > 2):
                                
                                # Generate meaning
                                meaning = self.morphological_generator.generate_verbal_meaning(
                                    root, person, number, tense, voice
                                )
                                
                                # Validate
                                is_valid, _ = self.validator.validate_meaning(meaning)
                                if is_valid:
                                    entry = {
                                        "word": form,
                                        "meaning": self.validator.enhance_meaning(meaning),
                                        "type": "verb",
                                        "root": root,
                                        "person": person,
                                        "number": number,
                                        "tense": tense,
                                        "voice": voice,
                                        "semantic_field": info.get("semantic_field", "action"),
                                        "frequency": self._calculate_verb_frequency(tense, voice, person, number)
                                    }
                                    
                                    self.generated_dict[form] = entry
                                    count += 1
        
        return count
    
    def _generate_complete_participle_system(self):
        """Generate complete participle system"""
        count = 0
        
        # All participle types
        participle_types = {
            "present_active": {"suffix": "ant", "meaning": "ing", "declinable": True},
            "present_middle": {"suffix": "māna", "meaning": "ing (reflexive)", "declinable": True},
            "present_passive": {"suffix": "yamāna", "meaning": "being Xed", "declinable": True},
            "past_passive": {"suffix": "ta", "meaning": "ed", "declinable": True},
            "past_active": {"suffix": "tavant", "meaning": "having Xed", "declinable": True},
            "past_middle": {"suffix": "āna", "meaning": "having Xed (for oneself)", "declinable": True},
            "future_passive": {"suffix": "tabba", "meaning": "to be Xed", "declinable": True},
            "future_passive_2": {"suffix": "anīya", "meaning": "should be Xed", "declinable": True},
            "future_active": {"suffix": "ssant", "meaning": "about to X", "declinable": True},
            "perfect_active": {"suffix": "vant", "meaning": "having Xed", "declinable": True},
            "gerund": {"suffix": "tvā", "meaning": "having Xed", "declinable": False},
            "gerund_prefixed": {"suffix": "ya", "meaning": "having Xed (with prefix)", "declinable": False},
            "infinitive": {"suffix": "tuṃ", "meaning": "to X", "declinable": False},
            "absolutive": {"suffix": "tvāna", "meaning": "having Xed", "declinable": False},
            "conditional_participle": {"suffix": "ce", "meaning": "if Xing", "declinable": False},
            "temporal_participle": {"suffix": "kāle", "meaning": "when Xing", "declinable": False}
        }
        
        genders = ["masculine", "feminine", "neuter"]
        numbers = ["singular", "dual", "plural"]
        cases = ["nominative", "accusative", "instrumental", "dative", "ablative", "genitive", "locative", "vocative"]
        
        # Process ALL roots
        for root, root_data in self.kb.root_meanings.items():
            clean_root = root.replace("√", "")
            
            for p_type, p_info in participle_types.items():
                # Generate base participle
                base_participle = self._generate_participle_base(clean_root, p_type, p_info, root_data)
                
                if not base_participle:
                    continue
                
                if not p_info["declinable"]:
                    # Indeclinable participle
                    if (base_participle not in self.existing_words and 
                        base_participle not in self.generated_dict):
                        
                        meaning = f"{root_data.get('meaning', root)} ({p_info['meaning']})"
                        
                        entry = {
                            "word": base_participle,
                            "meaning": self.validator.enhance_meaning(meaning),
                            "type": "participle",
                            "participle_type": p_type,
                            "root": root,
                            "indeclinable": True,
                            "frequency": 3.0
                        }
                        
                        self.generated_dict[base_participle] = entry
                        count += 1
                
                else:
                    # Declinable participle - generate ALL forms
                    for gender in genders:
                        for number in numbers:
                            for case in cases:
                                form = self._apply_participle_declension(
                                    base_participle, p_type, gender, number, case
                                )
                                
                                if (form and form not in self.existing_words and 
                                    form not in self.generated_dict):
                                    
                                    # Generate meaning
                                    meaning = self.morphological_generator.generate_participle_meaning(
                                        root, p_type, gender, number
                                    )
                                    
                                    # Add case information
                                    case_meaning = self.morphological_generator.case_templates[case]["default"]
                                    full_meaning = case_meaning.format(meaning)
                                    
                                    # Validate
                                    is_valid, _ = self.validator.validate_meaning(full_meaning)
                                    if is_valid:
                                        entry = {
                                            "word": form,
                                            "meaning": self.validator.enhance_meaning(full_meaning),
                                            "type": "participle",
                                            "participle_type": p_type,
                                            "root": root,
                                            "gender": gender,
                                            "number": number,
                                            "case": case,
                                            "semantic_field": root_data.get("semantic_field", "action"),
                                            "frequency": 2.5
                                        }
                                        
                                        self.generated_dict[form] = entry
                                        count += 1
        
        return count
    
    def _generate_all_comparison_forms(self):
        """Generate ALL comparative and superlative forms"""
        count = 0
        
        # Get ALL adjective-like words
        adjective_words = []
        
        # From base words
        for word, info in self.kb.base_meanings.items():
            if (info.get("semantic_field") in ["qualities", "colors", "mental_factors"] or 
                info.get("pos") == "adjective"):
                adjective_words.append(word)
        
        # From semantic fields
        for field in ["qualities", "mental_factors", "emotions"]:
            if field in self.kb.semantic_fields:
                adjective_words.extend(self.kb.semantic_fields[field])
        
        # Remove duplicates
        adjective_words = list(set(adjective_words))
        
        # Generate ALL comparison forms
        for adj in adjective_words:
            # Comparative forms (-tara, -iya)
            comp_suffixes = ["-tara", "-iya"]
            for suffix in comp_suffixes:
                form = adj + suffix.replace("-", "")
                
                if (form not in self.existing_words and 
                    form not in self.generated_dict):
                    
                    base_meaning = self._get_base_meaning(adj)
                    meaning = f"more {base_meaning}, rather {base_meaning}"
                    
                    entry = {
                        "word": form,
                        "meaning": self.validator.enhance_meaning(meaning),
                        "type": "derivative_comparison",
                        "base": adj,
                        "degree": "comparative",
                        "suffix": suffix,
                        "frequency": 2.5
                    }
                    
                    self.generated_dict[form] = entry
                    count += 1
            
            # Superlative forms (-tama, -iṭṭha)
            sup_suffixes = ["-tama", "-iṭṭha"]
            for suffix in sup_suffixes:
                form = adj + suffix.replace("-", "")
                
                if (form not in self.existing_words and 
                    form not in self.generated_dict):
                    
                    base_meaning = self._get_base_meaning(adj)
                    meaning = f"most {base_meaning}, very {base_meaning}"
                    
                    entry = {
                        "word": form,
                        "meaning": self.validator.enhance_meaning(meaning),
                        "type": "derivative_comparison",
                        "base": adj,
                        "degree": "superlative",
                        "suffix": suffix,
                        "frequency": 2.5
                    }
                    
                    self.generated_dict[form] = entry
                    count += 1
        
        return count
    
    def _generate_all_denominative_forms(self):
        """Generate ALL denominative verb forms"""
        count = 0
        
        patterns = {
            "-āyati": "acts like X, desires X",
            "-iyati": "behaves as X", 
            "-eti": "makes into X",
            "-āpeti": "causes to become X",
            "-karoti": "does X",
            "-bhavati": "becomes X"
        }
        
        # Select ALL suitable nouns
        noun_bases = []
        for word, info in self.kb.base_meanings.items():
            if info.get("semantic_field") in ["beings", "qualities", "emotions", "mind", "society", "nature"]:
                noun_bases.append(word)
        
        # Generate denominative verbs for ALL bases
        for base in noun_bases:
            for suffix, meaning_template in patterns.items():
                # Generate ALL persons, numbers, tenses
                for tense in ["present", "aorist", "future", "imperative", "optative"]:
                    for person in ["1st", "2nd", "3rd"]:
                        for number in ["singular", "dual", "plural"]:
                            # Skip certain combinations
                            if tense == "imperative" and person == "1st" and number == "singular":
                                continue
                            
                            form = self._generate_denominative_form(base, suffix, person, number, tense)
                            
                            if (form and form not in self.existing_words and 
                                form not in self.generated_dict):
                                
                                base_meaning = self._get_base_meaning(base)
                                template_meaning = meaning_template.replace("X", base_meaning)
                                
                                # Add tense/person info
                                tense_template = self.morphological_generator.tense_templates[tense]["active"]
                                verbal_meaning = tense_template.format(template_meaning)
                                pronoun = self.morphological_generator._get_pronoun(person, number)
                                final_meaning = f"({pronoun}) {verbal_meaning}"
                                
                                entry = {
                                    "word": form,
                                    "meaning": self.validator.enhance_meaning(final_meaning),
                                    "type": "derivative_denominative_verbs",
                                    "base": base,
                                    "suffix": suffix,
                                    "person": person,
                                    "number": number,
                                    "tense": tense,
                                    "frequency": 2.0
                                }
                                
                                self.generated_dict[form] = entry
                                count += 1
        
        return count
    
    def _generate_complete_prefixed_universe(self):
        """Generate ALL possible prefixed forms"""
        count = 0
        
        # Phase A: ALL single-prefix combinations
        print("   📝 Generating ALL single-prefix combinations...")
        count += self._generate_all_single_prefix_combinations()
        
        # Phase B: ALL double-prefix combinations
        print("   📝 Generating ALL double-prefix combinations...")
        count += self._generate_all_double_prefix_combinations()
        
        # Phase C: Triple-prefix combinations (rare but possible)
        print("   📝 Generating triple-prefix combinations...")
        count += self._generate_triple_prefix_combinations()
        
        print(f"   ✅ Generated {count} prefixed forms total")
        self.generation_stats["prefixed_verbs"] = count
        return count
    
    def _generate_all_single_prefix_combinations(self):
        """Generate ALL single prefix combinations"""
        count = 0
        
        # Get ALL prefixes
        all_prefixes = list(self.kb.prefix_meanings.keys())
        
        # Process ALL roots
        for root, root_data in self.kb.root_meanings.items():
            for prefix in all_prefixes:
                # Generate multiple tenses and forms
                for tense in ["present", "aorist", "future", "imperative", "optative", "conditional"]:
                    for person in ["1st", "2nd", "3rd"]:
                        for number in ["singular", "dual", "plural"]:
                            # Skip certain combinations
                            if self._should_skip_verbal_form(tense, person, number, "active"):
                                continue
                            
                            # Get base form
                            base_form = self._apply_verbal_morphology(root, person, number, tense)
                            
                            if base_form:
                                # Apply prefix with sandhi
                                prefixed_form = self._apply_prefix_sandhi(prefix, base_form)
                                
                                if (prefixed_form not in self.existing_words and 
                                    prefixed_form not in self.generated_dict):
                                    
                                    # Generate meaning
                                    prefix_meaning = self.kb.prefix_meanings.get(prefix, prefix)
                                    root_meaning = root_data.get("meaning", root)
                                    
                                    # Compose meaning
                                    combined_meaning = f"{prefix_meaning} {root_meaning}"
                                    tense_template = self.morphological_generator.tense_templates[tense]["active"]
                                    verbal_meaning = tense_template.format(combined_meaning)
                                    pronoun = self.morphological_generator._get_pronoun(person, number)
                                    full_meaning = f"({pronoun}) {verbal_meaning}"
                                    
                                    entry = {
                                        "word": prefixed_form,
                                        "meaning": self.validator.enhance_meaning(full_meaning),
                                        "type": "prefixed_verb",
                                        "root": root,
                                        "prefix": prefix,
                                        "person": person,
                                        "number": number,
                                        "tense": tense,
                                        "semantic_field": root_data.get("semantic_field", "action"),
                                        "frequency": 3.5
                                    }
                                    
                                    self.generated_dict[prefixed_form] = entry
                                    count += 1
                
                # Also generate participles with prefixes
                count += self._generate_single_prefix_participles(root, prefix, root_data)
        
        return count
    
    def _generate_all_double_prefix_combinations(self):
        """Generate ALL double prefix combinations"""
        count = 0
        
        # Extended double-prefix combinations
        double_prefixes = [
            ("sam", "anu"), ("sam", "pa"), ("sam", "pari"), ("sam", "ud"), ("sam", "ā"),
            ("pari", "ni"), ("pari", "ā"), ("pari", "ud"), ("pari", "pa"),
            ("vi", "pa"), ("vi", "ni"), ("vi", "ā"), ("vi", "sam"), ("vi", "pari"),
            ("anu", "pa"), ("anu", "vi"), ("anu", "sam"), ("anu", "pari"),
            ("pa", "ni"), ("pa", "vi"), ("pa", "ā"), ("pa", "ud"),
            ("ud", "pa"), ("ud", "ā"), ("ud", "sam"), ("ud", "vi"),
            ("ni", "pa"), ("ni", "vi"), ("ni", "sam"), ("ni", "ā"),
            ("ā", "pa"), ("ā", "vi"), ("ā", "sam"), ("ā", "pari"),
            ("abhi", "sam"), ("abhi", "ā"), ("abhi", "vi"), ("abhi", "ud"),
            ("adhi", "ṭhā"), ("adhi", "vas"), ("adhi", "gam"), ("adhi", "kar")
        ]
        
        # Select high-frequency roots
        frequent_roots = [
            root for root, info in self.kb.root_meanings.items()
            if info.get("frequency") == "high"
        ]
        
        # If no frequency info, use first 100 roots
        if not frequent_roots:
            frequent_roots = list(self.kb.root_meanings.keys())[:100]
        
        for prefix1, prefix2 in double_prefixes:
            for root in frequent_roots:
                # Generate select forms
                for tense in ["present", "aorist", "future"]:
                    for person in ["3rd"]:  # Focus on 3rd person
                        for number in ["singular", "plural"]:
                            # Get base form
                            base_form = self._apply_verbal_morphology(root, person, number, tense)
                            
                            if base_form:
                                # Apply both prefixes with sandhi
                                step1 = self._apply_prefix_sandhi(prefix2, base_form)
                                prefixed_form = self._apply_prefix_sandhi(prefix1, step1)
                                
                                if (prefixed_form not in self.existing_words and 
                                    prefixed_form not in self.generated_dict):
                                    
                                    # Generate meaning
                                    prefix1_meaning = self.kb.prefix_meanings.get(prefix1, prefix1)
                                    prefix2_meaning = self.kb.prefix_meanings.get(prefix2, prefix2)
                                    root_meaning = self.kb.root_meanings[root].get("meaning", root)
                                    
                                    combined_meaning = f"{prefix1_meaning} {prefix2_meaning} {root_meaning}"
                                    
                                    tense_template = self.morphological_generator.tense_templates[tense]["active"]
                                    verbal_meaning = tense_template.format(combined_meaning)
                                    pronoun = self.morphological_generator._get_pronoun(person, number)
                                    full_meaning = f"({pronoun}) {verbal_meaning}"
                                    
                                    entry = {
                                        "word": prefixed_form,
                                        "meaning": self.validator.enhance_meaning(full_meaning),
                                        "type": "prefixed_verb",
                                        "root": root,
                                        "prefix": f"{prefix1}+{prefix2}",
                                        "person": person,
                                        "number": number,
                                        "tense": tense,
                                        "prefix_type": "double",
                                        "frequency": 2.5
                                    }
                                    
                                    self.generated_dict[prefixed_form] = entry
                                    count += 1
        
        return count
    
    def _generate_triple_prefix_combinations(self):
        """Generate triple prefix combinations (very rare)"""
        count = 0
        
        # Only most common triple combinations
        triple_prefixes = [
            ("sam", "ā", "pa"), ("sam", "pari", "ā"), ("vi", "sam", "ā"),
            ("anu", "sam", "pa"), ("pari", "sam", "ā"), ("abhi", "sam", "ā")
        ]
        
        # Only highest frequency roots
        top_roots = ["√gam", "√kar", "√bhū", "√ṭhā", "√dis"]
        
        for prefix1, prefix2, prefix3 in triple_prefixes:
            for root in top_roots:
                if root in self.kb.root_meanings:
                    # Generate only present 3rd singular
                    base_form = self._apply_verbal_morphology(root, "3rd", "singular", "present")
                    
                    if base_form:
                        # Apply all three prefixes
                        step1 = self._apply_prefix_sandhi(prefix3, base_form)
                        step2 = self._apply_prefix_sandhi(prefix2, step1)
                        prefixed_form = self._apply_prefix_sandhi(prefix1, step2)
                        
                        if (prefixed_form not in self.existing_words and 
                            prefixed_form not in self.generated_dict):
                            
                            # Generate meaning
                            prefix1_meaning = self.kb.prefix_meanings.get(prefix1, prefix1)
                            prefix2_meaning = self.kb.prefix_meanings.get(prefix2, prefix2)
                            prefix3_meaning = self.kb.prefix_meanings.get(prefix3, prefix3)
                            root_meaning = self.kb.root_meanings[root].get("meaning", root)
                            
                            combined_meaning = f"{prefix1_meaning} {prefix2_meaning} {prefix3_meaning} {root_meaning}"
                            
                            entry = {
                                "word": prefixed_form,
                                "meaning": self.validator.enhance_meaning(f"(he/she/it) {combined_meaning}s"),
                                "type": "prefixed_verb",
                                "root": root,
                                "prefix": f"{prefix1}+{prefix2}+{prefix3}",
                                "person": "3rd",
                                "number": "singular",
                                "tense": "present",
                                "prefix_type": "triple",
                                "frequency": 1.5,
                                "rare": True
                            }
                            
                            self.generated_dict[prefixed_form] = entry
                            count += 1
        
        return count
    
    def _generate_unlimited_compounds(self):
        """Generate unlimited compounds"""
        count = 0
        
        # Use the ultimate compositor
        compounds = self.compound_compositor.generate_unlimited_compounds(
            self.kb.semantic_fields,
            max_total=self.limits["compounds_per_type"]
        )
        
        for compound, compound_info in compounds.items():
            if (compound not in self.existing_words and 
                compound not in self.generated_dict):
                
                entry = {
                    "word": compound,
                    "meaning": self.validator.enhance_meaning(compound_info["meaning"]),
                    "type": f"compound_{compound_info['type']}",
                    "components": compound_info["components"],
                    "pattern": compound_info.get("pattern", ""),
                    "semantic_field": "compound",
                    "frequency": compound_info.get("frequency", 2.5)
                }
                
                # Add depth for recursive compounds
                if "depth" in compound_info:
                    entry["depth"] = compound_info["depth"]
                    entry["base_compound"] = compound_info.get("base_compound", "")
                
                self.generated_dict[compound] = entry
                count += 1
        
        print(f"   ✅ Generated {count} unlimited compounds")
        self.generation_stats["compounds"] = count
        return count
    
    def _generate_complete_derivational_universe(self):
        """Generate ALL possible derivatives"""
        count = 0
        
        # Process ALL derivation patterns without limits
        for category, patterns in self.kb.derivation_patterns.items():
            print(f"      • Generating ALL {category}...")
            category_count = 0
            
            for suffix, suffix_info in patterns.items():
                # Select ALL appropriate base words
                if category in ["verbal_nouns", "agent_nouns"]:
                    # Use ALL roots
                    bases = list(self.kb.root_meanings.keys())
                else:
                    # Use ALL suitable base words
                    bases = [
                        w for w in self.kb.base_meanings.keys() 
                        if self.kb.base_meanings[w].get("semantic_field") not in ["particles"]
                    ]
                
                # Generate derivatives for ALL bases (no limits)
                for base in bases:
                    form = base.replace("√", "") + suffix.replace("-", "")
                    
                    if (form not in self.existing_words and 
                        form not in self.generated_dict):
                        
                        # Generate meaning with context
                        semantic_context = self._determine_semantic_context(base, category)
                        derivative_meaning = self.derivational_generator.generate_derivative_meaning(
                            base, suffix, category, semantic_context
                        )
                        
                        entry = {
                            "word": form,
                            "meaning": self.validator.enhance_meaning(derivative_meaning),
                            "type": f"derivative_{category}",
                            "base": base,
                            "suffix": suffix,
                            "frequency": self._calculate_derivative_frequency(base, suffix, category)
                        }
                        
                        # Add gender if specified
                        if "gender" in suffix_info:
                            entry["gender"] = suffix_info["gender"]
                        
                        self.generated_dict[form] = entry
                        count += 1
                        category_count += 1
            
            print(f"        ✓ {category_count} {category}")
        
        # Generate ALL secondary derivatives
        print("      • Generating ALL secondary derivatives...")
        secondary_count = self._generate_all_secondary_derivatives()
        count += secondary_count
        
        # Generate ALL tertiary derivatives
        print("      • Generating tertiary derivatives...")
        tertiary_count = self._generate_tertiary_derivatives()
        count += tertiary_count
        
        print(f"   ✅ Generated {count} derivative forms total")
        self.generation_stats["derivatives"] = count
        return count
    
    def _generate_all_secondary_derivatives(self):
        """Generate ALL secondary derivatives"""
        count = 0
        
        # Extended patterns for secondary derivation
        secondary_patterns = {
            "-tā": ["abstract_nouns", "state of being X"],
            "-tva": ["abstract_nouns", "nature of X"],
            "-ya": ["abstract_nouns", "condition of X"],
            "-ka": ["diminutives", "little X"],
            "-ika": ["possessive_adjectives", "connected with X"],
            "-ika": ["agent_nouns", "one who does X"],
            "-tara": ["comparison", "more X"],
            "-tama": ["comparison", "most X"]
        }
        
        # Find ALL existing derivatives
        primary_derivatives = [
            (word, entry) for word, entry in self.generated_dict.items()
            if entry["type"].startswith("derivative_") and 
            entry["type"] not in ["derivative_abstract_nouns", "derivative_comparison"]
        ]
        
        for primary_word, primary_entry in primary_derivatives:
            for suffix, (category, meaning_pattern) in secondary_patterns.items():
                secondary_form = primary_word + suffix.replace("-", "")
                
                if (secondary_form not in self.existing_words and 
                    secondary_form not in self.generated_dict):
                    
                    # Generate meaning
                    secondary_meaning = self.derivational_generator.generate_secondary_derivative(
                        primary_word, suffix, category
                    )
                    
                    entry = {
                        "word": secondary_form,
                        "meaning": self.validator.enhance_meaning(secondary_meaning),
                        "type": f"derivative_{category}",
                        "base": primary_word,
                        "primary_base": primary_entry.get("base", ""),
                        "suffix": suffix,
                        "derivation_level": "secondary",
                        "frequency": primary_entry.get("frequency", 2.0) * 0.8
                    }
                    
                    self.generated_dict[secondary_form] = entry
                    count += 1
        
        return count
    
    def _generate_tertiary_derivatives(self):
        """Generate tertiary derivatives (derivatives of derivatives of derivatives)"""
        count = 0
        
        # Only most productive patterns for tertiary
        tertiary_patterns = {
            "-tā": "state of being X",
            "-ka": "little X"
        }
        
        # Find secondary derivatives
        secondary_derivatives = [
            (word, entry) for word, entry in self.generated_dict.items()
            if entry.get("derivation_level") == "secondary"
        ][:500]  # Limit to avoid explosion
        
        for secondary_word, secondary_entry in secondary_derivatives:
            for suffix, meaning_pattern in tertiary_patterns.items():
                tertiary_form = secondary_word + suffix.replace("-", "")
                
                if (tertiary_form not in self.existing_words and 
                    tertiary_form not in self.generated_dict):
                    
                    # Generate meaning
                    secondary_meaning = secondary_entry["meaning"]
                    tertiary_meaning = meaning_pattern.replace("X", secondary_meaning)
                    
                    entry = {
                        "word": tertiary_form,
                        "meaning": self.validator.enhance_meaning(tertiary_meaning),
                        "type": "derivative_abstract_nouns",
                        "base": secondary_word,
                        "secondary_base": secondary_entry.get("base", ""),
                        "primary_base": secondary_entry.get("primary_base", ""),
                        "suffix": suffix,
                        "derivation_level": "tertiary",
                        "frequency": secondary_entry.get("frequency", 2.0) * 0.7,
                        "rare": True
                    }
                    
                    self.generated_dict[tertiary_form] = entry
                    count += 1
        
        return count
    
    def _generate_complete_technical_vocabulary(self):
        """Generate ALL technical vocabulary"""
        count = 0
        
        # Generate from comprehensive technical vocabulary
        if hasattr(self.kb, 'comprehensive_technical_vocabulary'):
            for field, terms in self.kb.comprehensive_technical_vocabulary.items():
                print(f"   📝 Processing {field} ({len(terms)} terms)...")
                field_count = 0
                
                for term in terms:
                    if term not in self.existing_words and term not in self.generated_dict:
                        # Create technical term entry
                        if term in self.kb.base_meanings:
                            base_meaning = self.kb.base_meanings[term]["primary"]
                            technical_meaning = f"{base_meaning} (technical term in {field})"
                        else:
                            technical_meaning = f"technical term in {field}"
                        
                        entry = {
                            "word": term,
                            "meaning": self.validator.enhance_meaning(technical_meaning),
                            "type": "technical_term",
                            "field": field,
                            "semantic_field": field,
                            "register": "technical",
                            "frequency": 3.0
                        }
                        
                        self.generated_dict[term] = entry
                        count += 1
                        field_count += 1
                        
                        # Generate ALL inflected forms for technical terms
                        tech_forms = self._generate_all_technical_inflections(term, field)
                        count += tech_forms
                        field_count += tech_forms
                
                print(f"      ✓ {field_count} entries for {field}")
        
        self.generation_stats["technical_terms"] = count
        return count
    
    def _generate_all_technical_inflections(self, term, field):
        """Generate ALL inflected forms for technical terms"""
        count = 0
        
        # ALL cases and numbers for technical terms
        all_cases = ["nominative", "accusative", "instrumental", "dative", 
                    "ablative", "genitive", "locative", "vocative"]
        all_numbers = ["singular", "dual", "plural"]
        
        for case in all_cases:
            for number in all_numbers:
                form = self._apply_nominal_morphology(term, case, number)
                
                if (form and form != term and 
                    form not in self.existing_words and 
                    form not in self.generated_dict):
                    
                    case_meaning = self.morphological_generator.case_templates[case]["default"]
                    base_meaning = f"{term} (technical term in {field})"
                    full_meaning = case_meaning.format(base_meaning)
                    
                    entry = {
                        "word": form,
                        "meaning": self.validator.enhance_meaning(full_meaning),
                        "type": "inflected_noun",
                        "base": term,
                        "case": case,
                        "number": number,
                        "field": field,
                        "register": "technical",
                        "frequency": 2.5
                    }
                    
                    self.generated_dict[form] = entry
                    count += 1
        
        return count
    
    def _generate_complete_phrasal_universe(self):
        """Generate ALL phrasal expressions"""
        count = 0
        
        # Process phrasal expressions
        if hasattr(self.kb, 'phrasal_expressions'):
            for phrase, meaning in self.kb.phrasal_expressions.items():
                if phrase not in self.existing_words and phrase not in self.generated_dict:
                    entry = {
                        "word": phrase,
                        "meaning": self.validator.enhance_meaning(meaning),
                        "type": "phrasal_expression",
                        "components": phrase.split("-"),
                        "frequency": 3.5
                    }
                    
                    self.generated_dict[phrase] = entry
                    count += 1
        
        # Process liturgical formulas
        if hasattr(self.kb, 'liturgical_formulas'):
            for formula, meaning in self.kb.liturgical_formulas.items():
                if formula not in self.existing_words and formula not in self.generated_dict:
                    entry = {
                        "word": formula,
                        "meaning": self.validator.enhance_meaning(meaning),
                        "type": "liturgical_formula",
                        "register": "ceremonial",
                        "frequency": 2.5
                    }
                    
                    self.generated_dict[formula] = entry
                    count += 1
        
        self.generation_stats["phrasal_expressions"] = count
        return count
    
    def _generate_complete_numerical_universe(self):
        """Generate ALL numerical expressions"""
        count = 0
        
        # Process complete numerals
        if hasattr(self.kb, 'complete_numerals'):
            for numeral, info in self.kb.complete_numerals.items():
                if numeral not in self.existing_words and numeral not in self.generated_dict:
                    entry = {
                        "word": numeral,
                        "meaning": self.validator.enhance_meaning(info["meaning"]),
                        "type": f"numeral_{info['type']}",
                        "value": info["value"],
                        "numeral_type": info["type"],
                        "frequency": 4.0 if info["value"] <= 10 else 3.0
                    }
                    
                    if "gender" in info:
                        entry["gender"] = info["gender"]
                    
                    self.generated_dict[numeral] = entry
                    count += 1
                    
                    # Generate inflected forms for declinable numerals
                    if info["type"] in ["cardinal", "ordinal"] and info["value"] <= 100:
                        inflected_count = self._generate_numeral_inflections(numeral, info)
                        count += inflected_count
        
        # Generate ALL number + noun combinations
        count += self._generate_all_numerical_compounds()
        
        self.generation_stats["numerals"] = count
        return count
    
    def _generate_all_numerical_compounds(self):
        """Generate ALL number + noun combinations"""
        count = 0
        
        # Get numbers up to 1000
        numbers = []
        if hasattr(self.kb, 'complete_numerals'):
            for numeral, info in self.kb.complete_numerals.items():
                if (info["type"] == "cardinal" and 
                    isinstance(info["value"], int) and 
                    info["value"] <= 1000):
                    numbers.append((numeral, info["value"], info["meaning"]))
        
        # Get countable nouns
        countable_nouns = []
        for word, info in self.kb.base_meanings.items():
            if info.get("semantic_field") not in ["particles", "prefixes", "abstract"]:
                countable_nouns.append(word)
        
        # Common patterns with numbers
        patterns = [
            ("X", "Y", "X Y"),
            ("X", "Y", "Y of X"),
            ("X", "divasa", "X days"),
            ("X", "ratti", "X nights"),
            ("X", "māsa", "X months"),
            ("X", "vassa", "X years"),
            ("X", "vāra", "X times"),
            ("X", "kkhattaṃ", "X times"),
            ("X", "bhāga", "X parts"),
            ("X", "koṭi", "X crores"),
            ("X", "gāthā", "X verses"),
            ("X", "sutta", "X discourses")
        ]
        
        # Generate combinations
        for num_word, num_value, num_meaning in numbers[:50]:  # Limit to first 50 numbers
            for pattern in patterns:
                if pattern[1] == "Y":
                    # General pattern - use countable nouns
                    for noun in countable_nouns[:20]:  # Limit nouns
                        compound = self._apply_compound_sandhi([num_word, noun])
                        meaning = pattern[2].replace("X", num_meaning).replace("Y", self._get_base_meaning(noun))
                        
                        if (compound not in self.existing_words and 
                            compound not in self.generated_dict):
                            
                            entry = {
                                "word": compound,
                                "meaning": self.validator.enhance_meaning(meaning),
                                "type": "numerical_compound",
                                "components": [num_word, noun],
                                "number": num_value,
                                "frequency": 3.0 if num_value <= 10 else 2.5
                            }
                            
                            self.generated_dict[compound] = entry
                            count += 1
                else:
                    # Specific pattern
                    compound = self._apply_compound_sandhi([num_word, pattern[1]])
                    meaning = pattern[2].replace("X", num_meaning)
                    
                    if (compound not in self.existing_words and 
                        compound not in self.generated_dict):
                        
                        entry = {
                            "word": compound,
                            "meaning": self.validator.enhance_meaning(meaning),
                            "type": "numerical_compound",
                            "components": [num_word, pattern[1]],
                            "number": num_value,
                            "pattern": pattern[0] + "+" + pattern[1],
                            "frequency": 3.0 if num_value <= 10 else 2.5
                        }
                        
                        self.generated_dict[compound] = entry
                        count += 1
        
        return count
    
    def _generate_complete_sandhi_universe(self):
        """Generate ALL possible sandhi variants"""
        count = 0
        
        # Phase A: Compound boundary sandhi
        print("   📝 Generating ALL compound boundary sandhi...")
        count += self._generate_all_compound_boundary_sandhi()
        
        # Phase B: Word combination sandhi
        print("   📝 Generating ALL word combination sandhi...")
        count += self._generate_all_word_combination_sandhi()
        
        # Phase C: Internal sandhi variants
        print("   📝 Generating ALL internal sandhi variants...")
        count += self._generate_all_internal_sandhi_variants()
        
        print(f"   ✅ Generated {count} sandhi variants total")
        self.generation_stats["sandhi_variants"] = count
        return count
    
    def _generate_all_compound_boundary_sandhi(self):
        """Generate ALL compound boundary sandhi variants"""
        count = 0
        
        # Get ALL compound entries
        compound_entries = [
            (word, entry) for word, entry in self.generated_dict.items()
            if entry["type"].startswith("compound_") and "components" in entry
        ]
        
        for compound_word, compound_entry in compound_entries:
            components = compound_entry["components"]
            
            if len(components) >= 2:
                # Try alternative sandhi at each boundary
                for i in range(len(components) - 1):
                    first = components[i]
                    second = components[i + 1]
                    
                    # Get ALL possible sandhi alternatives
                    alternatives = self._get_all_sandhi_alternatives(first, second)
                    
                    for alt_sandhi in alternatives:
                        # Reconstruct compound with alternative sandhi
                        new_components = components[:i] + [alt_sandhi] + components[i+2:]
                        variant = "".join(new_components)
                        
                        if (variant != compound_word and 
                            variant not in self.existing_words and 
                            variant not in self.generated_dict):
                            
                            entry = {
                                "word": variant,
                                "meaning": compound_entry["meaning"] + " (alternative sandhi)",
                                "type": "sandhi_variant",
                                "base": compound_word,
                                "components": components,
                                "sandhi_boundary": i,
                                "sandhi_type": "compound_boundary",
                                "frequency": compound_entry.get("frequency", 2.0) * 0.9
                            }
                            
                            self.generated_dict[variant] = entry
                            count += 1
        
        return count
    
    def _generate_all_word_combination_sandhi(self):
        """Generate ALL word combination sandhi"""
        count = 0
        
        # Extended combiners
        common_combiners = {
            "particles": ["ca", "vā", "api", "eva", "iti", "ti", "nu", "kho", "pana", "hi", "tu"],
            "pronouns": ["ayaṃ", "idaṃ", "etaṃ", "taṃ", "yaṃ", "kiṃ", "so", "sā", "te"],
            "negations": ["na", "no", "mā", "natthi"],
            "prefixes": list(self.kb.prefix_meanings.keys())[:20]
        }
        
        # Select high-frequency words
        high_freq_words = [
            word for word, entry in self.generated_dict.items()
            if entry.get("frequency", 0) >= 4.0 and len(word) < 12
        ][:200]  # Increased limit
        
        # Generate ALL combinations
        for category, combiners in common_combiners.items():
            for combiner in combiners:
                for word in high_freq_words:
                    # Try both orders
                    for combo in [(combiner, word), (word, combiner)]:
                        first, second = combo
                        
                        # Apply ALL possible sandhi
                        combined_variants = self._apply_all_sandhi_to_combination(first, second)
                        
                        for combined in combined_variants:
                            if (combined and 
                                combined != first + second and
                                combined not in self.existing_words and 
                                combined not in self.generated_dict and
                                len(combined) > 2):
                                
                                # Generate meaning
                                first_meaning = self._get_word_meaning_for_combination(first)
                                second_meaning = self._get_word_meaning_for_combination(second)
                                
                                combined_meaning = self._compose_combination_meaning(
                                    first_meaning, second_meaning, category
                                )
                                
                                entry = {
                                    "word": combined,
                                    "meaning": self.validator.enhance_meaning(combined_meaning),
                                    "type": "sandhi_variant",
                                    "components": [first, second],
                                    "category": f"{category}_combination",
                                    "sandhi_type": "word_combination",
                                    "frequency": 2.0
                                }
                                
                                self.generated_dict[combined] = entry
                                count += 1
        
        
