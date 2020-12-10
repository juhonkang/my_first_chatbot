# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import pandas as pd
import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

csdl = pd.read_excel("actions/csdl.xls", header=1)
csdl['name'] = csdl["Họ"] + ' ' + csdl['Đệm'] + ' ' + csdl["Tên"]
print(csdl[csdl["name"]=="Hoàng Thị Hảo"])
class ActionMssv(Action):

    def name(self) -> Text:
        return "action_mssv"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        dob = tracker.get_slot('dob')
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


class ActionMsl(Action):

    def name(self) -> Text:
        return "action_msl"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        dob = tracker.get_slot('dob')
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


class ActionHi(Action):

    def name(self) -> Text:
        return "action_greet"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        dob = tracker.get_slot('dob')
        d, m, y = dob.split('-')
        dob_tst = pd.Timestamp(int(y), int(m), int(d), 0)
        # logic -> find ans
        is_name = csdl['name'] == name
        is_dob = csdl['Ngày sinh'] == dob_tst

        gender = csdl[is_name & is_dob]["Gender"][0]
        if gender == "Nam":
            gd = "người con trai"
        else:
            gd = "thánh nữ"

        noi_sinh = csdl[is_name & is_dob]["Nơi sinh"][0]
        a = noi_sinh
        dan_toc = csdl[is_name & is_dob]["Dân tộc"][0]
        if dan_toc != "Kinh":
            a = "dân tộc {}".format(dan_toc)
        hi_list = ["Ui, hot nha,",
                   "Gút chóp, ơ mây zing",
                   "Wow, tuỵt zời"]
        chem_gio_list = [
            ", Viện Công Nghệ Thông tin wel cơm và tui, bé bot được nuôi bằng sữa Quang thọ ở đây để giúp bạn nek",
            ":), wel căm to Viện Công Nghệ Thông Tin, chào e, a đứng đây từ chiều :)"]
        message = "{} {} {} {}".format(random.choice(hi_list), gd, a, random.choice(chem_gio_list))

        dispatcher.utter_message(text=message)
        return []


class XXX(Action):

    def name(self) -> Text:
        return "action_xxx"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        dob = tracker.get_slot('dob')
        # preprocess name

        # preprocess dob
        d, m, y = dob.split('-')
        dob_tst = pd.Timestamp(int(y), int(m), int(d), 0)
        # logic -> find ans
        is_name = csdl['name'] == name
        is_dob = csdl['Ngày sinh'] == dob_tst
        id_mssv = csdl[is_name & is_dob]["Gender"][0]
        # final

        if id_mssv == "Nam":
            dispatcher.utter_message(text="Vào bit.ly với mã số code 2JQu8Pf")

        else:
            dispatcher.utter_message(text="Gọi số này nha 0348259665")

        return []

class ActionFunc(Action):

    def name(self) -> Text:
        return "action_gt_func"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(buttons=[{"payload": "/mssv", "title": "Tìm mã số sinh viên"}, {"payload": "/msl", "title": "Tìm mã số lớp"}, {"payload": "/xxx", "title": "xxx :)"}])

        return []
