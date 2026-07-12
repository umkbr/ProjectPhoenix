import json
from pathlib import Path


class DeviceKnowledgeLoader:

    def __init__(self):
        self.base_path = Path("database/devices")

    def load(self, manufacturer: str, model: str):

        manufacturer = manufacturer.lower()

        folder = self.base_path / manufacturer

        if not folder.exists():
            return None

        for file in folder.glob("*.json"):

            with open(file, encoding="utf-8") as f:

                data = json.load(f)

            if data.get("model") == model:

                return data

        return None