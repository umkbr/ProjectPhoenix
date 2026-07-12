from phoenix.models.recommendation import Recommendation


class RecoveryAnalyzer:

    def analyze(self, report):

        recommendations = []

        # Storage
        for storage in report.storage:

            if storage.filesystem == "/data":

                if storage.usage_percent >= 90:

                    recommendations.append(
                        Recommendation(
                            "Storage hampir penuh",
                            "Hapus aplikasi atau file yang tidak digunakan.",
                            "warning",
                        )
                    )

        # RAM
        if report.memory.free_kb < 200000:

            recommendations.append(
                Recommendation(
                    "RAM rendah",
                    "Tutup aplikasi yang berjalan di latar belakang.",
                    "warning",
                )
            )

        # Battery
        if report.battery.temperature >= 45:

            recommendations.append(
                Recommendation(
                    "Baterai panas",
                    "Periksa aplikasi yang menggunakan CPU secara berlebihan.",
                    "critical",
                )
            )

        return recommendations