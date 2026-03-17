import argparse
from app.core.logger import setup_logger
from app.core.scoring import HealthScorer
from app.integrations.git_client import GitClient

from app.analyzers.repo_analyzer import RepoAnalyzer
from app.analyzers.code_quality import CodeQualityAnalyzer
from app.analyzers.security import SecurityAnalyzer
from app.analyzers.branch_health import BranchHealthAnalyzer

from app.report.generator import ReportGenerator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)

    args = parser.parse_args()

    logger = setup_logger()

    repo = GitClient(args.repo).clone()

    repo_metrics = RepoAnalyzer(repo).analyze()
    code_metrics = CodeQualityAnalyzer(repo).analyze()
    security_metrics = SecurityAnalyzer(repo.working_tree_dir).analyze()
    branch_metrics = BranchHealthAnalyzer(repo).analyze()

    metrics = {
        "code_quality": code_metrics["score"],
        "collaboration": 50,
        "devops": 70,
        "security": security_metrics["score"],
        "branch": branch_metrics["score"],
    }

    result = HealthScorer().calculate_score(metrics)

    report = {
        "repository": args.repo,
        "final_score": result,
    }

    ReportGenerator().generate(report)

    logger.info(f"Health Score: {result['total_score']}")


if __name__ == "__main__":
    main()
