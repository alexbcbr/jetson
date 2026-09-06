FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml .
RUN uv sync --no-install-project

COPY main.py ./
COPY services/ services/
COPY utils/ utils/
COPY db-init/ db-init/
RUN mkdir -p data && cd db-init && uv run python seed.py

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
