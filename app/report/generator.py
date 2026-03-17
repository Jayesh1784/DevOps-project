import json

class ReportGenerator:
    def generate(self, data, filename="report.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print("Report saved:", filename)
