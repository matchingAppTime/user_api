# API設計
🌳
```
./api
├── cruds
│   └── user.py
├── db.py
├── main.py
├── migrate_db.py
├── models
│   └── user.py
├── routers
│   └── user.py
└── schemas
    └── user.py
```

* lambda_handler
  * 実行ファイル
    
* db, migrate_db
  * db関連ファイル（別関数にわけるかも）
    
* routers
  * コントローラー定義 mvcのcあたり
    
* schemas
  * pydanticのスキーマ定義 domainクラスやDTOと言えばそれ
    
* models
  * dbに対応したスキーマ定義 schemasとごっちゃにならないように
    
* cruds
  * routerやdbとやりとりする関数群 service層



user関連のパス
http://localhost:8000/docs

# 認証
* / GET
  * 不要
  
* /users GET
  * ログイン必要
  
* /users/search GET
  * ログイン必要
  
* /users/{user_id} GET
  * ログイン必要
  
* /user POST
  * ログイン必要
  
* /user/{user_id} PUT
  * ログイン必要
  
* /user/{user_id} DELETE
  * ログイン必要
  