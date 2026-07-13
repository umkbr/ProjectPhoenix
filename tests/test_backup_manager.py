from phoenix.backup.backup_manager import BackupManager


def test_backup_save_load(tmp_path):

    manager = BackupManager(
        filename=tmp_path / "backup.json"
    )

    packages = [
        "com.asus.webstorage",
        "com.asus.weathertime",
    ]

    manager.save(packages)

    restored = manager.load()

    assert restored == packages