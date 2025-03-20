def get_prompt(user_input):
    return f"""
You are an expert in writing Splunk SPL queries.
Convert the following natural language request into a valid SPL query.
Only return the query. Do not include any explanation or extra text.

Request: "{user_input}"
SPL:
"""
