from phoenix.executor.command_builder import CommandBuilder
from phoenix.executor.adb_executor import ADBExecutor
from phoenix.utils.logger import logger


class RestoreManager:

    def __init__(self, backup):

        self.backup = backup
        self.builder = CommandBuilder()
        self.executor = ADBExecutor()

    def restore(self):

        packages = self._packages()

        commands = []

        for package in packages:

            commands.append(
                self.builder.enable(package)
            )

        return commands

    def _packages(self):

        if hasattr(self.backup, "load"):
            packages = self.backup.load()
        else:
            packages = self.backup.results

        return [
            package.package if hasattr(package, "package") else package
            for package in packages
        ]

    def execute(self):

        commands = self.restore()

        try:

            return self.executor.run_many(
                commands
            )

        except Exception as e:

            logger.exception(e)

            raise
