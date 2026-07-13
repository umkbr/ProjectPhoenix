from dataclasses import dataclass


@dataclass
class AppAdvice:

    package: str

    name: str

    recommendation: str

    reason: str

    priority: int