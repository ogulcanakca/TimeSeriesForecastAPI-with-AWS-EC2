# tests/test_utils.py

import pytest
import pandas as pd
from app.utils import validate_csv, preprocess_data
from app.config import Config
import os


def test_validate_csv_empty():
    with pytest.raises(ValueError, match="CSV file is empty"):
        validate_csv(b"")


def test_validate_csv_invalid_format():
    with pytest.raises(ValueError, match="CSV file is empty "
                       "or file is not CSV."):
        validate_csv(b"not a csv content")


def test_preprocess_data():
    data_path = os.path.join("data", "data.csv")
    dummy_data = pd.read_csv(data_path)
    dummy_data = preprocess_data(df=dummy_data)

    assert "open" in dummy_data.columns
    assert "high" in dummy_data.columns


def test_create_time_steps():
    time_step = Config.TIME_STEP

    assert time_step == Config.TIME_STEP
