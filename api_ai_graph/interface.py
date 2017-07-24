import pysettings as conf
import pyforms

from pyforms          import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlDir
from pyforms.Controls import ControlCombo
from api_ai_graph.parser import load_jsons as api_load
from api_ai_graph.intent import search_cases as api_search
from api_ai_graph.build import build_graph as api_build


class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1,self).__init__('API.AI Graph')

        # Definition of the forms fields
        self._intentfolder  = ControlDir('  Intents location', 'path')
        self._load          = ControlButton('Load Intents')
        self._usercases     = ControlCombo('  User Cases')
        self._build         = ControlButton('Show Graph')

        # Define the button action
        self._load.value = self.__buttonLoad
        self._build.value = self._buttonBuild

        # Define the organization of the forms
        self.formset = ['_intentfolder',
                        '_load',
                        ('_usercases', '_build')
                        ]
        # The ' ' is used to indicate that a empty space should be placed at the bottom of the window
        # If you remove the ' ' the forms will occupy the entire window

    def __buttonLoad(self):
        """Button action event"""
        allintents = api_search(api_load(self._intentfolder.value))

        for index, elements in enumerate(allintents):
            self._usercases.add_item(elements, allintents[elements])

    def _buttonBuild(self):
        """Button action event"""
        api_build(self._usercases.name, self._usercases.value)


# Execute the application
if __name__ == "__main__":
    pyforms.start_app(SimpleExample1)
