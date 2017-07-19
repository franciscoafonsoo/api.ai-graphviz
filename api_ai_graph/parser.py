# -*- coding: utf-8 -*-
import os
import json
from api_ai_graph import intent


def load_jsons(path: str) -> list:
    """ Converts all JSON's given in path (inside 'intents) to a list of Intent Objects.

    :param path: the path where the intent json's are located
    :return: list of Intent objects.
    """

    data = dict()

    for i, filename in enumerate(os.listdir(path)):
        with open(path + '/' + filename, encoding="utf-8") as data_file:
            data[filename] = json.load(data_file)
    return [intent.Intent(value) for keys, value in data.items()]
