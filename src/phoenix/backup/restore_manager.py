class RestoreManager:

    def __init__(
        self,
        adb_client,
        backup_manager
    ):
        self.adb = adb_client
        self.backup = backup_manager


    def restore_package(
        self,
        package_name
    ):
        """
        Restore aplikasi yang sebelumnya dihapus/disable
        """

        command = (
            "cmd package install-existing "
            f"{package_name}"
        )

        result = self.adb.shell(command)

        return {
            "package": package_name,
            "status": "success",
            "output": result
        }


    def restore_backup(
        self,
        backup_file
    ):
        """
        Restore seluruh isi backup
        """

        backup_data = (
            self.backup.load_backup(
                backup_file
            )
        )


        restored = []

        for package in backup_data["packages"]:

            result = self.restore_package(
                package["name"]
            )

            restored.append(result)


        return {
            "restored": restored,
            "count": len(restored)
        }