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