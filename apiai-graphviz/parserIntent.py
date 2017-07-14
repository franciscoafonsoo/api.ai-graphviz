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
        self.obj = list()
        self.relativepath = Path('./aquamote/intents')
        self.relativefile = dict()

    '''
    load_jsons
    
    Carregar os vários ficheiros para memória
    '''

    def load_jsons(self, path: str) -> object:
        # data is not declared on __init__ because it's a temp dict
        data = dict()

        for i, filename in enumerate(os.listdir(path)):
            with open(path + '/' + filename, encoding="utf-8") as data_file:
                data[filename] = json.load(data_file)
        return self.load_objs(data)

    '''
    load_objs
    
    Carregar a lista de ficherios para objectos do tipo Intent
    '''
    def load_objs(self, data: dict) -> object:

        for key, value in data.items():
            self.obj.append(intent.Intent(value['name'],
                                          value['contexts'],
                                          value['responses'],
                                          value['events']))

        return self.obj
