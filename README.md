# user_api

ローカルセットアップ
dockerの初期ビルド
```
$ docker-compose build
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


# デプロイ方法（アプリに変更があったらこれをする）
ECRリポジトリ名: user-api

CLIからAWS（ECR）へログイン
```
aws ecr get-login-password | docker login --username AWS --password-stdin https://268820476020.dkr.ecr.ap-northeast-1.amazonaws.com
```

URL仕込み
```
ECR_URI=$(aws ecr describe-repositories --repository-name user-api --query 'repositories[0].repositoryUri' --output text)
```

lambda用dokerfileでビルド
```
docker build -t user-api -f Dockerfile.lambda . --no-cache
```


AWSのタグつけてビルド -> デプロイ
```
docker tag user-api:latest ${ECR_URI}:latest
docker push ${ECR_URI}:latest
```

あとはECRのコンソールにGO😎