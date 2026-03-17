import os

class SecurityAnalyzer:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def analyze(self):
        suspicious = []

        for root, _, files in os.walk(self.repo_path):
            for f in files:
                if "key" in f.lower() or "secret" in f.lower():
                    suspicious.append(f)

        score = max(0, 100 - len(suspicious) * 10)

        return {
            "suspicious_files": suspicious,
            "score": score,
        }
