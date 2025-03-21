import streamlit as st
from openai import OpenAI
from prompts import get_prompt

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

st.title("🧠 Splunk Query Generator")
st.write("Enter a natural language request to generate a Splunk SPL query.")

user_input = st.text_input("🔍 Natural Language Request", "")

if user_input:
    with st.spinner("Generating SPL..."):
        prompt = get_prompt(user_input)

        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[
                {"role": "system", "content": "You are an expert in Splunk SPL queries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )

        spl_query = response.choices[0].message.content.strip()
        st.code(spl_query, language="spl")
