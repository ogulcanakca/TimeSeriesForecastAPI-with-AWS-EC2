FROM python:3.12.4-slim AS backend

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libgomp1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements/requirements_app.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_DIR=/app/model
ENV SCALER_DIR=/app/scaler

COPY app/ app/
COPY model/ model/
COPY scaler/ scaler/
COPY app/frontend /app/frontend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM nginx:alpine AS frontend

COPY conf/nginx.conf /etc/nginx/nginx.conf

COPY app/frontend /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]