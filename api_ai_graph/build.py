# -*- coding: utf-8 -*-
from graphviz import Digraph


def build_graph(lintents):
    """
    Build the graph based on a list of Intent Objects (from api_ai_graph.intent)

    :type lintents: list
    :param lintents: list of all intents loaded
    """

    remaining = lintents
    f = Digraph('intents', filename='graphs/intents')
    f.attr(rankdir='LR', size='8,5')
    f.node('true', label='True', shape='doublecircle')

    # first intent

    for x in lintents:
        f.node(x.name, label=' | '.join(x.contextout))
        if x.first:
            f.edge('true', x.name, label=' | '.join(x.usersays))
        elif not x.contextin:
            f.edge('true', x.name, label=' | '.join(x.usersays))
        elif not x.contextin and not x.contextout and x.webhook:
            f.edge('true', x.name, label='action: '.join(x.usersays))
            remaining.remove(x)
            if remaining != lintents:
                print('yay')

    # for x in lintents:
    #    if x.first:
    #        f.node(x.name, label=' | '.join(x.contextout))

    for x in remaining:
        for y in remaining:
            if x == y:
                # edge from y to x, labeled
                f.edge(y.name, x.name, label=' | '.join(x.usersays))

    # noinspection PyArgumentList
    f.render()

    # noinspection PyArgumentList
    # f.view()


def jantar():
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
