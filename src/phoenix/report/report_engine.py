class ReportEngine:

    def render(
        self,
        model: str,
        score: int,
        recommendations,
    ):

        lines = [
            "========================================",
            "          PROJECT PHOENIX",
            "========================================",
            "",
            f"Device : {model}",
            f"Health Score : {score}",
            "",
            "Recommendations",
            "----------------",
        ]

        for recommendation in recommendations:
            lines.append(f"- {recommendation}")

        return "\n".join(lines)