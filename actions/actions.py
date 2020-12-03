# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import pandas as pd

csdl = pd.read_excel("actions/csdl.xls", header=1)
csdl['name'] = csdl["Họ"] + ' ' + csdl['Đệm'] + ' ' + csdl["Tên"]
print(csdl.head())
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionMssv(Action):

    def name(self) -> Text:
        return "action_mssv"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = Tracker.get_slot('name')
        dob = Tracker.get_slot('dob')
        # preprocess name
        # preprocess dob
        d, m, y = dob.split('-')
        dob_tst = pd.Timestamp(int(y), int(m), int(d), 0)
        # logic -> find ans
        is_name = csdl['name'] == name
        is_dob = csdl['Ngày sinh'] == dob_tst
        id_mssv = csdl[is_name & is_dob]["MSSV"][0]
        # final
        message = "Mã số sinh viên của bạn là {}".format(id_mssv)

        dispatcher.utter_message(text=message)
        return []


class ACtionMsl(Action):

    def name(self) -> Text:
        return "action_msl"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = Tracker.get_slot('name')
        dob = Tracker.get_slot('dob')
        # preprocess name

        # preprocess dob
        d, m, y = dob.split('-')
        dob_tst = pd.Timestamp(int(y), int(m), int(d), 0)
        # logic -> find ans
        is_name = csdl['name'] == name
        is_dob = csdl['Ngày sinh'] == dob_tst
        id_mssv = csdl[is_name & is_dob]["Lớp"][0]
        # final
        message = "Mã số lớp của bạn là {}".format(id_mssv)

        dispatcher.utter_message(text=message)

        return []

class ACtionHi(Action):

    def name(self) -> Text:
        return "action_hi"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Đmm")

        return []
