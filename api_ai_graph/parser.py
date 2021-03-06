# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json
from api_ai_graph.intent import Intent


def load_jsons(path):
    """ Converts all JSON's given in path (inside 'intents) to a list of Intent Objects.

    :param path: intent directory extrated from API.AI
    :type path: str
    :return: list of Intent objects.
    :rtype: list
    """

    data = dict()

    for i, filename in enumerate(os.listdir(path)):
        with open(path + '/' + filename, encoding="utf-8") as data_file:
            data[filename] = json.load(data_file)

    return [Intent(value) for keys, value in data.items()]
