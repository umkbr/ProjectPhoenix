from phoenix.models.doctor_report import DoctorReport


class DoctorEngine:

    def diagnose(self, health):

        diagnosis = []

        if health.score >= 90:
            diagnosis.append("Device is in excellent condition.")

        elif health.score >= 75:
            diagnosis.append("Device is healthy but needs minor optimization.")

        elif health.score >= 50:
            diagnosis.append("Device performance is degraded.")

        else:
            diagnosis.append("Device requires immediate maintenance.")

        return DoctorReport(
            health=health,
            diagnosis=diagnosis,
            recommendations=health.recommendations,
            summary=diagnosis[0],
        )