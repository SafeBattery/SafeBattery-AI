#!/bin/bash
cd /home/ubuntu/flask_test
source .venv/bin/activate

# 이전에 실행 중인 Gunicorn 프로세스가 있다면 종료 (PID 파일 사용 또는 pgrep로 검색)
# 예시: PID 파일 방식으로 관리하는 경우
if [ -f gunicorn.pid ]; then
    PID=$(cat gunicorn.pid)
    if ps -p $PID > /dev/null; then
        echo "Stopping existing Gunicorn process with PID $PID"
        kill $PID
        sleep 5
    fi
fi

# Gunicorn 실행 (백그라운드에서 실행하고 PID 기록)
nohup gunicorn --workers 3 --bind 0.0.0.0:8000 flask_test:app > gunicorn.log 2>&1 &
echo $! > gunicorn.pid
