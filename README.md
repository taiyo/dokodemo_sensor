# dokodemo_sensor

どこでもセンサーの値を定期的に読み取り、値に応じてLINEに通知するなどのアクションを行う。

## 環境変数
トークンを環境変数として```app.env```として設定する。

```
MAC=
TOKEN=
LINE_URL
```

## 起動
```bash
docker-compose up -d
```
