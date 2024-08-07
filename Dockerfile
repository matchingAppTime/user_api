# Dockerfile
# python3.11のイメージをダウンロード
FROM python:3.11-buster

# pythonの出力表示をDocker用に調整
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# 必要なライブラリをインストール
COPY requirements.txt ./
RUN pip install -r requirements.txt

# FastAPIアプリケーションのコードをコピー
COPY . .

# ローカル開発用のエントリーポイントを設定
CMD ["uvicorn", "lambda_handler:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]