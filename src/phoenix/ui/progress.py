class Progress:

    def show(self, current, total, title):

        print(
            f"[{current}/{total}] {title}"
        )