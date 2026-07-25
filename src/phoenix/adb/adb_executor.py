from phoenix.core.adb_client import ADBClient
from phoenix.models.execution_result import ExecutionResult


class ADBExecutor:

    def __init__(self, adb_client=None):

        self.adb = adb_client or ADBClient()

    def execute(self, command):

        result = self.adb.run("shell", command)

        return ExecutionResult(
            package=command.split()[-1],
            success=result.returncode == 0,
            message=result.stdout.strip()
            if result.stdout
            else result.stderr.strip(),
            command=command,
        )
