from thefuzz import process

# Multilingual menu items with common Telugu pronunciations & typos
MENU_SYNONYMS = {
    "dosa": ["dosa", "dosaa", "dose", "dosu", "dossaa", "dosu", "dosey", "dosaa", "dosu"],
    "masala dosa": ["masala dosa", "masala dosaa", "masaala dosa", "masaladosa", "masala dosu", "masala dosaa"],
    "idly": ["idly", "idli", "idlee", "idlyy", "idlii", "idlee"],
    "vada": ["vada", "vadha", "vadda", "vaddu", "vadha", "vadda"],
    "upma": ["upma", "upmaa", "upmaa", "upmu", "upm"]
}

MENU_PRICES = {
    "dosa": 30,
    "idly": 30,
    "vada": 40,
    "upma": 40,
    "masala dosa": 40,
}



# Fuzzy match menu items
def extract_item(text: str) -> str:
    text_tokens = text.lower().split()
    best_item = ""
    highest_score = 0
    MIN_SCORE = 70  # minimum confidence to accept a match

    for token in text_tokens:
        for item, synonyms in MENU_SYNONYMS.items():
            match, score = process.extractOne(token, synonyms)
            if score > highest_score:
                highest_score = score
                best_item = item

    if highest_score < MIN_SCORE:
        return ""  # return empty if no confident match
    return best_item