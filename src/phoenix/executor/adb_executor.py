from phoenix.core.adb_client import ADBClient


class ADBExecutor:

    def __init__(self):

        self.adb = ADBClient()

    def run(self, command):

        return self.adb.shell(command)

    def run_many(self, commands):

        results = []

        for command in commands:

            results.append(
                self.run(command)
            )

        return results
    