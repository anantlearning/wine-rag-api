FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# CPU-only PyTorch
RUN pip install --no-cache-dir \
    torch \
    --index-url https://download.pytorch.org/whl/cpu

# Application dependencies
RUN pip install --no-cache-dir \
    sentence-transformers \
    google-genai \
    qdrant-client \
    pandas \
    python-dotenv \
    fastapi \
    uvicorn \
    pytest

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]


