import argparse

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.report.report_engine import ReportEngine


def inspect():
    report = InspectionEngine().inspect()
    print(report)


def doctor():
    inspection = InspectionEngine().inspect()
    health = HealthEngine().evaluate(inspection)

    output = ReportEngine().render(
        model=inspection.device.model,
        score=health.score,
        recommendations=[
            r.title
            for r in health.recommendations
        ],
    )

    print(output)


def main():
    parser = argparse.ArgumentParser(
        prog="phoenix",
        description="Project Phoenix Android Inspector"
    )

    parser.add_argument(
        "command",
        choices=[
            "inspect",
            "battery",
            "memory",
            "storage",
            "doctor",
        ]
    )

    args = parser.parse_args()

    if args.command == "inspect":
        inspect()

    elif args.command == "doctor":
        doctor()

    elif args.command == "battery":
        print("Battery module coming soon")

    elif args.command == "memory":
        print("Memory module coming soon")

    elif args.command == "storage":
        print("Storage module coming soon")


if __name__ == "__main__":
    main()