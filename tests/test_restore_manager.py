from phoenix.restore.restore_manager import RestoreManager
from phoenix.backup.backup_manager import BackupManager
from phoenix.history.history_manager import HistoryTransaction
from phoenix.models.execution_result import ExecutionResult


def test_restore_commands(tmp_path):

    backup = BackupManager(
        filename=tmp_path / "backup.json"
    )

    backup.save([
        "com.asus.webstorage",
        "com.asus.weathertime",
    ])

    manager = RestoreManager(backup)

    commands = manager.restore()

    assert len(commands) == 2

    assert commands[0].startswith(
        "pm enable"
    )


def test_restore_commands_from_history_transaction():

    transaction = HistoryTransaction(
        id="TX-20260725-120000",
        results=[
            ExecutionResult(
                package="com.asus.webstorage",
                success=True,
                message="OK",
                command="pm disable-user com.asus.webstorage",
            )
        ],
    )

    manager = RestoreManager(transaction)

    assert manager.restore() == [
        "pm enable com.asus.webstorage"
    ]
