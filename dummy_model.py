import torch
import torch.nn as nn
import pandas as pd

class DummyModel(nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()

    def forward(self, x):
        # 각 행의 모든 수치형 값의 합계를 예측 값으로 반환
        return x.sum(dim=1)

if __name__ == "__main__":
    model = DummyModel()
    model.eval()  # 평가 모드로 설정
    # 모델을 dummy_model.pt 파일로 저장
    torch.save(model.state_dict(), "dummy_model.pt")
    print("DummyModel saved as dummy_model.pt")
    print(__name__)
