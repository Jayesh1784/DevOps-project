from datetime import datetime

class RepoAnalyzer:
    def __init__(self, repo):
        self.repo = repo

    def analyze(self):
        commits = list(self.repo.iter_commits(max_count=200))

        if not commits:
            return {"score": 0}

        latest = commits[0].committed_datetime
        days = (datetime.now(latest.tzinfo) - latest).days

        score = max(0, 100 - days)

        return {
            "total_commits": len(commits),
            "days_since_last_commit": days,
            "score": score,
        }
