from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from data.utils.menu_utils import extract_item
from data.utils.num_utils import extract_quantity


class ActionOrderItem(Action):

    def name(self) -> Text:
        return "action_order_food_json"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text", "")
        quantity = extract_quantity(user_message)
        item = extract_item(user_message)
        price_per_item = 50  # You can replace this with a dynamic lookup from menu

        response = {
            "recipient_id": tracker.sender_id,
            "custom": {
                "items": [item, quantity, price_per_item]
            }
        }

        dispatcher.utter_message(json_message=response)
        return []
