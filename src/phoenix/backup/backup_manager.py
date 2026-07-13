import json


class BackupManager:

    def __init__(self, filename="backup.json"):

        self.filename = filename

    def save(self, packages):

        with open(self.filename, "w") as f:

            json.dump(packages, f, indent=4)

    def load(self):

        with open(self.filename) as f:

            return json.load(f)