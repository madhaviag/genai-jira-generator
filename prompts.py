def build_prompt(text):
    return f"""
You are an Business or System Analyst and an expert in understanding requirements and generating actionable JIRA stories. Based on the input below, generate a list of Jira issues in JSON format.
Each issue should include:
- summary
- description
- type (Bug, Story, Task)
- priority (Low, Medium, High)
The description should have detailed Acceptance Criteria in Given,When,Then format.
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
