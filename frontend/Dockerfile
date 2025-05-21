FROM node:16-alpine

WORKDIR /app

# Bağımlılıkları kur
COPY package.json .
RUN npm install

# Uygulama dosyalarını kopyala
COPY . .

# Build
RUN npm run build

# Çalıştırma
CMD ["npm", "start"]
