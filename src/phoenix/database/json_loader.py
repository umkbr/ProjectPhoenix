import json


def load(path):

    with open(path, encoding="utf8") as f:

        return json.load(f)