#!/bin/bash

# Türkiye Hukuk AI Platformu Kurulum Scripti

# Gerekli paketleri kur
echo "Gerekli paketler kuruluyor..."
apt-get update
apt-get install -y python3 python3-pip nodejs npm nginx supervisor

# Python bağımlılıklarını kur
echo "Python bağımlılıkları kuruluyor..."
pip3 install fastapi uvicorn gunicorn pydantic python-docx docxtpl docx2pdf nltk PyPDF2 spacy scikit-learn numpy aiofiles python-multipart

# Frontend bağımlılıklarını kur
echo "Frontend bağımlılıkları kuruluyor..."
cd frontend && npm install

# Nginx yapılandırmasını kur
echo "Nginx yapılandırması kuruluyor..."
cp config/nginx.conf /etc/nginx/nginx.conf
systemctl restart nginx

# Supervisor yapılandırmasını kur
echo "Supervisor yapılandırması kuruluyor..."
cp config/supervisor.conf /etc/supervisor/conf.d/hukuk_ai_platformu.conf
supervisorctl reread
supervisorctl update

echo "Kurulum tamamlandı!"
