#!/bin/bash

# Türkiye Hukuk AI Platformu Çalıştırma Scripti

# Dizin yapısını oluştur
mkdir -p logs
mkdir -p data/dilekce_uretici/templates
mkdir -p data/dilekce_uretici/output
mkdir -p data/sozlesme_analizi/uploads
mkdir -p data/sozlesme_analizi/reports
mkdir -p data/hukuki_chatbot/sessions
mkdir -p data/hukuki_chatbot/knowledge
mkdir -p data/cache

# Backend servislerini başlat
echo "Backend servisleri başlatılıyor..."
cd backend/dilekce_uretici && python3 run_optimized.py &
cd backend/sozlesme_analizi && python3 run_optimized.py &
cd backend/hukuki_chatbot && python3 run_optimized.py &

# Frontend'i başlat (geliştirme modu)
echo "Frontend başlatılıyor..."
cd frontend && npm start
