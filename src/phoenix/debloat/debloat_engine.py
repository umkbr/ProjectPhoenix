from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.executor.debloat_executor import DebloatExecutor


class DebloatEngine:

    def __init__(self):
        self.inventory = InventoryEngine()
        self.executor = DebloatExecutor()

    def removable(self, apps):
        """
        Mengembalikan aplikasi yang aman untuk dinonaktifkan.
        """
        return [
            app
            for app in apps
            if app.safe_disable
        ]

    def recommend(self, apps):
        """
        Alias agar nama method lebih mudah dipahami.
        """
        return self.removable(apps)

    def analyze(self, packages):
        """
        Menganalisis daftar package dan mengembalikan
        aplikasi yang aman untuk dinonaktifkan.
        """
        apps = self.inventory.build(packages)
        return self.removable(apps)

    def commands(self, apps):
        """
        Menghasilkan command disable.
        """
        commands = []

        for app in self.removable(apps):
            commands.append(
                self.executor.disable(app.package)
            )

        return commands