import streamlit as st
import openai
import os
from dotenv import load_dotenv
from prompts import build_prompt
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 GenAI: Requirements to Jira Generator")

user_input = st.text_area("Paste product requirements, emails or ideas here:", height=250)

if st.button("Generate Jira Tickets"):
    if not user_input.strip():
        st.warning("Please enter some input.")
    else:
        with st.spinner("Generating tasks..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a business or system analyst that generates Jira issues from requirements."},
                    {"role": "user", "content": build_prompt(user_input)}
                ],
                temperature=0.3
            )
            result = response.choices[0].message.content
            st.subheader("📋 Generated Jira Tasks")
            st.code(result, language="json")
