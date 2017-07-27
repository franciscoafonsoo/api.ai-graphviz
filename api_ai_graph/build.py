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

        if x.events:
            f.node(x.events[0], label=x.events[0], shape='rect')
            f.node(x.name, label=x.name + '\n' + "in: " + str(x.contextin) + ' \n ' + "out: " + str(x.contextout))
            f.edge(x.events[0], x.name)
        if x.first:
            f.node(x.name, label=x.name + '\n' + "in: " + str(x.contextin) + ' \n ' + "out: " + str(x.contextout))
            f.edge('true', x.name, label=x.usersays[0])
        elif not x.contextin:
            f.node(x.name, label=x.name + ' \n ' + "out: " + str(x.contextout))
            f.edge('true', x.name, label=x.usersays[0])
        else:
            f.node(x.name, label=x.name + '\n' + "in: " + str(x.contextin) + ' \n ' + "out: " + str(x.contextout))

    # compare every intent with every other intent

    for target in lintents:
        for source in lintents:

            # if the first is equal to the second (overwrite equal function at the intent.py)
            if target == source:
                # draw an edge if the user interacts with the api.ai
                if target.fallback:
                    f.edge(source.name, target.name, label='#')
                elif target.events:
                    f.edge(source.name, target.events[0], label='event')
                else:
                    f.edge(source.name, target.name, label=target.usersays[0])

                    # draw an edge if the intent is a intentfallback

    # noinspection PyArgumentList
    # f.render()

    # noinspection PyArgumentList
    f.view()