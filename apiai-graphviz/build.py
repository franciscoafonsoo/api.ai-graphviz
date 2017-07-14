# -*- coding: utf-8 -*-
from graphviz import Digraph
from . import intent


def build_graph(lintents: list):
    """
    Only building the first intent for now

    :type cenas: intent
    :param cenas:
    :return:
    """
    f = Digraph('intents', filename='graphs/intents')
    f.attr(rankdir='LR', size='8,5')

    # first intent

    f.node('true', label='True', shape='doublecircle')

    for x in lintents:
        f.node(x.name, label=' | '.join(x.contextout))

    # for x in lintents:
    #    if x.first:
    #        f.node(x.name, label=' | '.join(x.contextout))

    for x in lintents:
        for y in lintents:
           if x == y:
                f.edge(x.name, y.name, label=' | '.join(x.usersays))
                # edge from x to y, labeled



    # if cenas.first:
    #    f.node(cenas.name, label=' | '.join(cenas.contextout))
    #    f.edge('true', cenas.name, label=cenas)

    # f.view()
    f.view()
    jantar()
    # noinspection PyArgumentList
    # f.view()


def jantar():
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

    # e.edge('telma', 'pizza', label='faz')
    # e.edge('pizza', 'jantar', label='para o')
    # e.edge('telma', 'chico', label='E manda à merda')
    # e.edge('chico', 'chico', label='recur.')

    # noinspection PyArgumentList
    e.view()
