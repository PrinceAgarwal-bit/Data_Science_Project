
import streamlit as st
import openai
from openai import OpenAI


# --------------------------------------------------
# 1. OPENAI CLIENT CONFIGURATION
# --------------------------------------------------

try:
    API_KEY = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=API_KEY)

except Exception as e:
    st.error("OpenAI API key configuration failed.")
    st.error(str(e))
    client = None


# --------------------------------------------------
# 2. COMMON API ERROR HANDLING
# --------------------------------------------------

def handle_api_error(e):
    if isinstance(e, openai.NotFoundError):
        st.error("OpenAI returned a 404 Not Found error.")
        st.write("Error message:", e.message)
        st.write("Error code:", e.code)
        st.write("Error details:", e.body)

    elif isinstance(e, openai.AuthenticationError):
        st.error("Invalid OpenAI API key. Check Streamlit Secrets.")

    elif isinstance(e, openai.RateLimitError):
        st.error("API rate limit or quota exceeded.")
        st.write(e.message)

    elif isinstance(e, openai.APIConnectionError):
        st.error("Unable to connect to OpenAI. Check your internet connection.")

    elif isinstance(e, openai.APIStatusError):
        st.error(f"OpenAI API error: {e.status_code}")
        st.write(e.message)
        st.write("Details:", e.body)

    else:
        st.error(f"Unexpected error: {str(e)}")


# --------------------------------------------------
# 3. GENERATE DATA SCIENCE EXERCISE
# --------------------------------------------------

def generate_grammar_exercise():

    if client is None:
        st.error("OpenAI client is not configured.")
        return None

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an expert Data Science teacher.

                    Teach students through fun and interesting
                    short exercises.

                    Generate only ONE multiple-choice question
                    based on Data Science.

                    Include:
                    1. A clear question.
                    2. Four options (A, B, C, D).

                    Do not reveal the correct answer.
                    """
                },
                {
                    "role": "user",
                    "content": "Generate one interesting Data Science MCQ."
                }
            ],
            temperature=0.7,
            max_tokens=300
        )

        return completion.choices[0].message.content.strip()

    except openai.APIStatusError as e:
        handle_api_error(e)
        return None

    except openai.APIConnectionError as e:
        handle_api_error(e)
        return None

    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return None


# --------------------------------------------------
# 4. CHECK USER ANSWER
# --------------------------------------------------

def check_answer(question, user_answer):

    if client is None:
        st.error("OpenAI client is not configured.")
        return None

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an expert Data Science teacher
                    and evaluator.

                    Evaluate the student's answer.

                    Tell the student:
                    1. Whether the answer is correct or incorrect.
                    2. The correct answer.
                    3. A short and simple explanation.

                    Be friendly and encouraging.
                    """
                },
                {
                    "role": "user",
                    "content": (
                        f"Question:\n{question}\n\n"
                        f"Student's answer:\n{user_answer}\n\n"
                        "Evaluate the answer and provide feedback."
                    )
                }
            ],
            temperature=0.5,
            max_tokens=300
        )

        return completion.choices[0].message.content.strip()

    except openai.APIStatusError as e:
        handle_api_error(e)
        return None

    except openai.APIConnectionError as e:
        handle_api_error(e)
        return None

    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return None


# --------------------------------------------------
# 5. CHECK AVAILABLE MODELS (DIAGNOSTICS)
# --------------------------------------------------

def check_available_models():

    if client is None:
        st.error("OpenAI client is not configured.")
        return

    try:
        models = client.models.list()

        available_models = [
            model.id for model in models.data
            if "gpt" in model.id.lower()
        ]

        st.write("Available GPT models:")
        st.write(available_models)

    except openai.APIStatusError as e:
        handle_api_error(e)


# --------------------------------------------------
# 6. STREAMLIT APPLICATION
# --------------------------------------------------

def app():

    st.header("📊 Data Science MCQ Generator")

    st.write(
        "Test your Data Science knowledge "
        "with AI-generated multiple-choice questions!"
    )

    st.divider()

    # Initialize session state

    if "exercise" not in st.session_state:
        st.session_state.exercise = None

    if "feedback" not in st.session_state:
        st.session_state.feedback = None

    if "response" not in st.session_state:
        st.session_state.response = ""

    # Generate question button

    if st.button("🎯 Generate Question"):

        with st.spinner("Generating your Data Science question..."):

            st.session_state.exercise = generate_grammar_exercise()
            st.session_state.feedback = None
            st.session_state.response = ""

    # Display question

    if st.session_state.exercise:

        st.subheader("📝 Your Exercise")

        st.write(st.session_state.exercise)

        st.divider()

        # User answer input

        user_response = st.text_input(
            "Enter your answer (A, B, C or D):",
            key="response"
        )

        # Check answer button

        if st.button("✅ Check Answer"):

            if user_response.strip():

                with st.spinner("Checking your answer..."):

                    feedback = check_answer(
                        st.session_state.exercise,
                        user_response
                    )

                    st.session_state.feedback = feedback

            else:
                st.warning("Please enter your answer first.")

        # Display feedback

        if st.session_state.feedback:

            st.subheader("📢 Feedback on Your Answer")

            st.success("Evaluation completed!")

            st.write(st.session_state.feedback)

    # Diagnostic section

    with st.expander("🔧 API Diagnostics"):

        if st.button("Check Available Models"):

            with st.spinner("Checking OpenAI models..."):
                check_available_models()
