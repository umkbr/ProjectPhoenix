from phoenix.executor.command_builder import CommandBuilder


class RestoreManager:

    def __init__(self, backup):

        self.backup = backup
        self.builder = CommandBuilder()

    def restore(self):

        packages = self.backup.load()

        commands = []

        for package in packages:

            commands.append(
                self.builder.enable(package)
            )

        return commands