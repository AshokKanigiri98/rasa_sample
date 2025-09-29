from thefuzz import process

# Multilingual menu items with common Telugu pronunciations & typos
MENU_SYNONYMS = {
    "dosa": ["dosa", "dosaa", "dose", "dosu", "dossaa", "dosu", "dosey", "dosaa", "dosu"],
    "masala dosa": ["masala dosa", "masala dosaa", "masaala dosa", "masaladosa", "masala dosu", "masala dosaa"],
    "idly": ["idly", "idli", "idlee", "idlyy", "idlii", "idlee"],
    "vada": ["vada", "vadha", "vadda", "vaddu", "vadha", "vadda"],
    "upma": ["upma", "upmaa", "upmaa", "upmu", "upm"]
}


# Fuzzy match menu items
def extract_item(text: str) -> str:
    text_tokens = text.lower().split()
    best_item = "item"
    highest_score = 0

    for token in text_tokens:
        for item, synonyms in MENU_SYNONYMS.items():
            match, score = process.extractOne(token, synonyms)
            if score > highest_score:
                highest_score = score
                best_item = item
    return best_item