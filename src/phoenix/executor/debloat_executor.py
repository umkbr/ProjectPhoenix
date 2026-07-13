from phoenix.executor.command_builder import CommandBuilder


class DebloatExecutor:

    def __init__(self):

        self.builder = CommandBuilder()

    def disable(self, package):

        return self.builder.disable(package)

    def enable(self, package):

        return self.builder.enable(package)

    def dry_run(self, package):

        return self.disable(package)

    def execute(self, commands):

        return commands