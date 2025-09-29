from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from data.utils.menu_utils import extract_item, MENU_PRICES
from data.utils.num_utils import extract_quantity

class ActionOrderItem(Action):

    def name(self) -> Text:
        return "action_order_food_json"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get("text", "")
        parts = [p.strip() for p in user_message.split(",")]

        items_list = []
        cart_value = 0

        for part in parts:
            quantity = extract_quantity(part)
            item = extract_item(part)

            # Skip if item not recognized or empty
            if not item or item.lower() not in MENU_PRICES:
                continue

            price_per_item = MENU_PRICES.get(item.lower())
            total_item_price = price_per_item * quantity

            items_list.append([item, quantity, price_per_item])
            cart_value += total_item_price

        response = {
            "custom": {
                "items": items_list,
                "cart_value": cart_value
            }
        }

        dispatcher.utter_message(json_message=response)
        return []