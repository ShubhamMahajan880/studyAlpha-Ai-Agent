"""
Streamlit frontend for StudyAlpha demo.
Run locally: `streamlit run frontend/app.py`
"""
import streamlit as st
import json
from studyalpha.agents import StudyOrchestrator
from studyalpha.predictor import train_and_save_model

st.set_page_config(page_title="StudyAlpha — Demo", layout="wide")
st.title("StudyAlpha — Personal AI Study Coach (Demo)")
st.markdown("**Shubham Mahajan · AI Agent Arc** — StudyAlpha ULTRA demo")

# Initialize orchestrator in session state
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = StudyOrchestrator()
    try:
        train_and_save_model()
    except Exception:
        pass

with st.sidebar:
    st.header("User profile")
    name = st.text_input("Your name", value="Test Learner")
    dsa_mode = st.checkbox("Enable DSA mode", value=True)
    hours_per_day = st.slider("Hours per day", min_value=1.0, max_value=6.0, value=2.0)
    days = st.slider("Plan days", 3, 14, 7)

st.header("Step 1 — Enter Topics")
topics_str = st.text_area("Topics (one per line; append priority as comma, e.g. 'Algorithms,2')",
                          value="Arrays,2\nGraphs,1\nDynamic Programming,2")
if st.button("Generate Plan"):
    topics = []
    for line in topics_str.strip().splitlines():
        parts = [p.strip() for p in line.split(",")]
        if parts:
            topics.append({"topic": parts[0], "priority": int(parts[1]) if len(parts) > 1 else 1})
    orchestrator = st.session_state.orchestrator
    flow = orchestrator.full_plan_flow(topics, hours_per_day, days)
    st.session_state.plan = flow["plan"]
    st.session_state.sample_quiz = flow["sample_quiz"]
    st.success("Plan generated! See sections below.")

if "plan" in st.session_state:
    st.subheader("Generated Study Plan (sample days)")
    st.json(st.session_state.plan)
    st.subheader("Sample Quiz (for first topic)")
    for i, q in enumerate(st.session_state.sample_quiz.get("questions", [])):
        st.markdown(f"**Q{i+1}. {q.get('q')}**")
        st.text_input(f"Your answer to Q{i+1}", key=f"ans_{i}")
    if st.button("Submit Sample Answers"):
        answers = []
        for i, q in enumerate(st.session_state.sample_quiz.get("questions", [])):
            answers.append(st.session_state.get(f"ans_{i}", ""))
        orchestrator = st.session_state.orchestrator
        res = orchestrator.tracker.record_quiz(st.session_state.sample_quiz, answers)
        st.write("Evaluation:", res["evaluation"])
        st.write("Weakness probability (higher -> needs revision):", round(res["weakness_prob"], 2))
        st.success("Quiz recorded to memory.")
