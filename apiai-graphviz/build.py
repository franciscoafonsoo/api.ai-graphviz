# -*- coding: utf-8 -*-
from graphviz import Digraph


def build_graph(cenas):
    f = Digraph('teste', filename='cenas.gv')
    f.attr(rankdir='LR', size='8,5')

    f.node('true', label='True', shape='doublecircle')

    f.view()

def jantar():
    e = Digraph('teste', filename='telma.gv')
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

    e.view()
