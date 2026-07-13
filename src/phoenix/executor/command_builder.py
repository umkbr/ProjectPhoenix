class CommandBuilder:

    def disable(
        self,
        package: str,
    ) -> str:

        return (
            f"adb shell pm disable-user {package}"
        )

    def uninstall(
        self,
        package: str,
    ) -> str:

        return (
            f"adb shell pm uninstall --user 0 {package}"
        )