from fastapi import FastAPI, UploadFile, File, Body
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import git
import shutil

from backend.ai_engine import analyze_code

app = FastAPI()

# Enable CORS so frontend can call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
TEMP_REPO = "temp_repo"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------------------
# Upload a single file and generate docs
# -----------------------------------------

@app.post("/upload")
async def upload_code(file: UploadFile = File(...)):

    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    code_text = content.decode("utf-8", errors="ignore")

    # Send code to AI
    ai_result = analyze_code(code_text)

    output_file = f"{OUTPUT_FOLDER}/documentation.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ai_result)

    return {
        "filename": file.filename,
        "documentation_file": output_file,
        "ai_analysis": ai_result
    }


# -----------------------------------------
# Download generated documentation
# -----------------------------------------

@app.get("/download")
def download_documentation():

    file_path = f"{OUTPUT_FOLDER}/documentation.md"

    return FileResponse(
        path=file_path,
        filename="documentation.md",
        media_type="text/markdown"
    )


# -----------------------------------------
# Analyze entire GitHub repository
# -----------------------------------------

@app.post("/analyze-repo")
def analyze_repo(repo_url: str = Body(...)):

    # Remove old repo if exists
    if os.path.exists(TEMP_REPO):
        shutil.rmtree(TEMP_REPO)

    # Clone repo
    git.Repo.clone_from(repo_url, TEMP_REPO)

    combined_code = ""

    # Read all python files
    for root, dirs, files in os.walk(TEMP_REPO):
        for file in files:

            if file.endswith(".py"):

                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    combined_code += f"\n\n# FILE: {file}\n"
                    combined_code += f.read()

    # Send all code to AI
    documentation = analyze_code(combined_code)

    output_file = f"{OUTPUT_FOLDER}/repo_documentation.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(documentation)

    return {
        "documentation": documentation,
        "file": output_file
    }