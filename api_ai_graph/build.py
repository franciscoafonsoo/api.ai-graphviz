# !/usr/bin/python3
# -*- coding: utf-8 -*-
from graphviz import Digraph


def build_graph(usercase, lintents):
    """
    Build the graph based on a list of Intent Objects (from api_ai_graph.intent)

    :type lintents: list
    :type usercase: str
    :param lintents: list of all intents loaded
    :param usercase: name of the usercase to build
    """

    f = Digraph(usercase, filename='graphs/' + usercase)
    f.attr(rankdir='LR', size='8,5')
    f.node('true', label='True', shape='doublecircle')

    # first intent

    remaining = lintents
    for x in lintents:
        f.node(x.name, label=x.name + '\n' + "in: " + str(x.contextin) + ' \n ' + "out: " + str(x.contextout))
        if x.first:
            f.edge('true', x.name, label=x.usersays[0])
        elif not x.contextin:
            f.edge('true', x.name, label=x.usersays[0])
        elif not x.contextin and not x.contextout and x.webhook:
            # this code is not doing anything right now.
            f.edge('true', x.name, label='action: '.join(x.usersays[0]))
            remaining.remove(x)
            if remaining != lintents:
                print('yay')

    # compare every intent with every other intent
    for target in remaining:
        for source in remaining:

            # if the first is equal to the second (overwrite equal function at the intent.py
            if target == source:
                # draw an edge if the user interacts with the api.ai
                if target.usersays:
                    f.edge(source.name, target.name, label=target.usersays[0])
                # draw an edge if the intent is a intentfallback
                if target.fallback:
                    f.edge(source.name, target.name, label='#')

    # noinspection PyArgumentList
    # f.render()

    # noinspection PyArgumentList
    f.view()


def testing_dot():
    """
    Test function, made for previewing how a graphviz module works
    """
    e = Digraph('teste', filename='../graphs/teste.gv')
    e.attr(rankdir='LR', size='8,5')

    e.node('true', label='True', shape='doublecircle')
    e.node('welcome-0-start', label='signup-data | "Welcome"')
    e.node('welcome-1-yes', label='signup-data | "cenas"')

    e.edge('true', 'welcome-0-start', label='signup')
    e.edge('welcome-0-start', 'true', label='cancel')
    e.edge('welcome-0-start', 'true', label='no')
    e.edge('welcome-0-start', 'welcome-0-start', label='!= no, yes')
    e.edge('welcome-0-start', 'welcome-1-yes', label='yes')

    e.edge('telma', 'pizza', label='faz')
    e.edge('pizza', 'jantar', label='para o')
    e.edge('telma', 'chico', label='E manda à merda')
    e.edge('chico', 'chico', label='recur.')

    # noinspection PyArgumentList
    e.view()
