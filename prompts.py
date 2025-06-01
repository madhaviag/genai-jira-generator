def build_prompt(text):
    return f"""
You are a helpful assistant. Based on the input below, generate a list of Jira issues in JSON format.
Each issue should include:
- summary
- description
- type (Bug, Story, Task)
- priority (Low, Medium, High)

Input:
"""
{text}
"""

Output format:
[
  {{
    "summary": "...",
    "description": "...",
    "type": "Story",
    "priority": "Medium"
  }},
  ...
]
"""
"""