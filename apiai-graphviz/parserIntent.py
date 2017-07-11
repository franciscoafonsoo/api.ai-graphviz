# -*- coding: utf-8 -*-
import os

__path__ = [os.path.dirname(os.path.abspath(__file__))]

import json
from pathlib import Path
from . import intent

'''
Class Load:

    data: dictionario dos ficheiros json
    obj: lista de objectos do tipo "Intent"
    relativepath: (uso numa proxima iteracao): verificar se o path "intents" existe
    ralativefile: (uso numa proxima iteracao): verificar se os jsons sao do formato esperado

    Classe responsavel por carregar a pasta intent
    
    nota:   json.load   - loads a file
            json.loads  - loads a string
'''


class Load:
    def __init__(self):
        self.data = dict()
        self.obj = list()
        self.relativepath = Path('./aquamote/intents')
        self.relativefile = dict()

    '''
    load_jsons
    
    Carregar os vários ficheiros para memória
    '''

    def load_jsons(self, path):
        for i, filename in enumerate(os.listdir(path)):
            with open('./aquamote/intents/' + filename, encoding="utf-8") as data_file:
                self.data[filename] = json.load(data_file)
        self.load_objs()

    '''
    load_objs
    
    Carregar a lista de ficherios para objectos do tipo Intent
    '''
    def load_objs(self):
        for key, value in self.data.items():
            self.obj.append(
                intent.Intent(value['name'],
                              value['contexts'],
                              value['responses'],
                              value['events'],
                              ))
