# Arquitetura do Sistema

## Visão Geral

```
┌─────────────────────────────────────────────────────────────────┐
│                    Vision Computer Project                       │
│                                                                │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│  │  Streamlit   │    │   FastAPI    │    │    Desktop   │     │
│  │     Web      │    │     REST     │    │     PyQt5    │     │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘     │
│         │                   │                   │              │
│         └───────────────────┼───────────────────┘              │
│                             ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   Core Analyzer                          │   │
│  │  • Landmarks (MediaPipe FaceMesh)                        │   │
│  │  • Métricas Estéticas                                    │   │
│  │  • Proporção Áurea                                       │   │
│  │  • Simetria Facial                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                             │                                   │
│         ┌───────────────────┼───────────────────┐              │
│         ▼                   ▼                   ▼              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│  │     GAN      │    │    Ethics    │    │   Reports    │     │
│  │  Simulator   │    │   Framework  │    │  Generator   │     │
│  │              │    │              │    │              │     │
│  │ • StyleGAN   │    │ • Bias Check │    │ • PDF        │     │
│  │ • Pix2Pix    │    │ • Audit      │    │ • JSON       │     │
│  │ • Fallback   │    │ • Compliance │    │ • Excel      │     │
│  └──────────────┘    └──────────────┘    └──────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

## Estrutura de Diretórios

```
Vision-Computer-Project-for-Facial-Aesthetics/
├── src/
│   ├── __init__.py              # Pacote principal
│   ├── core/                    # Lógica central
│   │   ├── __init__.py
│   │   ├── analyzer.py          # FacialAnalyzer principal
│   │   ├── landmarks.py         # Detecção de landmarks
│   │   └── metrics.py           # Cálculo de métricas
│   ├── ai/                      # Modelos de IA
│   │   ├── __init__.py
│   │   ├── gan_simulator.py     # GAN para simulações
│   │   └── face_models.py       # Modelos de face (InsightFace, etc)
│   ├── ethics/                  # Framework de ética
│   │   ├── __init__.py
│   │   └── ai_ethics.py         # Auditoria e compliance
│   ├── ui/                      # Interfaces
│   │   ├── streamlit_app.py     # Web app
│   │   └── desktop_app.py       # Desktop app
│   └── api/                     # API REST
│       ├── __init__.py
│       └── main.py              # FastAPI app
├── tests/
│   ├── conftest.py              # Fixtures
│   ├── unit/                    # Testes unitários
│   └── integration/             # Testes de integração
├── docs/                        # Documentação
├── models/                      # Modelos pré-treinados
├── data/                        # Dados (não versionado)
├── docker-compose.yml           # Orquestração
├── Dockerfile                   # Containerização
└── requirements.txt             # Dependências
```

## Fluxo de Dados

### 1. Análise Facial

```
┌──────────┐     ┌──────────────┐     ┌─────────────┐
│  Upload  │────▶│  Pre-process │────▶│  FaceMesh   │
│  Imagem  │     │  (resize,    │     │  Detection  │
│          │     │   normalize) │     │  (468 pts)  │
└──────────┘     └──────────────┘     └─────────────┘
                                              │
                                              ▼
┌──────────┐     ┌──────────────┐     ┌─────────────┐
│  Export  │◀────│   Auditoria  │◀────│  Cálculo    │
│ Relatório│     │    Ética     │     │  Métricas   │
└──────────┘     └──────────────┘     └─────────────┘
```

### 2. Simulação com GAN

```
┌──────────┐     ┌──────────────┐     ┌─────────────┐
│  Upload  │────▶│  Verificação │────▶│   Ética     │
│  Imagem  │     │  Consent.    │     │  (Audit)    │
└──────────┘     └──────────────┘     └─────────────┘
                                              │
                            ┌─────────────────┘
                            ▼
┌──────────┐     ┌──────────────┐     ┌─────────────┐
│  Blend   │◀────│  Pós-proc.   │◀────│   GAN       │
│  Output  │     │  (merge)     │     │  Inference  │
└──────────┘     └──────────────┘     └─────────────┘
```

## Componentes Principais

### FacialAnalyzer

```python
class FacialAnalyzer:
    """Analisa landmarks faciais e calcula métricas estéticas."""

    def __init__(self, model_path: Optional[str] = None):
        # MediaPipe FaceMesh initialization

    def analyze(self, image_path: str) -> dict:
        """Retorna landmarks e scores estéticos."""
```

### GANSimulator

```python
class GANSimulator:
    """Gera simulações realistas de procedimentos."""

    def simulate_procedure(
        self,
        image: Image.Image,
        procedure: str,
        intensity: float = 0.5
    ) -> Image.Image:
        """Aplica simulação de procedimento na imagem."""
```

### AIEthicsFramework

```python
class AIEthicsFramework:
    """Framework de ética e compliance."""

    def audit_analysis(self, results: dict) -> EthicsAuditResult:
        """Realiza auditoria ética da análise."""

    def generate_ethics_report(self, results: dict) -> str:
        """Gera relatório JSON de compliance."""
```

## API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/analyze` | Analisar imagem |
| POST | `/api/v1/simulate` | Simular procedimento |
| GET | `/api/v1/report/{id}` | Obter relatório |
| POST | `/api/v1/ethics/audit` | Auditoria ética |
| GET | `/api/v1/ethics/disclosure` | Texto de divulgação |

## Banco de Dados (Opcional)

```
┌─────────────────────────────────────────┐
│           PostgreSQL / SQLite           │
├─────────────────────────────────────────┤
│  • users (opcional, se autenticado)     │
│  • analyses (resultados de análise)     │
│  • simulations (simulações geradas)     │
│  • audit_logs (logs de auditoria ética) │
└─────────────────────────────────────────┘
```

## Segurança

### Autenticação (Opcional)

```
┌──────────┐     ┌──────────────┐     ┌─────────────┐
│   Login  │────▶│  JWT Token   │────▶│  Bearer     │
│          │     │  Generation  │     │  Auth       │
└──────────┘     └──────────────┘     └─────────────┘
```

### Proteção de Dados

- Processamento local preferencial
- Dados biométricos não persistidos por padrão
- Opção de exclusão imediata
- Logs sem PII (Personally Identifiable Information)

## Deploy

### Docker (Desenvolvimento)

```bash
docker-compose up
# Streamlit: http://localhost:8501
# API: http://localhost:8000
```

### Docker (Produção)

```bash
docker-compose --profile production up -d
# Inclui NGINX como reverse proxy
```

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vision-aesthetics
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: vision-aesthetics:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

## Performance

| Cenário | Tempo | Hardware |
|---------|-------|----------|
| Análise (CPU) | 2-3s | Intel i7 |
| Análise (GPU) | 0.5-1s | RTX 3060 |
| Simulação (fallback) | 1-2s | CPU |
| Simulação (GAN) | 3-5s | GPU |

## Escalabilidade

```
┌─────────────────────────────────────────────────────┐
│                  Load Balancer                       │
└─────────────────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │ Worker 1 │    │ Worker 2 │    │ Worker N │
  │  (GPU)   │    │  (GPU)   │    │  (CPU)   │
  └──────────┘    └──────────┘    └──────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Redis   │    │PostgreSQL│    │   S3     │
  │  Cache   │    │   DB     │    │ Storage  │
  └──────────┘    └──────────┘    └──────────┘
```