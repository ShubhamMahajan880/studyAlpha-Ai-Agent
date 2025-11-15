"""
studyalpha.utils
LLM wrapper, tracing, and lightweight config helpers.
"""
import os
import json
import logging
import random
from typing import Any, Dict, Optional

logger = logging.getLogger("studyalpha")
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def get_gemini_key() -> Optional[str]:
    """Retrieve Gemini key from Kaggle secrets or environment variable."""
    try:
        from kaggle_secrets import UserSecretsClient
        user_secrets = UserSecretsClient()
        return user_secrets.get_secret("GOOGLE_API_KEY")
    except Exception:
        return os.getenv("GEMINI_API_KEY", None)

def mock_llm(prompt: str) -> str:
    """
    Deterministic mock LLM response for reproducible demos.
    Makes outputs dependent on prompt content but deterministic.
    """
    seed = abs(hash(prompt)) % 10000
    random.seed(seed)
    header = "MOCK_RESPONSE\n"
    # Simple structured JSON-like reply when prompt asks for JSON, otherwise plain text.
    if "Return a JSON" in prompt or "Return JSON" in prompt or prompt.strip().endswith("Return JSON"):
        # Minimal plausible plan or quiz structures depending on keyword detection.
        if "Planner" in prompt or "create_study_plan" in prompt:
            plan = {"plan_id": "mock_plan_v1", "days": {f"day_{i+1}": [] for i in range(7)}, "meta": {}}
            return header + json.dumps(plan)
        if "QuizAgent" in prompt or "Quiz" in prompt:
            questions = [{"id": f"q{i+1}", "q": f"Explain part {i+1} of topic", "a": "Sample answer", "type": "text"} for i in range(3)]
            return header + json.dumps({"questions": questions})
    # Fallback general text
    body = f"This deterministic mock answer (seed={seed}) for prompt excerpt: {prompt[:160].replace('\\n',' ')}"
    return header + body

def call_gemini(prompt: str, model: str = "gemini-2.5-flash", max_tokens: int = 512) -> str:
    """
    Unified LLM wrapper. If a Gemini key is present and SDK installed,
    replace the TODO with the official SDK call. Otherwise returns deterministic mock.
    """
    key = get_gemini_key()
    if key:
        # If you add real Gemini support, implement it here.
        # Example pseudocode (DO NOT COMMIT KEYS):
        # import google.generativeai as genai
        # genai.configure(api_key=key)
        # model_obj = genai.GenerativeModel(model)
        # out = model_obj.generate_content(prompt, max_tokens=max_tokens, temperature=0.2)
        # return out.text
        logger.info("Gemini key detected but SDK call not implemented. Using mock instead.")
        return mock_llm(prompt)
    else:
        return mock_llm(prompt)

def trace(action: str, details: Dict[str, Any]):
    """Simple structured trace logger for observability."""
    payload = {"action": action, **(details or {})}
    logger.info(json.dumps(payload))
