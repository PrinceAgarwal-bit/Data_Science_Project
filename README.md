# 🤖 Data Science Fun & Learn

An AI-powered Streamlit application that makes Data Science learning
simple, interactive, and fun.

## 🚀 Live Demo

[Open the Live
App](https://datascienceproject-bmz58bbybnesd97x2u2pba.streamlit.app/)

## 📌 About

**Data Science Fun & Learn** is a B.Tech CSE project that uses AI to
help students understand and practice Data Science concepts.

### ✨ Main Features

-   🗄️ **SQL Query Explainer**\
    Enter a SQL query and get a simple, step-by-step explanation of its
    logic.

-   🎯 **Data Science MCQ Generator**\
    Generate AI-powered Data Science questions and receive feedback on
    your answers.

-   🏠 **Interactive Home Page**\
    A modern interface with simple navigation and an overview of the
    learning tools.

## 🛠️ Technologies

-   Python
-   Streamlit
-   OpenAI API
-   HTML/CSS
-   Git & GitHub
-   Streamlit Community Cloud

## 📂 Project Structure

``` text
Data_Science/
├── app.py
├── requirements.txt
├── .gitignore
├── pages/
│   ├── __init__.py
│   ├── home.py
│   ├── grammar_fun.py
│   └── reading_translation.py
└── .streamlit/
    └── secrets.toml
```

## 🔐 API Key Security

The OpenAI API key is stored using **Streamlit Secrets** instead of
being written directly in the source code.

``` python
API_KEY = st.secrets["OPENAI_API_KEY"]
```

The `secrets.toml` file is excluded from GitHub using `.gitignore`.

## ⚙️ Run Locally

Clone the repository and install the required packages:

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Data_Science
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:

``` toml
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

Run the application:

``` bash
streamlit run app.py
```

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud** and
connected to GitHub.

**Live Application:**\
https://datascienceproject-bmz58bbybnesd97x2u2pba.streamlit.app/

## 🎓 Project Details

**Project:** Data Science Fun & Learn\
**Developer:** Prince Agarwal\
**Course:** B.Tech CSE\
**Purpose:** Academic / Educational Project

## 🔮 Future Enhancements

-   Add Python, Statistics, Pandas, and Machine Learning learning
    modules.
-   Add difficulty levels and scoring.
-   Add progress tracking.
-   Add more interactive Data Science exercises.

## 📄 License

This project is created for educational and academic purposes.
