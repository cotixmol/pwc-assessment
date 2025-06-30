FROM python:3.13.5-slim
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
RUN chmod +x /app/script/start.sh
EXPOSE 8000
CMD ["/app/script/start.sh"]
