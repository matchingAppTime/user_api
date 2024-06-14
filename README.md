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
IDとURL仕込み
```
ID=ほげ
ECR=URI=$(aws ecr describe-repositories --repository-name user-api --query 'repositories[0].repositoryUri' --output text)
```

タグ付きのビルド
```
docker build -t ${ID}.dkr.ecr.ap-northeast-1.amazonaws.com/user-api:latest -f Dockerfile.lambda .
```

使用profileの確認
```
$ aws configure list --profile ecr-profile
```
CLIからAWS（ECR）へログイン
```
 aws ecr get-login-password | docker login --username AWS --password-stdin https://268820476020.dkr.ecr.ap-northeast-1.amazonaws.com
```

AWSのタグつけてビルド -> デプロイ
```
docker build -t ${ID}.dkr.ecr.ap-northeast-1.amazonaws.com/user-api:latest --platform linux/amd64 -f Dockerfile.cloud .
docker push ${ID}.dkr.ecr.ap-northeast-1.amazonaws.com/user-api:latest
```

確認
```
aws ecr list-images --repository-name=user-api
```

あとはECRのコンソールにGO😎