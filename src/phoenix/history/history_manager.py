import json

from pathlib import Path
from datetime import datetime


class HistoryManager:

    def __init__(self, folder="history"):

        self.folder = Path(folder)

        self.folder.mkdir(exist_ok=True)

    def save(self, results):

        tx = datetime.now().strftime(
            "TX-%Y%m%d-%H%M%S"
        )

        file = self.folder / f"{tx}.json"

        with open(file, "w") as f:

            json.dump(results, f, indent=4)

        return tx

    def list(self):

        items = []

        for file in sorted(

            self.folder.glob("TX-*.json"),

            reverse=True,

        ):

            with open(file) as f:

                data = json.load(f)

            items.append(

                {

                    "id": file.stem,

                    "packages": len(data),

                    "success": sum(

                        1

                        for item in data

                        if item["success"]

                    ),

                }

            )

        return items