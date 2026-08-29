import streamlit as st
import openai

from openai import OpenAI

API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=API_KEY)


def generate_grammar_exercise():
    # Using OpenAI to generate a grammar exercise
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
      {"role": "system","content": "You are a Data Science teacher. your job is to tech people data science, via fun and interesting short exercises by sharing with them some fill in the blanks or multiple choice questions. Please give one question only"
},
      {"role": "user","content": "Create a fun data science exercise (fill in the blanks or multiple choice) based on data science. Please give one question only"
}
      ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content.strip()

def check_answer(question, user_answer):
    # Using OpenAI to check the user's answer and provide feedback
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
      {"role": "system", "content": "You are an expert Data Science teacher and evaluator.Your job is to determine whether the answer is correct or incorrect, provide the correct option, and give a short, clear explanation."},
      {"role": "user", "content": f"Question: {question}\nAnswer: {user_answer}\nEvaluate the correctness of the answer and provide feedback:"}
      ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content.strip()



def app():
    st.header('📊 Data Science MCQ Generator')
    st.write('Test your Data Science knowledge with AI-generated multiple-choice questions!')

    # State management for exercise generation and user input
    if 'exercise' not in st.session_state:
        st.session_state.exercise = None
    if 'user_response' not in st.session_state:
        st.session_state.user_response = ''

    # Generate exercise button
    if st.button('Generate Question'):
        st.session_state.exercise = generate_grammar_exercise()
    
    if st.session_state.exercise:
        st.subheader('Exercise:')
        st.write(st.session_state.exercise)

        # User input for response
        user_response = st.text_input('Your answer:', key="response")

        if st.button('Check Answer'):
            if user_response:
                st.session_state.user_response = user_response
                feedback = check_answer(st.session_state.exercise, user_response)
                st.subheader('Feedback on Your Answer:')
                st.write(feedback)
            else:
                st.error("Please enter an answer before checking.")
