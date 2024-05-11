# user_api

ローカルセットアップ
dockerの初期ビルド
```
$ docker-compose build
```

コンテナ内でpoetry初期化
```
$ docker-compose run \
  --entrypoint "poetry init \
    --name user-api-app \
    --dependency fastapi \
    --dependency uvicorn[standard] \
    --dependency sqlalchemy \
    --dependency aiomysql \
    --dependency pymysql" \
  user-api-app
```

poetryの依存ライブラリをインストール（.venv）
```
$ docker-compose run --entrypoint "poetry install --no-root" user-api-app
```

再度dockerをビルド
```
$ docker-compose build --no-cache
```

起動
```
$ docker-compose up
```
http://localhost:8000/docs にアクセス


# DB関連
マイグレーション
```
docker-compose exec user-api-app poetry run python -m api.migrate_db
```

起動
```
docker-compose exec db mysql demo
```


# デプロイ方法
使用profileの確認
```
$ aws configure list --profile ecr-profile
```
CLIからAWS（ECR）へログイン
```
 aws ecr get-login-password | docker login --username AWS --password-stdin https://268820476020.dkr.ecr.ap-northeast-1.amazonaws.com
```