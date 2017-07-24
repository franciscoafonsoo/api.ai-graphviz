import pysettings as conf

conf.PYFORMS_MATPLOTLIB_ENABLED = False
conf.PYFORMS_WEB_ENABLED = False
conf.PYFORMS_GL_ENABLED = False
conf.PYFORMS_VISVIS_ENABLED = False

import pyforms

from pyforms          import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlDir
from api_ai_graph.parser import load_jsons as load


class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1,self).__init__('API.AI Graph')

        # Definition of the forms fields
        self._intentfolder  = ControlDir('Intents location', 'path')
        self._button        = ControlButton('Load Intents')

        # Define the button action
        self._button.value = self.__buttonLoad

        # Define the organization of the forms
        self.formset = ['_intentfolder',
                        '_button',
                        ' ']
        # The ' ' is used to indicate that a empty space should be placed at the bottom of the window
        # If you remove the ' ' the forms will occupy the entire window

    def __buttonLoad(self):
        """Button action event"""
        intents = load(self._intentfolder.value)

# Execute the application
if __name__ == "__main__":
    pyforms.start_app(SimpleExample1)
