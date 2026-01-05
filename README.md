<div align="center">

# 🧠 StudyAlpha-AI-Agent  
## **Autonomous Study & Revision System**  
### *Your Personal AI Study Coach powered by Multi-Agent Intelligence*

[![Made with Python](https://img.shields.io/badge/Python-3.10-blue)]()
[![Multi-Agent System](https://img.shields.io/badge/Multi--Agent-Architecture-brightgreen)]()
[![Machine Learning](https://img.shields.io/badge/ML-Weakness%20Prediction-orange)]()
[![RAG](https://img.shields.io/badge/RAG-TF--IDF%20Memory-purple)]()
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)]()

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/fb7afdc4-3409-4566-8fc2-ce304b4e5b49" />

</div>

---

# 🚀 Google × Kaggle Agents Intensive – Capstone Project  
## 🏆 *Hackathon Writeup + Full System Documentation*

---

# 🟦 Problem Statement  

Students today struggle with **learning consistency**.  
Effective learning requires:

- 🗂️ structured planning  
- 📊 progress tracking  
- 📝 performance evaluation  
- ❗ early detection of weak topics  

Most learners **don’t know what to study next**, how long to study, or when to revise.  
Traditional AI tools simply **answer questions** — they don’t:

- plan  
- evaluate  
- remember  
- adapt  

💡 **StudyAlpha solves this** by acting as a complete, autonomous study coach that:

- plans the study roadmap  
- generates quizzes  
- evaluates understanding  
- predicts weaknesses using ML  
- adjusts future study sessions automatically  

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/8c525cac-eaca-480c-914c-b6e0db5f0eb5" />

---

# 🤖 Why I Used Agents  

Learning involves multiple interdependent tasks:

✔ planning  
✔ quizzing  
✔ evaluating  
✔ memory retrieval  
✔ weakness prediction  
✔ revision scheduling  

No single LLM call can manage this entire workflow.

### Agents enable:
- 🔹 **Modularity** — each task handled by a specialized sub-agent  
- 🔹 **Delegation** — one agent passes output to the next  
- 🔹 **Memory** — mistakes & patterns influence future learning  
- 🔹 **Multi-step reasoning** — structured learning cycles  
- 🔹 **Extensibility** — new agents or tools can be added easily  

📘 StudyAlpha behaves like a **real human tutor** — thoughtful, adaptive, and aware of past performance.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/995fca32-8271-4053-9706-28e5c51efb33" />


---

🌐 Deployment
Platform: Streamlit Cloud
Entry file: app.py
Auto-deploy: On every push to main
🔗 Live App:
https://studyalpha-ai-agent-muwkpf3edkao3iva87sxgp.streamlit.app


# 🏗️ Architecture Overview  

StudyAlpha is a **multi-agent learning ecosystem** orchestrated by a central StudyOrchestrator.

---

## 1️⃣ **StudyOrchestrator (Master Controller)**  
Controls the entire pipeline:

- planning  
- quiz creation  
- evaluation  
- tracking  
- revision generation  

---

## 2️⃣ **Planner Agent**  
Builds personalized study plans using:

- topics  
- priority  
- difficulty  
- available hours  
- duration  

Outputs a **multi-day optimized schedule**.

---

## 3️⃣ **Quiz Agent**  
- Generates **3 conceptual questions**  
- Uses a **TF-IDF RAG Memory**  
- Pulls context from past mistakes & logs  

---

## 4️⃣ **Revision Agent**  
Generates targeted revision tasks based on:

- past mistakes  
- predicted weaknesses  
- forgotten topics  

Optimized for **spaced repetition**.

---

## 5️⃣ **Tracker Agent**  
Evaluates quiz answers and logs:

- accuracy  
- score  
- correctness patterns  

Feeds data into the ML model.

---

## 6️⃣ **Weakness Predictor (ML Model)**  
A **GradientBoostingClassifier** predicts:

- weakness probability  
- likelihood of future mistakes  
- topics needing urgent focus  

---

## 7️⃣ **Memory Bank (RAG System)**  
Stores and retrieves:

- quizzes  
- explanations  
- errors  
- performance logs  
- improvement history  

Powered by **TF-IDF + Cosine Similarity**.

---

## 8️⃣ **Streamlit UI (Optional)**  
A simple interface to:

- generate study plans  
- take quizzes  
- see analytics  
- visualize performance  


<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/6323c1bc-fe13-460d-88b9-fbf21dfc1bff" />

---

# 🔄 Architecture Summary  

```
Plan → Quiz → Evaluate → Predict Weakness → Revise → Store Memory → Adapt Next
```

---

# 🖼️ Architecture Diagram  


<img width="637" height="951" alt="image" src="https://github.com/user-attachments/assets/751f89e4-9fe6-4895-bc49-d99ecc47067e" />

---

# 🎬 Demo and Simulation  

The notebook demonstrates a **full 7-day learning simulation**:

- study plans  
- quiz generation  
- evaluation  
- ML-based weakness prediction  
- dynamic revision cycles  
- memory retrieval  
- performance graphs  
- time allocation charts  
- exported reports  

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/5f8f5439-876d-4109-a838-a4c220fbf839" />

---

# 📅 Study Plan Example  

For topics:

- Arrays – Priority 2  
- Graphs – Priority 1  
- DP – Priority 2  

The planner builds a **7-day optimized schedule**.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/1c130314-8bfd-4aa7-83f5-bcd7fc52ac63" />

---


## 🔄 2) WORKFLOW DIAGRAM  
> *(Insert your workflow diagram image below — drag & drop into GitHub editor and replace the link)*

<img width="379" height="949" alt="image" src="https://github.com/user-attachments/assets/59a3d84b-b45a-444f-bf8b-143d37e1c04c" />

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/e3b67a7a-a0ab-465a-9484-005362a0c296" />



# 📝 Quiz Generation  

Example for topic **DP**:

- 3 conceptual MCQs  
- Memory-aware grounding  


---

# 📈 Evaluation & Tracking  

Logs include:

- correct / incorrect  
- explanations  
- topic-wise accuracy  

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/e993ed25-54ce-4905-b464-7fff10529a9c" />

---

# 🔮 Weakness Prediction  

ML model assigns a numerical probability:

```
Weakness Probability: 0.73  
→ High chance of confusion  
```

---

# 🔁 Revision Planning  

Revision Agent outputs:

- targeted tasks  
- recommended questions  
- spaced repetition intervals  

---

# 📊 Analytics & Visualizations  

Includes:

- study-time distribution chart  
- accuracy line graph  
- mistake clusters  
- topic dependency graph  
- memory-retrieval maps  
- revision heatmaps  

---

# 🛠️ The Build  

### ✨ Engineering Philosophy  
StudyAlpha is:

- modular  
- reproducible  
- deterministic  
- easy to test  
- extendable  

### 🧰 Technologies Used  

- Python  
- Scikit-learn  
- Pandas / NumPy  
- TF-IDF / Cosine Similarity  
- Streamlit  
- Joblib  
- Logging & Tracing  

### 🔧 Key Design Decisions  

- Deterministic mock LLM (no API keys required)  
- True multi-agent architecture  
- RAG-based quiz grounding  
- ML-based weakness prediction  
- Structured modular repository  

### 📦 Notebook Includes  

- agent modules  
- memory system  
- planner/quiz/revision pipelines  
- ML training + explainability  
- analytics & visualizations  
- reproducible tests  
- synthetic student simulation  

---

# ⏳ Future Improvements  

- Gemini Integration for richer feedback  
- Cloud deployment (API/Serverless)  
- Long-term spaced repetition pipeline  
- Daily streak tracking  
- PDF/notes ingestion  
- Leaderboards & gamification  

---

# 📝 Final Note  

**StudyAlpha acts like a real AI tutor — doing more than answering questions.**  
It thinks, plans, evaluates, adapts, and remembers.

This system combines:

- multi-agent intelligence  
- memory  
- ML prediction  
- structured planning  

Perfectly aligned with the goals of the **Google × Kaggle Agents Intensive Capstone**.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d1a4328f-52d2-4ceb-9c5e-6e10f7c70e4f" />

---

# 👤 Author  
### **Shubham Mahajan**  
AI & Web Developer  
*“Solve. Fail. Learn. Repeat.”*

---

# 🔗 Project Links  

- `studyalpha_video_demo.ipynb`  
- `studyAlpha_demo.ipynb`  
- GitHub Repository: **https://github.com/ShubhamMahajan880/studyAlpha-Ai-Agent**

