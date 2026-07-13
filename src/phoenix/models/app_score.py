from dataclasses import dataclass


@dataclass
class AppScore:
    name: str
    score: int
    compatible: bool
    reasons: list[str]