from pathlib import Path

from phoenix.parsers.memory_parser import MemoryParser


class MemoryService:
    def __init__(self) -> None:
        self.parser = MemoryParser()

    def read(self):
        path = Path("resources/meminfo.txt")

        text = path.read_text(encoding="utf-8")

        return self.parser.parse(text)