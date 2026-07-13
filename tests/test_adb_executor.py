from phoenix.executor.adb_executor import ADBExecutor


class FakeADB:

    def shell(self, command):

        return command


def test_run():

    executor = ADBExecutor()

    executor.adb = FakeADB()

    result = executor.run(
        "pm disable-user --user 0 test.app"
    )

    assert result == (
        "pm disable-user --user 0 test.app"
    )


def test_run_many():

    executor = ADBExecutor()

    executor.adb = FakeADB()

    commands = [
        "one",
        "two",
        "three",
    ]

    result = executor.run_many(commands)

    assert result == commands