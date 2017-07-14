# -*- coding: utf-8 -*-
import os
import json
__path__ = [os.path.dirname(os.path.abspath(__file__))]

# local imports
from . import intent

'''
Module Load:

    data: dictionario dos ficheiros json
    obj: lista de objectos do tipo "Intent"
    relativepath: (uso numa proxima iteracao): verificar se o path "intents" existe
    ralativefile: (uso numa proxima iteracao): verificar se os jsons sao do formato esperado

    Module responsable for loading the intent folder
    
    note:   json.load   - loads a file
            json.loads  - loads a string
'''


def load_jsons(path: str) -> list:
    data = dict()

    for i, filename in enumerate(os.listdir(path)):
        with open(path + '/' + filename, encoding="utf-8") as data_file:
            data[filename] = json.load(data_file)
    return [intent.Intent(value) for keys, value in data.items()]
