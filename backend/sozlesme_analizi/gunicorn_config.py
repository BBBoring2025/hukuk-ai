# Gunicorn yapılandırma dosyası
bind = "0.0.0.0:8001"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5
errorlog = "../logs/sozlesme_analizi_error.log"
accesslog = "../logs/sozlesme_analizi_access.log"
loglevel = "info"
