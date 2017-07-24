# -*- coding: utf-8 -*-
from collections import defaultdict


class Intent:
    def __init__(self, a):
        """ Atributs for the Intent Object. Note: only using relevant atributes to build the graph

        :param a: json.load() from a file containting an intent
        :type a: dict
        """

        self.name = a.get('name')

        self.events = [x.get('name') for x in a.get('events')]

        self.webhook = a.get('webhookUsed')

        self.usercase = str

        # find intents representing the first interaction
        sub = '_WELCOME'
        self.first = True if [s for s in self.events if sub in s] else False

        # find user cases
        sub = '-'
        self.usercase = self.name.partition(sub)[0] if sub in self.name else ''

        self.contextin = sorted(a.get('contexts'))

        self.action = a.get('responses')[0].get('action')

        self.usersays = [x.get('data')[0] for x in a.get('userSays')]

        self.usersays = [x.get('text') if len(x) == 1 else x.get('alias') for x in self.usersays]

        self.contextout = sorted([i.get('name') for i in a.get('responses')[0].get('affectedContexts')
                                  if not i.get('lifespan') == 0])

    def __str__(self):
        """
        String representation of the class
        :rtype: str
        """
        return self.name

    def __eq__(self, o):
        """
        Compares the output context with the input context.

        :type   o:  object
        :rtype   :  bool
        :param  o:  Intent Object
        """
        return self.contextin[:len(o.contextout)] == o.contextout


def search_cases(lintents):
    """
    Find User Cases in the given intents

    :param lintents: a list of intents
    :type lintents: list
    :return: dict with key = usercase name and value = list of intents of usercase
    :rtype: dict
    """

    group = defaultdict(list)

    # dict: {'usercase': list of intents}

    for index, intent in enumerate(lintents):
        if intent.usercase is not '':
            group[intent.usercase].append(intent)
            # if intent.usercase == lintents[index + 1].usercase:
                # group[intent.usercase] = list().append(lintents[index + 1])

    return group