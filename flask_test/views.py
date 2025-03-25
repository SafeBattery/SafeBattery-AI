from flask import jsonify, request
import pandas as pd
import torch

from flask_test import app
from flask_test import db
from flask_test import model
from flask_test.models import *


@app.route('/')
def health_check():
    return 'Server alive!'

@app.route('/api/test/sql')
def test_sql():
    pemfcs = db.session.execute(db.select(PEMFC).order_by(PEMFC.id)).scalars()
    first = pemfcs.all()
    print(first)
    return jsonify(first)

@app.route('/api/test/pandas')
def test_pandas():
    try:
        # 요청 JSON 예시: {"data": [{"feature1": 1.0, "feature2": 2.0}, {...}, ...]}
        json_data = request.get_json()
        # 입력 데이터를 pandas DataFrame으로 변환
        df = pd.DataFrame(json_data["data"])
        # DataFrame을 torch.Tensor로 변환 (dtype: float)
        input_tensor = torch.tensor(df.values, dtype=torch.float32)
        # 모델 예측 수행 (torch.no_grad()를 사용하여 추론 모드)
        with torch.no_grad():
            predictions = model(input_tensor)
        # 예측 결과를 리스트로 변환하여 반환
        result = predictions.numpy().tolist()
        return jsonify({"predictions": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400