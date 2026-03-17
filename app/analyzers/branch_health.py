class BranchHealthAnalyzer:
    def __init__(self, repo):
        self.repo = repo

    def analyze(self):
        branches = self.repo.branches
        stale = [b for b in branches if "old" in b.name]

        score = max(0, 100 - len(stale) * 10)

        return {
            "total_branches": len(branches),
            "stale_branches": len(stale),
            "score": score,
        }
