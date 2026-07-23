from dataclasses import dataclass


@dataclass
class ExecutionResult:

    package: str

    success: bool

    message: str

    command: str