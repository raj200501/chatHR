from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSearchPolicy(Action):
    def name(self) -> Text:
        return "action_search_policy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_query = tracker.latest_message.get('text')
        answer = search_company_policies(user_query)
        dispatcher.utter_message(text=answer)
        return []


def search_company_policies(query):
    # Implement search logic here
    # For simplicity, let's return a placeholder response
    return "Here's the information about that policy..."
