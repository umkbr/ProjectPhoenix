from phoenix.restore.restore_manager import RestoreManager
from phoenix.backup.backup_manager import BackupManager


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