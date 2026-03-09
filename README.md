# 🤖 AI Code Documentation Generator

An AI-powered developer tool that automatically analyzes source code or GitHub repositories and generates structured documentation.

This project uses **FastAPI**, **Ollama (DeepSeek-Coder)**, and a **web-based interface** to help developers quickly understand codebases and generate clear documentation.

---

## 🚀 Features

- 📄 Generate documentation from uploaded code files
- 🌐 Analyze entire GitHub repositories automatically
- 🤖 AI-powered code understanding using **DeepSeek-Coder**
- 📝 Automatic Markdown documentation generation
- 📥 Download generated documentation
- 💻 Simple and clean web interface
- 🔒 Runs locally (no external API required)

---

## 🏗 System Architecture

User (Browser)
│
▼
Frontend (HTML / CSS / JavaScript)
│
▼
FastAPI Backend (Python)
│
▼
Ollama Local AI Model (DeepSeek-Coder)
│
▼
Code Analysis & Documentation Generation
│
▼
Markdown Documentation Output



---

## 📂 Project Structure


ai-code-doc-generator
│
├── backend
│ ├── main.py
│ ├── ai_engine.py
│
├── frontend
│ ├── index.html
│ ├── script.js
│ ├── style.css
│
├── uploads
├── outputs
│
├── requirements.txt
└── README.md



---

## ⚙ Installation

### 1️⃣ Clone the Repository

bash
git clone https://github.com/your-username/ai-code-doc-generator.git
cd ai-code-doc-generator


---


2️⃣ Create a Virtual Environment

python -m venv venv

Activate it:

Windows :   venv\Scripts\activate

Mac/Linux :  source venv/bin/activate


---

3️⃣ Install Dependencies
pip install -r requirements.txt


---

4️⃣ Install Ollama

Download and install:

https://ollama.com

Then install the AI model:  ollama run deepseek-coder


---


5️⃣ Start the Backend Server
uvicorn backend.main:app --reload

Server will run at:   http://127.0.0.1:8000



---

6️⃣ Launch the Frontend

Open:

frontend/index.html (in your browser.)


---

🖥 Usage
📄 Generate Documentation from Code

Upload a Python file

Click Generate Documentation

AI analyzes the code

Documentation is displayed

Download the generated file


---


🌐 Analyze GitHub Repository

Enter a GitHub repository URL

Click Analyze Repository

AI reads the repository code

Documentation is generated automatically



---
Example:

https://github.com/user/project

📊 Example Output
# Code Documentation

## Overview
This application performs satellite image classification using TensorFlow.

## Functions
predict_image()

## Workflow
1. User uploads image
2. Image preprocessing
3. Model prediction
4. Display results

## Suggestions
Improve error handling and logging.


---

🛠 Technologies Used

Python

FastAPI

Ollama

DeepSeek-Coder

HTML / CSS / JavaScript

GitPython

---

🔮 Future Improvements

Support multiple programming languages

Automatic architecture diagram generation

API documentation generation

Docker deployment

Cloud-based AI support

---

📜 License

This project is open source and available under the MIT License.

👨‍💻 Author

Developed by [Pritideba Patra]
