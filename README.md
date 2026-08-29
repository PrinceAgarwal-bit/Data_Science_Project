🤖 Data Science Fun & Learn

An AI-powered Streamlit application designed to make learning Data
Science simple, interactive, and fun.

🚀 Live Demo

Open Data Science Fun &
Learn

📌 About the Project

Data Science Fun & Learn is a B.Tech CSE project that combines AI
with interactive learning tools for Data Science students and beginners.

The application currently provides two AI-powered learning tools:

🗄️ SQL Query Explainer -- Paste a SQL query and get a
step-by-step explanation in simple language.

🎯 Data Science MCQ Generator -- Generate Data Science practice
questions and receive AI-powered feedback on your answer.

✨ Features

🗄️ SQL Query Explainer

Accepts SQL queries from the user.

Uses OpenAI to explain the query in plain English.

Breaks down SELECT fields, JOINs, WHERE conditions, GROUP BY
clauses, and other query logic.

Provides an easy-to-understand explanation for learners.

🎯 Data Science MCQ Generator

Generates short Data Science questions using AI.

Supports multiple-choice and fill-in-the-blank style exercises.

Allows users to submit their answers.

Uses AI to evaluate the answer and provide feedback.

🏠 Interactive Home Page

Modern dark-themed interface.

Responsive Streamlit layout.

Explains the purpose of the platform and its learning tools.

Simple sidebar navigation.

🛠️ Technologies Used

Python

Streamlit

OpenAI API

HTML/CSS for custom UI styling

Git & GitHub for version control

Streamlit Community Cloud for deployment

📂 Project Structure

Data_Science/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── .streamlit/
│   └── secrets.toml
│
└── pages/
    ├── __init__.py
    ├── home.py
    ├── grammar_fun.py
    └── reading_translation.py

🔐 API Key Security

The application uses Streamlit Secrets for the OpenAI API key.

The API key is not stored directly in the Python source code or GitHub
repository.

The application accesses it using:

API_KEY = st.secrets["OPENAI_API_KEY"]

The local secrets.toml file is excluded from Git using .gitignore.

⚙️ Run the Project Locally

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd Data_Science

2. Install dependencies

pip install -r requirements.txt

3. Configure the OpenAI API key

Create:

.streamlit/secrets.toml

Add:

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

Never commit this file to GitHub.

4. Run the application

streamlit run app.py

The application will open in your browser.

☁️ Deployment

The project is deployed using Streamlit Community Cloud and
connected to a GitHub repository.

Live application:

https://datascienceproject-bmz58bbybnesd97x2u2pba.streamlit.app/

🎓 Project Information

Project: Data Science Fun & Learn
Technology: Python, Streamlit, OpenAI API
Type: B.Tech CSE Project
Developer: Prince Agarwal

🎯 Future Enhancements

Add more Data Science topics such as Python, Statistics, Machine
Learning, and Pandas.

Add user progress tracking.

Add difficulty levels for MCQs.

Add scores and leaderboards.

Add more SQL examples and interactive practice.

Add authentication and personalized learning paths.

📄 License

This project is created for educational and academic purposes.
