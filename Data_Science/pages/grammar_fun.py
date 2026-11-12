
import streamlit as st
import openai
from openai import OpenAI

API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=API_KEY)


def generate_grammar_exercise():
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Data Science teacher. "
                        "Teach people Data Science through fun "
                        "and interesting short exercises. "
                        "Give fill-in-the-blanks or multiple-choice "
                        "questions. Give only one question."
                    )
                },
                {
                    "role": "user",
                    "content": "Create one fun Data Science MCQ."
                }
            ]
        )

        return completion.choices[0].message.content.strip()

    except openai.APIStatusError as e:
        st.error(f"OpenAI API error: {e.status_code}")
        st.write(e.message)
        return None

    except openai.APIConnectionError:
        st.error("Could not connect to OpenAI. Check your internet connection.")
        return None


def check_answer(question, user_answer):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Data Science teacher. "
                        "Determine whether the answer is correct. "
                        "Provide the correct answer and a short explanation."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Question: {question}\n"
                        f"Answer: {user_answer}\n"
                        "Evaluate the answer and provide feedback."
                    )
                }
            ]
        )

        return completion.choices[0].message.content.strip()

    except openai.APIStatusError as e:
        st.error(f"OpenAI API error: {e.status_code}")
        st.write(e.message)
        return None

    except openai.APIConnectionError:
        st.error("Could not connect to OpenAI.")
        return None


def app():
    st.header("📊 Data Science MCQ Generator")
    st.write(
        "Test your Data Science knowledge with "
        "AI-generated multiple-choice questions!"
    )

    if "exercise" not in st.session_state:
        st.session_state.exercise = None

    if "user_response" not in st.session_state:
        st.session_state.user_response = ""

    if st.button("Generate Question"):
        st.session_state.exercise = generate_grammar_exercise()
        st.session_state.user_response = ""

    if st.session_state.exercise:
        st.subheader("Exercise:")
        st.write(st.session_state.exercise)

        user_response = st.text_input(
            "Your answer:",
            key="response"
        )

        if st.button("Check Answer"):
            if user_response.strip():
                feedback = check_answer(
                    st.session_state.exercise,
                    user_response
                )

                if feedback:
                    st.subheader("Feedback on Your Answer:")
                    st.write(feedback)
            else:
                st.error("Please enter an answer before checking.")
