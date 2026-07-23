from phoenix.history.transaction_manager import TransactionManager
from phoenix.models.execution_result import ExecutionResult


def test_transaction():

    manager = TransactionManager("tmp_history")

    results = [
        ExecutionResult(
            package="com.asus.weather",
            success=True,
            message="OK",
            command="pm disable-user com.asus.weather",
        )
    ]

    tx = manager.save(results)

    assert tx.startswith("TX-")