from phoenix.executor.debloat_executor import DebloatExecutor


def test_execute():

    executor = DebloatExecutor()

    commands = [
        "pm enable com.asus.webstorage",
        "pm enable com.asus.weathertime",
    ]

    result = executor.execute(commands)

    assert len(result) == 2

    assert result[0].command == commands[0]
    assert result[1].command == commands[1]