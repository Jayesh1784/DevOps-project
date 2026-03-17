class CodeQualityAnalyzer:
    def __init__(self, repo):
        self.repo = repo

    def analyze(self):
        commits = list(self.repo.iter_commits(max_count=200))
        weekly = len(commits) / 4 if commits else 0

        score = min(100, weekly * 10)

        return {
            "weekly_commits": weekly,
            "score": score,
        }
