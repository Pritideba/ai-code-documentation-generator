import ollama

def analyze_code(code_text):

    prompt = f"""
You are a software documentation assistant.

Analyze the following code and generate structured documentation.

Provide output in this format:

# Code Documentation

## Overview
Explain what the program does.

## Functions
List each function and describe:
- purpose
- parameters
- return values

## Workflow
Explain how the program works step-by-step.

## Suggestions
Suggest improvements to the code.

Code:
{code_text}
"""

    response = ollama.chat(
        model="deepseek-coder",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]