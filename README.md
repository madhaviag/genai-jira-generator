# 🧠 GenAI Requirements to Jira Generator

This app uses OpenAI's GPT-4 to convert unstructured product ideas (emails, messages, requirements) into structured Jira issue suggestions.

## 🚀 Features

- Paste product specs or emails
- Generates a JSON list of Jira tickets
- Streamlit-based UI

## 📦 Installation

```bash
git clone https://github.com/madhaviag/genai-jira-generator.git
cd genai-jira-generator
pip install -r requirements.txt
cp .env.example .env
```

Add your OpenAI key to `.env`.

## ▶️ Run the App

```bash
streamlit run app.py
```

## 🛠️ Future Ideas

- Upload PDFs
- Integrate with Jira API
- Prioritize and auto-assign issues

## 📄 Example Input

> We need to fix the login bug on mobile and create a dashboard for analytics.

## 📤 Output

```json
[
  {
    "summary": "Fix mobile login bug",
    "description": "Investigate and resolve login issues reported by users on mobile devices.",
    "type": "Bug",
    "priority": "High"
  },
  {
    "summary": "Build analytics dashboard",
    "description": "Create a new dashboard to visualize key performance metrics.",
    "type": "Story",
    "priority": "Medium"
  }
]
```
