import json
from pathlib import Path
from datetime import datetime


class TransactionManager:

    def __init__(self, folder="history"):

        self.folder = Path(folder)
        self.folder.mkdir(exist_ok=True)

    def create_id(self):

        now = datetime.now()

        return now.strftime(
            "TX-%Y%m%d-%H%M%S"
        )

    def save(self, results):

        tx = self.create_id()

        filename = self.folder / f"{tx}.json"

        data = []

        for item in results:

            data.append(
                {
                    "package": item.package,
                    "command": item.command,
                    "success": item.success,
                    "message": item.message,
                }
            )

        with open(filename, "w") as f:

            json.dump(
                data,
                f,
                indent=4,
            )

        return tx