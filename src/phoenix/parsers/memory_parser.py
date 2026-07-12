from phoenix.models.memory_info import MemoryInfo


class MemoryParser:
    def parse(self, text: str) -> MemoryInfo:
        values = {}

        for line in text.splitlines():
            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            value = value.strip().split()[0]

            try:
                values[key] = int(value)
            except ValueError:
                values[key] = 0

        return MemoryInfo(
            total_kb=values.get("MemTotal", 0),
            free_kb=values.get("MemFree", 0),
            available_kb=values.get("MemAvailable", values.get("MemFree", 0)),
            buffers_kb=values.get("Buffers", 0),
            cached_kb=values.get("Cached", 0),
        )