from PySide6.QtWidgets import QMessageBox


class ConfirmationDialog:

    @staticmethod
    def confirm(parent, items):

        if not apps:
            QMessageBox.information(
                parent,
                "Debloat",
                "No application selected.",
            )
            return False

        names = []

        for item in items:

            if hasattr(item, "name"):
                names.append(item.name)

            elif hasattr(item, "package"):
                names.append(item.package)

            else:
                names.append(str(item))

        reply = QMessageBox.question(
            parent,
            "Execute Debloat",
            (
                f"The following applications will be disabled:\n\n"
                f"{names}\n\n"
                f"Continue?"
            ),
            QMessageBox.Yes | QMessageBox.No,
        )

        return reply == QMessageBox.Yes