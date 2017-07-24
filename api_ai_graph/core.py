# -*- coding: utf-8 -*-
import easygui
from pprint import pprint
from api_ai_graph.parser import load_jsons as load
from api_ai_graph.build import build_graph as build
from api_ai_graph.intent import search_cases as search

if __name__ == '__main__':
    # welcome message
    print('Welcome.\n\nPlease select the "intent" folder from the zip exported from API.AI.\r\n')

    # parse all the json's in given dir to a list of Intent objects (api_ai_graphs.intent)
    intents = load(easygui.diropenbox())

    l = len(intents)
    for index, i in enumerate(intents):
        # should be in __str__() function. for now its ok here.

        print('Name: ' + i.name)
        print('User Says: ' + ' | '.join(i.usersays))
        print('Context in: ' + ' | '.join(i.contextin))
        print('Context out: ' + ' | '.join(i.contextout))
        print('Action: ' + str(i.action))
        print('Events: ' + ''.join(i.events))
        print('User Case: ' + i.usercase + '\n')

    # search user cases
    test = search(intents)

    pprint(test)

    # render the graphs based on the list of intents
    build(test['welcome'])