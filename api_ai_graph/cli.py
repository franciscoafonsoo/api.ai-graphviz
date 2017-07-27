# !/usr/bin/python3
# -*- coding: utf-8 -*-
from pprint import pprint
from api_ai_graph.parser import load_jsons   as load
from api_ai_graph.build import build_graph  as build
from api_ai_graph.intent import search_cases as search

from pysettings import conf

if __name__ == '__main__':

	print('Welcome.\n\nPlease select the "intent" folder from the zip exported from API.AI.\r\n')

	# parse all the json's in given dir to a list of Intent objects (api_ai_graphs.intent)
	if not conf.DEFAULT_INTENTS_PATH:
		raise Exception("Please define an intents path in the user_settings.py file")

	intents = load(conf.DEFAULT_INTENTS_PATH)

	l = len(intents)
	for index, i in enumerate(intents):
		# should be in __str__() function. for now its ok here.

		print(type(i.usercase))

		print('Name: ' + str(i))
		print('User Says: ' + ' | '.join(i.usersays))
		print('Context in: ' + ' | '.join(i.contextin))
		print('Context out: ' + ' | '.join(i.contextout))
		print('Action: ' + str(i.action))
		print('Events: ' + ''.join(i.events))
		print('fallback: ' + str(i.fallback))
	#  print('User Case: ' + i.usercase + '\n')

	# search user cases
	test = search(intents)

	# printing the dict by user cases
	pprint(test)

	print('User Cases found:')
	for index, elements in enumerate(test):
		print(elements)

	case = 'signup-followup'

	# render the graphs based on a user case
	build(case, test[case])
