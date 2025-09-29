NUMBER_SYNONYMS = {
    1: ["one", "oru", "ek"],
    2: ["two", "rendu", "do"],
    3: ["three", "moodu", "teen"],
    4: ["four", "naalu", "char"],
    5: ["five", "aidu", "paanch"]
}

def extract_quantity(text):
    # first check for digits
    for token in text.split():
        if token.isdigit():
            return int(token)
    # then check for words
    text_lower = text.lower()
    for number, words in NUMBER_SYNONYMS.items():
        for word in words:
            if word in text_lower:
                return number
    # default quantity
    return 1