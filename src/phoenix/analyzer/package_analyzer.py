from phoenix.database.package_database import PackageDatabase
from phoenix.models.recommendation import Recommendation


class PackageAnalyzer:

    def __init__(self):
        self.db = PackageDatabase()

    def analyze(self, packages):

        recommendations = []

        for package in packages:

            app = self.db.find(package)

            if app and app["safe_disable"]:

                recommendations.append(
                    Recommendation(
                        title=f"Disable {app['name']}",
                        description=app.get(
                            "reason",
                            "Known ASUS application"
                        ),
                        severity="medium",
                        action="disable",
                        category="package",
                    )
                )

        return recommendations