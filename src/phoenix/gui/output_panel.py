from PySide6.QtWidgets import QTextEdit


class OutputPanel(QTextEdit):

    def __init__(self):

        super().__init__()

        self.setReadOnly(True)

    def show_text(self, title, lines):

        self.clear()

        self.append(title)
        self.append("=" * len(title))
        self.append("")

        if isinstance(lines, list):

            for line in lines:
                self.append(line)

        else:

            self.append(str(lines))