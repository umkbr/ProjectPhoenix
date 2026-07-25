from phoenix.adb.adb_executor import ADBExecutor


class FakeADB:

    def run(self, *args):

        class Result:
            returncode = 0
            stdout = "Package disabled"
            stderr = ""

        assert args == (
            "shell",
            "pm disable-user --user 0 com.example.app",
        )
        return Result()


def test_execute_uses_adb_client_backend():

    executor = ADBExecutor(adb_client=FakeADB())

    result = executor.execute(
        "pm disable-user --user 0 com.example.app"
    )

    assert result.package == "com.example.app"
    assert result.success is True
    assert result.message == "Package disabled"
