from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re

NUMBER_SYNONYMS = {
    1: ["one", "oru", "ek"],
    2: ["two", "rendu", "do"],
    3: ["three", "moodu", "teen"],
    4: ["four", "naalu", "char"],
    5: ["five", "aidu", "panch"],
}

def extract_quantity(text: str) -> int:
    digits = re.findall(r'\d+', text)
    if digits:
        return int(digits[0])
    text_lower = text.lower()
    for number, words in NUMBER_SYNONYMS.items():
        for word in words:
            if word in text_lower:
                return number
    return 1

def extract_item(text: str) -> str:
    menu_items = ["dosa", "idly", "vada", "upma"]
    text_lower = text.lower()
    for item in menu_items:
        if item in text_lower:
            return item
    return "item"

class ActionOrderItem(Action):

    def name(self) -> Text:
        return "action_order_food_json"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get("text", "")
        quantity = extract_quantity(user_message)
        item = extract_item(user_message)
        price_per_item = 50

        response = {
            "recipient_id": tracker.sender_id,
            "custom": {
                "items": [item, quantity, price_per_item]
            }
        }

        dispatcher.utter_message(json_message=response)
        return []
