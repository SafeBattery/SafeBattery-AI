#!/bin/bash
cd /home/ubuntu/flask_test
source .venv/bin/activate

# PID 파일에 기록된 gunicorn 프로세스가 있으면 강제 종료
if [ -f gunicorn.pid ]; then
    PID=$(cat gunicorn.pid)
    if ps -p $PID > /dev/null; then
        echo "Stopping existing Gunicorn process with PID $PID"
        sudo kill -9 $PID
        sleep 5
    fi
fi

# PID 파일 기반으로 종료되지 않은 다른 gunicorn 프로세스들도 강제로 종료 (다른 유저의 프로세스 포함)
sudo pkill -9 -f gunicorn

# 새로운 gunicorn 프로세스 백그라운드 실행 및 PID 기록
nohup gunicorn --workers 2 --bind 0.0.0.0:8000 flask_test:app > gunicorn.log 2>&1 &
echo $! > gunicorn.pid
