import streamlit as st
import openai
from prompts import get_prompt

# Set your OpenAI key
#openai.api_key = "YOUR_OPENAI_API_KEY"
openai.api_key = "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"

st.title("🧠 Splunk Query Generator")
st.write("Enter a natural language request to generate a Splunk SPL query.")

user_input = st.text_input("🔍 Natural Language Request", "")

if user_input:
    with st.spinner("Generating SPL..."):
        prompt = get_prompt(user_input)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in Splunk SPL queries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )

        spl_query = response["choices"][0]["message"]["content"].strip()
        st.code(spl_query, language="spl")
