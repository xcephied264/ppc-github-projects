FROM python:3.12-slim

WORKDIR /app

COPY todo.py todo-test.py ./
COPY scripts/ ./scripts/

ENV GITHUB_WORKSPACE=/app

ENTRYPOINT ["bash", "scripts/entrypoint.sh"]