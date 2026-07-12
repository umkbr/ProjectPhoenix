from dataclasses import dataclass


@dataclass
class Recommendation:
    title: str
    description: str
    severity: str

    action: str
    category: str = "general"