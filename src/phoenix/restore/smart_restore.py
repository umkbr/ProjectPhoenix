from phoenix.backup.backup_manager import BackupManager
from phoenix.executor.command_builder import CommandBuilder


class SmartRestore:

    def __init__(self):

        self.backup = BackupManager()
        self.builder = CommandBuilder()

    def restore(self, keyword):

        packages = self.backup.load()

        commands = []

        for package in packages:

            if keyword.lower() in package.lower():

                commands.append(
                    self.builder.enable(package)
                )

        return commands

    def restore_all(self):

        packages = self.backup.load()

        return [
            self.builder.enable(package)
            for package in packages
        ]