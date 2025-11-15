from studyalpha.predictor import train_and_save_model, load_model, predict_weakness

def test_predictor_pipeline(tmp_path):
    path = train_and_save_model()
    model = load_model(path)
    assert model is not None
    prob = predict_weakness([0.5, 60.0, 2.0], model)
    assert 0.0 <= prob <= 1.0
