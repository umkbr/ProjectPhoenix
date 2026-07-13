from phoenix.executor.debloat_executor import DebloatExecutor


def test_execute():

    executor = DebloatExecutor()

    commands = [
        "pm enable com.asus.webstorage",
        "pm enable com.asus.weathertime",
    ]

    result = executor.execute(commands)

    assert result == commands