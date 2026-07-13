from dataclasses import dataclass

@dataclass
class DebloatResult:

    package: str

    name: str

    installed: bool

    safe_disable: bool

    priority: int

    recommendation: str