from dataclasses import dataclass


@dataclass(slots=True)
class MemoryInfo:
    total_kb: int
    free_kb: int
    available_kb: int
    buffers_kb: int
    cached_kb: int