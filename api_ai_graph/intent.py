# !/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import defaultdict
from functools import reduce


class Intent:
    def __init__(self, a):
        """ Atributs for the Intent Object. Note: only using relevant atributes to build the graph

        :param a: json.load() from a file containting an intent
        :type a: dict
        """

        self.name = a.get('name')

        self.events = [x.get('name') for x in a.get('events')]

        self.webhook = a.get('webhookUsed')

        # find intents representing the first interaction
        sub = '_WELCOME'
        self.first = True if [s for s in self.events if sub in s] else False

        self.contextin = sorted(a.get('contexts'))

        self.action = a.get('responses')[0].get('action')

        self.usersays = [x.get('data')[0] for x in a.get('userSays')]

        self.usersays = [x.get('text') if len(x) == 1 else x.get('alias') for x in self.usersays]

        self.contextout = sorted([i.get('name') for i in a.get('responses')[0].get('affectedContexts')
                                  if not i.get('lifespan') == 0])

        # find user cases
        self.usercase = (each for each in self.contextout)

        self.fallback = a.get('fallbackIntent')

    def __str__(self):
        """
        String representation of the class (copy and adapt prints from cli.py)
        :rtype: str
        """
        return self.name

    def __eq__(self, b):
        """
        first: All output contexts from 'b' also appear in 'a'
        second: 'b' user says is not empty OR 'b' is a fallback intent

        first AND second must be true.

        :type   b:  object
        :rtype   :  bool
        :param  b:  Intent Object
        """

        first = self.contextin[:len(b.contextout)] == b.contextout
        second = b.usersays or b.fallback

        return first and second


def search_cases(lintents):
    """
    Find 'User Cases' in the given intents. Returns a dict
    with the following format : {'usercase': list of intents}.
    If the intent doesn't have a usercase, it should be grouped
    in with the 'empty' name

    :param lintents: a list of intents
    :type lintents: list
    :return: defaultdict {'usercase': list of intents}
    :rtype: defaultdict
    """

    group = defaultdict(list)

    for index, intent in enumerate(lintents):
        for context in intent.usercase:
            if intent.usercase is '':
                group['empty'].append(intent)
            else:
                group[context].append(intent)

    return group
