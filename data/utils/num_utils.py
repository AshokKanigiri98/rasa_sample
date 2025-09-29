import re
from thefuzz import process

NUMBER_SYNONYMS = {
    1: ["one", "ek", "oru", "onnu", "ondhu", "onrai", "okati", "okka"],
    2: ["two", "do", "rendu", "rendhu", "irandu", "randu", "rendo", "rendoo"],
    3: ["three", "teen", "moodu", "mooru", "moondru", "moodu", "moodu"],
    4: ["four", "char", "naalu", "naal", "nalu", "naangu", "nalugu", "nalugu"],
    5: ["five", "panch", "aidu", "ainthu", "anju", "aidu", "aidhu"],
    6: ["six", "chha", "aaru", "aaru", "aaru", "aaru", "aaru"],
    7: ["seven", "saat", "yedu", "elu", "ezhu", "yedu", "yedhu"],
    8: ["eight", "aath", "entu", "yettu", "ettu", "ettu", "aythu"],
    9: ["nine", "nau", "thommudu", "ondu", "onbhu", "thommudu", "tomudu"],
    10: ["ten", "dus", "padi", "pathu", "padi", "pathu", "padiyu"],
    11: ["eleven", "gyaarah", "pathinonnu", "panoh"],
    12: ["twelve", "baarah", "panthirudu", "panniudu"],
    13: ["thirteen", "terah", "muppudu", "muppadu"],
    14: ["fourteen", "chaudah", "naalpadhu", "nalpadu"],
    15: ["fifteen", "pandrah", "aidupadhu", "aidupadu"],
    16: ["sixteen", "solah", "aarupadhu", "aarupadu"],
    17: ["seventeen", "satrah", "yedupadhu", "yedupadu"],
    18: ["eighteen", "atharah", "yetupadhu", "yetupadu"],
    19: ["nineteen", "unnis", "onbudu", "onbadu"],
    20: ["twenty", "bees", "irupadhu", "irupadu", "irupaduu"]
}

# Fuzzy match quantity words
def extract_quantity(text: str) -> int:
    digits = re.findall(r'\d+', text)
    if digits:
        return int(digits[0])

    text_tokens = text.lower().split()
    for token in text_tokens:
        best_match = None
        highest_score = 0
        for number, words in NUMBER_SYNONYMS.items():
            match, score = process.extractOne(token, words)
            if score > highest_score:
                best_match = number
                highest_score = score
                print(highest_score)
        if highest_score >= 75:  # threshold for matching
            return best_match
    return 1  # default quantity

