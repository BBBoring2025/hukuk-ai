# Gunicorn yapılandırma dosyası
bind = "0.0.0.0:8000"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5
errorlog = "../logs/dilekce_uretici_error.log"
accesslog = "../logs/dilekce_uretici_access.log"
loglevel = "info"
