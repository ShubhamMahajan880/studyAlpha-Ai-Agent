# 📘 Study Alpha – Focused Learning Planner

A study assistance application that helps students **plan, track, and adapt** their learning for both **exam-focused preparation** and **daily consistency-based study**.  
The system builds an adaptive study schedule based on available time, tracks actual study effort, redistributes remaining workload dynamically, and highlights what to study next.

This project represents the **working, deployed implementation** of the broader **StudyAlpha AI vision**, focused on **real usability and explainable planning logic**.

---

## 🚀 Problem Statement

Students often struggle not because of lack of resources, but because they lack:

- Clear direction on what to study today.
- Visibility into remaining syllabus and effort.
- Adaptive schedules when progress changes.
- Identification of weak or lagging topics.
- Realistic time management.

Most tools either provide static timetables or simply answer questions.  
They **do not adapt** as learning progresses.

**Study Alpha – Focused Learning Planner** solves this by acting as a **living, adaptive study plan**.

---

## 🧠 How It Works (High-Level)

- User enters **exam date** and **daily study hours**.
- User adds **subjects and their topics**.
- The system calculates **remaining days** and **total available study time**.
- An initial **topic-wise study plan** is generated.
- User logs **actual study effort** per topic.
- Remaining workload is recalculated automatically.
- Pending topics receive **redistributed time**.
- The system highlights:
  - Daily study focus.
  - Weak or incomplete topics.
  - Urgency based on remaining time.

The logic is **deterministic, explainable, and planner-driven**, similar to how a real human study coach adapts plans.

---

## 🌐 Live Demo

🔗 **Live Application:**  
https://studyalpha-ai-agent-muwkpf3edkao3iva87sxgp.streamlit.app

---

## 📊 Core Planning Logic

Total Available Hours = Remaining Days × Daily Study Hours

Initial Topic Allocation = Total Available Hours / Total Topics

As topics are completed:

Remaining hours are recalculated.

Time is redistributed only among pending topics.

This ensures the evaluation is **effort-aware**, not static.

---

## 🖥️ Application Flow

- Enter exam date and daily study hours.
- Add subjects and their topics.
- Generate the initial study plan.
- Log study progress per topic.
- View:
  - Completed vs remaining effort.
  - Updated time distribution.
  - Next recommended focus areas.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI and application flow.
- **Pandas** – Data handling, progress tracking, and analysis.

No paid APIs or external AI services are required.

---

## 📂 Project Structure

StudyAlpha-Focused-Learning-Planner/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── planner.py
    ├── rebalancer.py
    ├── evaluator.py
    └── recommender.py



---

## ▶️ Run Locally

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

http://localhost:8501


## 🌐 Deployment

- **Platform:** Streamlit Cloud  
- **Entry file:** app.py  
- **Auto-deploy:** On every push to `main`

🔗 **Live App:**  
https://studyalpha-ai-agent-muwkpf3edkao3iva87sxgp.streamlit.app

---

## 🔮 Future Enhancements

- Agent-based orchestration.
- ML-driven weakness prediction.
- Memory-aware revision scheduling.
- Quiz and evaluation agents.
- Long-term spaced repetition.
- Persistent analytics dashboards.

---

## 👤 Author & Ownership

This project is designed, developed, and maintained by **Shubham Mahajan**.

- GitHub: https://github.com/ShubhamMahajan880  
- LinkedIn: https://www.linkedin.com/in/shubham-mahajan-2a9a47220/

The application represents **original work** and includes clear ownership attribution.

---

## ⭐ Why This Project Matters

This project demonstrates:

- Practical problem-solving for real student challenges.
- Adaptive planning without over-claiming AI.
- Explainable and deterministic system design.
- End-to-end product thinking, not just scripts.




