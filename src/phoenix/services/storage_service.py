from pathlib import Path

from phoenix.parsers.storage_parser import StorageParser


class StorageService:

    def read(self):

        text = Path("resources/storage.txt").read_text(
            encoding="utf-8"
        )

        parser = StorageParser()

        return parser.parse(text)