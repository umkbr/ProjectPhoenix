from phoenix.executor.command_builder import CommandBuilder
from phoenix.adb.adb_executor import ADBExecutor


class DebloatExecutor:

    def __init__(self):

        self.builder = CommandBuilder()
        self.executor = ADBExecutor()

    def disable(self, package):

        return self.builder.disable(package)

    def enable(self, package):

        return self.builder.enable(package)

    def dry_run(self, package):

        return self.disable(package)

    def execute(self, commands):

        results = []

        for command in commands:

            results.append(
                self.executor.execute(command)
            )

        return results