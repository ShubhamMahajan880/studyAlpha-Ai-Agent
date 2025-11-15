"""
Tools: planner, quiz generator, evaluator.
These are agent-facing tools used by the high-level agents.
"""
import json
from typing import List, Dict, Any
from .utils import call_gemini, trace
from .memory import MemoryBank

def create_study_plan(topics: List[Dict[str, Any]], hours_per_day: float = 2.0, days: int = 7) -> Dict[str, Any]:
    """
    Create a study plan. If LLM mock returns JSON, parse; otherwise run deterministic planner.
    topics: [{"topic":"Arrays","priority":2}, ...]
    """
    prompt = f"Planner: topics={topics}, hours_per_day={hours_per_day}, days={days}. Return JSON."
    out = call_gemini(prompt)
    if out.startswith("MOCK_RESPONSE"):
        # Deterministic round-robin scheduling weighted by priority.
        flat = []
        for t in topics:
            copies = max(1, int(t.get("priority", 1)))
            flat += [t["topic"]] * copies
        plan = {f"day_{i+1}": [] for i in range(days)}
        for idx, topic in enumerate(flat):
            day = f"day_{(idx % days) + 1}"
            plan[day].append({"topic": topic, "duration_mins": int(60 * hours_per_day / max(1, len(flat))), "type": "learning"})
        resp = {"plan_id": "mock_plan_v1", "days": plan, "meta": {"hours_per_day": hours_per_day, "days": days}}
        trace("tools.create_study_plan", {"topics": topics, "days": days})
        return resp
    # Production path would parse JSON content from out
    try:
        parsed = json.loads(out.split("\n", 1)[1])
        trace("tools.create_study_plan.llm", {"raw": out[:200]})
        return parsed
    except Exception:
        trace("tools.create_study_plan.parse_failed", {"raw": out[:200]})
        # fallback deterministic
        return create_study_plan(topics, hours_per_day, days)

def generate_quiz_from_topic(topic: str, mode: str = "general", memory: MemoryBank | None = None) -> Dict[str, Any]:
    context = ""
    if memory:
        hits = memory.query(topic, top_k=3)
        context = "\n".join([h["text"] for h in hits])
    prompt = f"QuizAgent: topic={topic}, mode={mode}, context={context}. Return JSON with 3 questions."
    out = call_gemini(prompt)
    if out.startswith("MOCK_RESPONSE"):
        qs = [{"id": f"q{i+1}", "q": f"Explain {topic} — part {i+1}", "a": "Sample answer", "type": "text"} for i in range(3)]
        return {"quiz_id": f"mock_quiz_{topic.replace(' ', '_')}", "topic": topic, "questions": qs}
    try:
        parsed = json.loads(out.split("\n", 1)[1])
        return parsed
    except Exception:
        trace("tools.generate_quiz_from_topic.parse_failed", {"topic": topic})
        return {"quiz_id": "fallback", "topic": topic, "questions": []}

def evaluate_quiz(answers: List[str], ground_truth: List[str]) -> Dict[str, Any]:
    scores = []
    for a, g in zip(answers, ground_truth):
        try:
            scores.append(1.0 if a.strip().lower() == g.strip().lower() else 0.0)
        except Exception:
            scores.append(0.0)
    total = sum(scores)
    return {"score": total, "max_score": len(scores), "accuracy": total / len(scores) if scores else 0.0}
