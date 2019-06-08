import schedule
import time
import sensor
import requests
import os

def job():
    # 1分間のデータを取得
    data = sensor.load(minutes=1)
    if len(data) > 0:
        # センサーに反応があればLINEに通知
        requests.get(os.getenv('LINE_URL'))

if __name__ == "__main__":
    # 毎分ごとにセンサーデータ取得ジョブを実行
    schedule.every().minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)