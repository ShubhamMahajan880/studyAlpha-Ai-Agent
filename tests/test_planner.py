from studyalpha.tools import create_study_plan

def test_planner_returns_days():
    topics = [{"topic":"A","priority":1},{"topic":"B","priority":2}]
    plan = create_study_plan(topics, hours_per_day=2.0, days=7)
    assert "days" in plan
    assert len(plan["days"]) == 7
