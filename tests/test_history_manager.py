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


def test_load_returns_transaction_results(tmp_path):

    transaction = TransactionManager(tmp_path)
    tx_id = transaction.save([
        ExecutionResult(
            package="com.test.app",
            success=True,
            message="OK",
            command="pm disable-user com.test.app",
        )
    ])

    history = HistoryManager(tmp_path)
    loaded = history.load(tx_id)

    assert loaded.id == tx_id
    assert loaded.results[0].package == "com.test.app"
