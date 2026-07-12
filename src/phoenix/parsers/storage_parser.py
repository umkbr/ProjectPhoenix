from phoenix.models.storage_info import StorageInfo


class StorageParser:

    @staticmethod
    def _to_kb(value: str) -> int:
        value = value.strip().upper()

        if value.endswith("G"):
            return int(float(value[:-1]) * 1024 * 1024)

        if value.endswith("M"):
            return int(float(value[:-1]) * 1024)

        if value.endswith("K"):
            return int(float(value[:-1]))

        return int(float(value))

    def parse(self, text: str) -> list[StorageInfo]:

        items = []

        lines = text.splitlines()

        for line in lines[1:]:

            if "Permission denied" in line:
                continue

            cols = line.split()

            if len(cols) < 5:
                continue

            try:

                filesystem = cols[0]

                total = self._to_kb(cols[1])
                used = self._to_kb(cols[2])
                available = self._to_kb(cols[3])

                usage = int((used / total) * 100) if total else 0

                items.append(
                    StorageInfo(
                        filesystem=filesystem,
                        total_kb=total,
                        used_kb=used,
                        available_kb=available,
                        usage_percent=usage,
                    )
                )

            except Exception as e:
                print("Parser error:", e)

        return items