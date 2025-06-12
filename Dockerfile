FROM python:3.12-slim

WORKDIR /app

COPY . .

# Install uv (fast Python package installer)
RUN pip install --no-cache-dir uv

# Install dependencies using uv sync
RUN uv sync

CMD ["uv", "run", "main.py"]
