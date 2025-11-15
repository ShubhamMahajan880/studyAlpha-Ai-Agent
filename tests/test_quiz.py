from studyalpha.tools import generate_quiz_from_topic

def test_quiz_has_questions():
    quiz = generate_quiz_from_topic("Arrays", "general", None)
    assert "questions" in quiz
    assert len(quiz["questions"]) == 3
