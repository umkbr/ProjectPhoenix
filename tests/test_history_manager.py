from phoenix.history.transaction_manager import TransactionManager
from phoenix.history.history_manager import HistoryManager
from phoenix.models.execution_result import ExecutionResult


def test_history():

    transaction = TransactionManager("tmp_history")

    transaction.save([
        ExecutionResult(
            package="com.test.app",
            success=True,
            message="OK",
            command="pm disable-user com.test.app",
        )
    ])

    history = HistoryManager("tmp_history")

    items = history.list()

    assert len(items) >= 1

    assert items[0]["packages"] == 1