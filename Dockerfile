# =============================================================================
# Dockerfile - Vision Computer Project for Facial Aesthetics
# =============================================================================
# Build: docker build -t vision-aesthetics:latest .
# Run:   docker run -p 8501:8501 -p 8000:8000 vision-aesthetics:latest
# GPU:   docker run --gpus all -p 8501:8501 vision-aesthetics:latest
# =============================================================================

# ---------------------------------------------------------
# Stage 1: Builder - Instalar dependências e build
# ---------------------------------------------------------
FROM python:3.11-slim-bookworm as builder

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar apenas requirements para cache de camadas
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------------------
# Stage 2: Runtime - Imagem final minimalista
# ---------------------------------------------------------
FROM python:3.11-slim-bookworm as runtime

WORKDIR /app

# Labels para metadados
LABEL maintainer="Léllo Lima"
LABEL version="1.0.0"
LABEL description="Sistema de análise facial estética com IA ética"
LABEL org.opencontainers.image.source="https://github.com/Lelolima/Vision-Computer-Project-for-Facial-Aesthetics"

# Copiar dependências do sistema do builder
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copiar Python packages do builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar código fonte
COPY . .

# Criar diretórios de dados
RUN mkdir -p /app/data /app/logs /app/models /app/ethics_logs && \
    chmod -R 755 /app

# Criar usuário não-root para segurança
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    ENVIRONMENT=production \
    LOG_LEVEL=INFO \
    DATA_DIR=/app/data \
    ETHICS_STRICT_MODE=true \
    INFERENCE_DEVICE=cpu

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/api/v1/health', timeout=5)" || exit 1

# Portas expostas
# 8501: Streamlit
# 8000: FastAPI
# 8080: Alternativa para ambientes restritos
EXPOSE 8501 8000 8080

# Comando de entrada
ENTRYPOINT ["python", "-m"]

# Comando padrão: Streamlit app
CMD ["streamlit", "run", "src/ui/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]