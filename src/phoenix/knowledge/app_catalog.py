import json
from pathlib import Path


class AppCatalog:

    def __init__(self):

        self.database = (
            Path(__file__)
            .resolve()
            .parents[3]
            / "database"
            / "apps"
        )

    def load(self):

        apps = []

        for file in self.database.glob("*.json"):

            with open(file, encoding="utf-8") as f:

                data = json.load(f)

                if isinstance(data, list):
                    apps.extend(data)

                elif isinstance(data, dict):
                    apps.append(data)

        return apps