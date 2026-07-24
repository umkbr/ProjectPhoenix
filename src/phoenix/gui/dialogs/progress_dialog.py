from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QProgressBar,
)


class ProgressDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Executing")
        self.setFixedSize(350, 100)

        layout = QVBoxLayout(self)

        self.label = QLabel("Executing commands...")

        self.progress = QProgressBar()
        self.progress.setRange(0, 0)

        layout.addWidget(self.label)
        layout.addWidget(self.progress)

    def finish(self):

        self.progress.setRange(0, 100)
        self.progress.setValue(100)
        self.label.setText("Completed")