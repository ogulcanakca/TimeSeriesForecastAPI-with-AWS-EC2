# tests/test_prediction_service.py

from app.prediction_service import PredictionService
from fastapi import UploadFile
from io import BytesIO

import pytest


@pytest.mark.asyncio
async def test_process_file_empty():
    prediction_service = PredictionService()
    empty_file = UploadFile(filename="empty.csv", file=BytesIO(b""))

    with pytest.raises(Exception) as e:
        await prediction_service.process_file(empty_file)
    assert "CSV file is empty" in str(e.value)


@pytest.mark.asyncio
async def test_process_file_valid():
    prediction_service = PredictionService()
    valid_csv_content = (
        "open,high,low,volume\n"
        "100,105,95,1000\n"
        "105,110,100,1500\n"
    )
    valid_file = UploadFile(
        filename="valid.csv", file=BytesIO(valid_csv_content.encode("utf-8"))
    )

    predictions = await prediction_service.process_file(valid_file)
    assert isinstance(predictions, list)
