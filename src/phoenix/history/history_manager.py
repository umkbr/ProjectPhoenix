import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from phoenix.models.execution_result import ExecutionResult


@dataclass
class HistoryTransaction:
    id: str
    results: list[ExecutionResult]


class HistoryManager:

    def __init__(self, folder="history"):

        self.folder = Path(folder)

        self.folder.mkdir(exist_ok=True)

    def save(self, results):

        tx = datetime.now().strftime(
            "TX-%Y%m%d-%H%M%S"
        )

        file = self.folder / f"{tx}.json"

        data = [
            {
                "package": item.package,
                "command": item.command,
                "success": item.success,
                "message": item.message,
            }
            for item in results
        ]

        with open(file, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=4)

        return tx

    def list(self):

        items = []

        for file in sorted(

            self.folder.glob("TX-*.json"),

            reverse=True,

        ):

            with open(file, encoding="utf-8") as handle:
                data = json.load(handle)

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

    def load(self, transaction_id):

        file = self.folder / f"{transaction_id}.json"

        if not file.is_file():
            return None

        with open(file, encoding="utf-8") as handle:
            data = json.load(handle)

        results = [
            ExecutionResult(
                package=item["package"],
                command=item["command"],
                success=item["success"],
                message=item["message"],
            )
            for item in data
        ]

        return HistoryTransaction(
            id=transaction_id,
            results=results,
        )
