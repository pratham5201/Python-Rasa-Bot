from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import difflib
from prepare_data import suggestions_list

class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Provide a list of suggestions
        suggestions = suggestions_list
        dispatcher.utter_message(text="I'm sorry, I couldn't understand your question. Here are some suggestions:")
        dispatcher.utter_message(text="\n".join(suggestions))
        

        return [UserUtteranceReverted()]
    









# dispatcher.utter_message(response="utter_didnt_get_that")
    # dispatcher.utter_message(response="utter_suggestions")0
    # dispatcher.utter_message(response="utter_ask_rephrase")0





# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

