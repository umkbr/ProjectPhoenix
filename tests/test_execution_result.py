from phoenix.models.execution_result import ExecutionResult


def test_execution_result():

    result = ExecutionResult(
        package="com.asus.weathertime",
        success=True,
        message="Success",
        command="pm disable-user --user 0 com.asus.weathertime",
    )

    assert result.success
    assert result.package == "com.asus.weathertime"