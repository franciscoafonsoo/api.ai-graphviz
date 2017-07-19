# -*- coding: utf-8 -*-
import easygui
from pprint import pprint
from api_ai_graph import parser
from api_ai_graph import build


if __name__ == '__main__':
    # create the obj for parsing the json's

    # parse all the json's in given dir
    intents = parser.load_jsons(easygui.diropenbox())
    # intents = load.load_jsons('./aquamote/intents')

    # verificar que contextsin são iguais a contextsout. A relação do grafo vai ser
    # baseado nisso

    l = len(intents)
    for index, i in enumerate(intents):
        pprint(i.name)
        pprint(i.usersays)
        pprint(i.action)
        pprint(i.contextin)
        pprint(i.contextout)
        pprint(i.events)
        pprint(i.first)

    build.build_graph(intents)

    # build.build_graph(load.data.get('welcome-1-start.json'))
