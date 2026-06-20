
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Advanced AI Interview Copilot", layout="wide")

st.title("Advanced AI Interview Copilot")

questions = pd.read_csv("../data/interview_questions.csv")

role = st.selectbox("Select Role", questions["role"].unique())

filtered = questions[questions["role"] == role]

if not filtered.empty:
    q = filtered.sample(1).iloc[0]

    st.subheader(q["question"])
    st.write("Difficulty:", q["difficulty"])

    answer = st.text_area("Write your answer")

    if st.button("Evaluate"):
        tech_score = min(len(answer) * 2, 100)
        confidence_score = min(len(answer.split()) * 4, 100)

        st.metric("Technical Score", tech_score)
        st.metric("Confidence Score", confidence_score)

feedback = pd.read_csv("../data/feedback_dataset.csv")

fig = px.line(feedback, y="technical_score")

st.plotly_chart(fig)
