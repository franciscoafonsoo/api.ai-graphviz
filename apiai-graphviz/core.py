# -*- coding: utf-8 -*-
import os
import easygui
from pprint import pprint
__path__ = [os.path.dirname(os.path.abspath(__file__))]

# local imports
from . import parserIntent
from . import build

if __name__ == '__main__':
    # create the obj for parsing the json's
    load = parserIntent

    # parse all the json's in given dir
    intents = load.load_jsons(easygui.diropenbox())

    # verificar que contextsin são iguais a contextsout. A relação do grafo vai ser
    # baseado nisso

    l = len(intents)
    for index, i in enumerate(intents):
        pprint(i.name)
        pprint(i.usersays)
        pprint(i.action)
        pprint(i.contextin)
        pprint(i.contextout)

    # build.build_graph(load.data.get('welcome-1-start.json'))