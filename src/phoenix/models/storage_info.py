from dataclasses import dataclass


@dataclass(slots=True)
class StorageInfo:
    filesystem: str
    total_kb: int
    used_kb: int
    available_kb: int
    usage_percent: int