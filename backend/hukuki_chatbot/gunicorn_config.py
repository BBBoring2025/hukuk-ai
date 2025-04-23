# Gunicorn yapılandırma dosyası
bind = "0.0.0.0:8002"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5
errorlog = "../logs/hukuki_chatbot_error.log"
accesslog = "../logs/hukuki_chatbot_access.log"
loglevel = "info"
