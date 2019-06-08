import os
import requests
from datetime import datetime, timedelta

url = 'https://svcipp.planex.co.jp/api/get_data.php'
payload = {
  'type': 'WS-USB02-PIR',
  'mac': os.getenv('MAC'),
  'token': os.getenv('TOKEN')
}

def load(minutes):
  # 取得時刻
  now = datetime.now()
  minute_age = now - timedelta(minutes=minutes)
  str_formte = '%Y/%m/%d %H:%M:%S'
  payload['from'] = minute_age.strftime(str_formte)
  payload['to'] = now.strftime(str_formte)

  # センサーデータ取得API
  r = requests.get(url, params=payload)
  return r.json()