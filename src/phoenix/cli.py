import argparse

from phoenix.core.inspection_engine import InspectionEngine


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
        engine = InspectionEngine()
        report = engine.inspect()
        print(report)


if __name__ == "__main__":
    main()