import json
from pathlib import Path

class AppKnowledgeLoader:

    def __init__(self):

        self.base = Path("database/apps")

    def load_all(self):

        apps = []

        for file in self.base.rglob("*.json"):

            with open(file, encoding="utf8") as f:

                apps.append(json.load(f))

        return apps