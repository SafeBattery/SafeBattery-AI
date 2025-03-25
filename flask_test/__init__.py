from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import torch

from dummy_model import DummyModel


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root@localhost:3306/safe_battery"
)
db = SQLAlchemy(app=app)

model = DummyModel()
model.load_state_dict(torch.load("dummy_model.pt", weights_only=False))
model.eval()

import flask_test.views
import flask_test.models


if __name__ == "__main__":
    app.run(debug=True)
