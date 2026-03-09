import os
import git
from backend.ai_engine import analyze_code


def analyze_github_repo(repo_url):

    repo_path = "temp_repo"

    if os.path.exists(repo_path):
        import shutil
        shutil.rmtree(repo_path)

    git.Repo.clone_from(repo_url, repo_path)

    combined_code = ""

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    combined_code += f"\n# File: {file}\n"
                    combined_code += f.read()

    documentation = analyze_code(combined_code)

    return documentation