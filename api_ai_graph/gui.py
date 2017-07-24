import pysettings as conf

import pyforms
from pyforms          import BaseWidget
from pyforms.Controls import ControlDir
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton
# from pyforms.Controls import ControlText

from api_ai_graph.parser    import load_jsons as api_load
from api_ai_graph.build     import build_graph as api_build
from api_ai_graph.intent    import search_cases as api_search


class ApiAI(BaseWidget):

    def __init__(self):
        super(ApiAI, self).__init__('API.AI Graph')

        # Definition of the forms fields
        self._intent_dir     = ControlDir('Intents location', 'path')
        self._load_intents  = ControlButton('Load Intents')
        self._user_cases    = ControlCombo('User Cases')
        self._build_graph   = ControlButton('Show Graph')

        # Define the button action
        self._load_intents.value    = self.__button_load
        self._build_graph.value     = self.__button_build

        # Define the organization of the forms
        self.formset = ['_intent_dir',
                        '_load_intents',
                        ('_user_cases', '_build_graph')
                        ]
        # The ' ' is used to indicate that a empty space should be placed at the bottom of the window
        # If you remove the ' ' the forms will occupy the entire window

    def __button_load(self):
        """_load_intent button action event"""
        allintents = api_search(api_load(self._intent_dir.value))

        for index, elements in enumerate(allintents):
            self._user_cases.add_item(elements, allintents[elements])

    def __button_build(self):
        """_build_graph button action event"""
        api_build(self._user_cases.text, self._user_cases.value)


# Execute the application
if __name__ == "__main__":
    pyforms.start_app(ApiAI)
