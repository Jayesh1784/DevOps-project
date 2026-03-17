class HealthScorer:
    def __init__(self):
        self.weights = {
            "code_quality": 0.25,
            "collaboration": 0.25,
            "devops": 0.2,
            "security": 0.2,
            "branch": 0.1,
        }

    def calculate_score(self, metrics):
        total_score = 0
        for key, weight in self.weights.items():
            total_score += metrics.get(key, 0) * weight

        return {
            "total_score": round(total_score, 2),
            "breakdown": metrics,
        }
