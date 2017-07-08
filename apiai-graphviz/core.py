# importing correct path under python 3.6
import os
import pprint as pp
__path__ = [os.path.dirname(os.path.abspath(__file__))]

from . import parserIntent
from . import build

if __name__ == '__main__':
    load = parserIntent.Load()

    load.load_intents('./aquamote/intents')
    pp.pprint(load.data)

    for i in load.intents:
        pp.pprint(i.name)
        pp.pprint(i.contextin)

    build.build_graph(load.data.get('welcome-1-start.json'))