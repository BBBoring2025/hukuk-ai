FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir uvicorn
# copy optimized AI helpernCOPY ../ai_components/mock_ai_service_optimized.py ./mock_ai_service_optimized.py# copy optimized AI helper
COPY ../ai_components/mock_ai_service_optimized.py ./mock_ai_service_optimized.py

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir uvicorn
# copy optimized AI helpernCOPY ../ai_components/mock_ai_service_optimized.py ./mock_ai_service_optimized.py# copy optimized AI helper
COPY ../ai_components/mock_ai_service_optimized.py ./mock_ai_service_optimized.py

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
