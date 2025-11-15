"""
High-level agents and StudyOrchestrator.
"""
import json
from typing import List, Dict, Any
from .tools import create_study_plan, generate_quiz_from_topic, evaluate_quiz
from .memory import MemoryBank
from .predictor import predict_weakness, train_and_save_model, load_model
from .utils import trace

class PlannerAgent:
    def generate(self, topics: List[Dict[str, Any]], hours_per_day: float = 2.0, days: int = 7):
        plan = create_study_plan(topics, hours_per_day, days)
        trace("Planner.generate", {"days": len(plan.get("days", {}))})
        return plan

class RevisionAgent:
    def __init__(self, memory: MemoryBank):
        self.memory = memory

    def generate(self, topic: str):
        # Basic micro-session generator
        trace("Revision.generate", {"topic": topic})
        return {"topic": topic, "sessions": [{"duration_mins": 15, "focus": topic, "activity": "quick_quiz"}, {"duration_mins": 20, "focus": topic, "activity": "review_notes"}]}

class QuizAgent:
    def __init__(self, memory: MemoryBank):
        self.memory = memory

    def generate(self, topic: str, mode: str = "general"):
        return generate_quiz_from_topic(topic, mode, memory=self.memory)

class TrackerAgent:
    def __init__(self, memory: MemoryBank, model_path: str | None = None):
        self.memory = memory
        self.model = load_model(model_path) if model_path else load_model()

    def record_quiz(self, quiz: Dict[str, Any], user_answers: List[str]):
        gt = [q.get("a", "") for q in quiz.get("questions", [])]
        res = evaluate_quiz(user_answers, gt)
        # store quiz result into memory (as JSON string for context)
        record_text = json.dumps({"quiz_topic": quiz.get("topic"), "result": res})
        self.memory.add(record_text, meta={"quiz_id": quiz.get("quiz_id")})
        # features example: [accuracy, avg_time_sec_placeholder, days_since_review_placeholder]
        features = [res["accuracy"], 60.0, 2.0]
        prob = predict_weakness(features, self.model)
        trace("Tracker.record_quiz", {"topic": quiz.get("topic"), "res": res, "weakness_prob": prob})
        return {"evaluation": res, "weakness_prob": prob}

class StudyOrchestrator:
    def __init__(self):
        self.memory = MemoryBank()
        self.planner = PlannerAgent()
        self.revision = RevisionAgent(self.memory)
        self.quiz = QuizAgent(self.memory)
        self.tracker = TrackerAgent(self.memory)

    def full_plan_flow(self, topics: List[Dict[str, Any]], hours_per_day: float = 2.0, days: int = 7):
        plan = self.planner.generate(topics, hours_per_day, days)
        sample_topic = topics[0]["topic"] if topics else "General"
        quiz = self.quiz.generate(sample_topic)
        return {"plan": plan, "sample_quiz": quiz}
