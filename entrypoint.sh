#!/bin/bash

# マイグレーション実施
poetry run python -am api.migrate_cloud_db

# uvicornサーバー起動
poetry run uvicorn api.main:app --host 0.0.0.0