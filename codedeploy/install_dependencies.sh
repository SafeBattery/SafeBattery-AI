#!/bin/bash
set -e

# 배포 대상 디렉토리로 이동 (appspec.yml의 destination과 동일)
cd /home/ubuntu/flask_test

# 가상환경 폴더가 존재하는지 확인, 없을 경우에만 새로 생성
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# 가상환경 활성화 후 의존성 설치
source .venv/bin/activate
pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

# 필요하다면 추가 환경 설정 작업 수행
