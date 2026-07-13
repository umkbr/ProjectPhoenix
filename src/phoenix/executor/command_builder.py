class CommandBuilder:

    def disable(self, package):

        return (
            f"pm disable-user --user 0 "
            f"{package}"
        )

    def enable(self, package):

        return (
            f"pm enable "
            f"{package}"
        )

    def uninstall(
        self,
        package: str,
    ) -> str:

        return (
            f"pm uninstall --user 0 "
            f"{package}"
        )