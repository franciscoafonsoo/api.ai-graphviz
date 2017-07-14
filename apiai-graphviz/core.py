# importing correct path under python 3.6
import os
import easygui
from pprint import pprint
__path__ = [os.path.dirname(os.path.abspath(__file__))]

from . import parserIntent
from . import build

if __name__ == '__main__':
    # create the obj for parsing the json's
    load = parserIntent.Load()

    # parse all the json's in given dir
    intents = load.load_jsons(easygui.diropenbox())

    # verificar que contextsin são iguais a contextsout. A relação do grafo vai ser
    # baseado nisso

    l = len(intents.obj)
    for index, i in enumerate(intents.obj):
        pprint(i.name)
        pprint(i.action)
        pprint(i.contextin)
        pprint(i.contextout)

    # build.build_graph(load.data.get('welcome-1-start.json'))