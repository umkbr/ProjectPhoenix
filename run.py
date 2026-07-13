from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.report.report_engine import ReportEngine


def main():

    inspection = InspectionEngine().inspect()

    health = HealthEngine().evaluate(
        inspection
    )

    report = ReportEngine().render(
        model=inspection.device.model,
        score=health.score,
        recommendations=[
            r.title
            for r in health.recommendations
        ],
    )

    print(report)


if __name__ == "__main__":
    main()