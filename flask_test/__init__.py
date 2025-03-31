import os
import torch
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from dummy_model import DummyModel


# 이미 시스템 환경변수가 설정되어 있다면 .env의 값은 덮어쓰지 않도록 override=False 사용
load_dotenv(dotenv_path=".env", override=False)

MYSQL_URL = os.getenv("MYSQL_URL")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

# 환경변수가 누락된 경우 에러 처리 (옵션)
if not MYSQL_URL or not MYSQL_USER or not "MYSQL_PASSWORD":
    raise Exception("MySQL 관련 환경변수가 설정되지 않았습니다.")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_URL}/safe_battery"
)
db = SQLAlchemy(app=app)

model = DummyModel()
model.load_state_dict(torch.load("dummy_model.pt", weights_only=False))
model.eval()

import flask_test.views
import flask_test.models


if __name__ == "__main__":
    app.run(debug=True)
