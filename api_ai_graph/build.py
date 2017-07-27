# !/usr/bin/python3
# -*- coding: utf-8 -*-
from graphviz import Digraph


def build_graph(usercase, lintents):
    """
    Build the graph based on a list of Intent Objects (from api_ai_graph.intent)

    :type lintents: list
    :type usercase: str
    :param lintents: list of all intents from usercase
    :param usercase: name of the usercase to build
    """

    f = Digraph(usercase, filename='graphs/' + usercase)
    f.attr(rankdir='LR', size='8,5')
    f.node('true', label='True', shape='doublecircle')

    # first intent

    for x in lintents:

        # if the intent has an event, we create a 'rect' shaped node that demostrastes a connection to the server.
        # in later stages, when an intent connects to this intent, we connected to the 'event' intent instead.

        f.node(x.name, label=x.name + '\n' + "in: " + str(x.contextin) + ' \n ' + "out: " + str(x.contextout))

        if x.events:
            f.node(x.events[0], label=x.events[0], shape='rect')
            f.edge(x.events[0], x.name)
        elif x.first:
            f.edge('true', x.name, label=x.usersays[0])
        elif not x.contextin:
            f.node(x.name, label=x.name + ' \n ' + "out: " + str(x.contextout))
            f.edge('true', x.name, label=x.usersays[0])

    # compare every intent with every other intent

    for target in lintents:
        for source in lintents:

            # if the first is equal to the second (overwrite equal function at the intent.py)

            if target == source:
                print('comparar: ' + source.name, target.name)
                # draw an edge if the user interacts with the api.ai
                if target.fallback:
                    f.edge(source.name, target.name, label='#')
                elif target.events and source.webhook:
                    f.edge(source.name, target.events[0], label='event')
                elif target.usersays:
                    f.edge(source.name, target.name, label=target.usersays[0])

    # noinspection PyArgumentList
    # f.render()

    # noinspection PyArgumentList
    f.view()