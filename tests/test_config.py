# test/test_config.py

from app.config import Config


def test_config_paths():
    assert Config.MODEL_PATH == "./model/model.keras"
    assert Config.SCALER_PATH == "./scaler/scaler.save"
    assert Config.TIME_STEP == 60
    assert "close" in Config.COLUMN_MAPPING
