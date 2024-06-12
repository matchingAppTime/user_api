# python3.11のイメージをダウンロード
FROM public.ecr.aws/lambda/python:3.11

# pythonの出力表示をDocker用に調整
ENV PYTHONUNBUFFERED=1

WORKDIR /var/task

# ライブラリのインストール
COPY requirements.txt ./
RUN pip install -r requirements.txt

# アプリのコードをコピー
COPY . .

# lambdaのエントリーポイント
CMD ["lambda_handler.handler"]