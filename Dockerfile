# Usando uma imagem base antiga com vulnerabilidades conhecidas
FROM python:3.8-slim

# Vulnerabilidade: Executando como root
USER root

# Vulnerabilidade: Não especificando versões exatas
# Instalando dependências necessárias para Pillow e outras bibliotecas
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    gcc \
    python3-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    zlib1g-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiando arquivos
COPY app.py /app/
COPY requirements.txt /app/

WORKDIR /app

# Vulnerabilidade: pip install sem especificar versões
RUN pip install -r requirements.txt

# Vulnerabilidade: Expondo informações sensíveis
ENV SECRET_KEY=super_secret_key_123
ENV DB_PASSWORD=admin123

# Vulnerabilidade: Porta exposta desnecessariamente
EXPOSE 5000 22 3306

# Vulnerabilidade: Executando como root
CMD ["python", "app.py"]
