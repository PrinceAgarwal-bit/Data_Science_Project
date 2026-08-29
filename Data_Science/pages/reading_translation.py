import streamlit as st
import openai
from openai import OpenAI

API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=API_KEY)

def explain_sql_query(sql_query):
    """Uses OpenAI API to break down and explain a given SQL query."""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert SQL DBA and data engineer. Your task is to explain "
                    "the provided SQL query in plain English. Break down the query step-by-step, "
                    "explaining SELECT fields, JOINs, WHERE filtering conditions, GROUP BYs, "
                    "and performance considerations if applicable."
                ),
            },
            {
                "role": "user",
                "content": f"Please explain this SQL query:\n\n```sql\n{sql_query}\n```",
            },
        ],
    )
    return completion.choices[0].message.content.strip()

def app():
    st.set_page_config(page_title="SQL Query Explainer", page_icon="🧠")
    st.header("🧠 SQL Query Explainer")
    st.write("Paste your SQL query below and AI will break down what it does step-by-step.")

    # SQL Input Area
    sql_input = st.text_area(
        "Enter your SQL Query:",
        height=200,
        placeholder="SELECT u.id, u.name, COUNT(o.id) FROM users u JOIN orders o ON u.id = o.user_id GROUP BY u.id, u.name;"
    )

    # Action Button
    if st.button("Explain Query", type="primary"):
        if sql_input.strip():
            with st.spinner("Analyzing SQL query..."):
                try:
                    explanation = explain_sql_query(sql_input)
                    st.subheader("💡 Query Explanation:")
                    st.markdown(explanation)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please paste a valid SQL query before clicking Explain.")

if __name__ == "__main__":
    app()