from PySide6.QtWidgets import QMessageBox


class ConfirmationDialog:

    @staticmethod
    def confirm(parent, apps):

        if not apps:
            QMessageBox.information(
                parent,
                "Debloat",
                "No application selected.",
            )
            return False

        names = "\n".join(
            f"• {app.name}"
            for app in apps
        )

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