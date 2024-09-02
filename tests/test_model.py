# tests/test_model_handler.py

from app.model import ModelHandler
import os
import pandas as pd
from app.utils import preprocess_data, create_time_steps
from app.config import Config


def test_model_handler_initialization():
    model_handler = ModelHandler()
    assert model_handler.model is not None
    assert model_handler.scaler is not None


def test_model_prediction():
    model_handler = ModelHandler()
    data_path = os.path.join("data", "data.csv")
    dummy_data = pd.read_csv(data_path)
    dummy_data = preprocess_data(df=dummy_data)
    time_step = Config.TIME_STEP
    data = create_time_steps(dummy_data.to_numpy(), time_step)
    predictions = model_handler.predict(data)
    assert predictions.size > 0
