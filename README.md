# 🤖 AI Issue Triage Dashboard

An automated AI-powered system that analyzes GitHub Issues and organizes them by category and priority.

## 🚀 Project Overview

This project automatically analyzes newly created GitHub Issues using Gemini AI.

The workflow is:

GitHub Issue → GitHub Actions → Gemini AI → results.json → Streamlit Dashboard

The system extracts:
- Issue summary
- Category
- Priority
- Suggested action

## ✨ Features

- Automatic GitHub Issue detection
- AI-powered issue analysis
- Issue categorization
- Priority classification
- Streamlit monitoring dashboard
- Filters for priority and category
- Automated result storage
- GitHub Actions workflow

## 🛠️ Technologies Used

- Python
- Google Gemini AI
- GitHub Actions
- Streamlit
- Pandas
- GitHub Issues

## 📊 Dashboard

Live Dashboard:

https://ai-issue-triage-bhairavi.streamlit.app/

## ⚙️ How It Works

1. A new GitHub Issue is created.
2. GitHub Actions automatically starts the workflow.
3. Gemini AI analyzes the issue.
4. The analysis is saved in `results.json`.
5. Streamlit displays the analyzed issues on the dashboard.

## 📁 Project Structure

```text
ai-issue-triage/
│
├── .github/
│   └── workflows/
│       └── triage.yml
│
├── dashboard.py
├── triage.py
├── results.json
├── requirements.txt
├── .gitignore
└── README.md
▶️ Run Locally

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run dashboard.py
👥 Author
Bhairavi Pawar