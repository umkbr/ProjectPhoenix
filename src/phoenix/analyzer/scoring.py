class PhoenixScore:

    def calculate(self, report):

        score = 100

        score -= len(report.recommendations) * 2

        battery = report.battery.level

        if battery < 80:
            score -= 5

        return max(score, 0)