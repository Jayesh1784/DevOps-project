from git import Repo
import os
import shutil

class GitClient:
    def __init__(self, repo_url, local_path="./repo"):
        self.repo_url = repo_url
        self.local_path = local_path

    def clone(self):
        if os.path.exists(self.local_path):
            shutil.rmtree(self.local_path)

        print("Cloning repository...")
        repo = Repo.clone_from(self.repo_url, self.local_path)
        print("Clone completed")
        return repo
