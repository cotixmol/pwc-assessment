#!/bin/sh
until alembic upgrade head; do
  echo "Alembic migration failed, waiting for DB to be ready..."
  sleep 3

done

exec uvicorn main:app --host 0.0.0.0 --port 8000
