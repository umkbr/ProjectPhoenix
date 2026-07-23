import subprocess

from phoenix.models.execution_result import ExecutionResult


class ADBExecutor:

    def execute(self, command):

        result = subprocess.run(
            ["adb", "shell"] + command.split(),
            capture_output=True,
            text=True,
        )

        return ExecutionResult(
            package=command.split()[-1],
            success=result.returncode == 0,
            message=result.stdout.strip()
            if result.stdout
            else result.stderr.strip(),
            command=command,
        )