from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionOrderFoodJson(Action):

    def name(self) -> Text:
        return "action_order_food_json"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get slot values
        item = tracker.get_slot("item") or "dosa"
        quantity = tracker.get_slot("quantity") or 1

        # Simple price calculation
        price_per_item = 50
        total_cost = int(quantity) * price_per_item

        response = {
            "items": [item, int(quantity), total_cost]
        }

        dispatcher.utter_message(json_message=response)
        return []