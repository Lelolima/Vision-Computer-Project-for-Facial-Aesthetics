# Vision Computer Project for Facial Aesthetics

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/Lelolima/Vision-Computer-Project-for-Facial-Aesthetics/actions/workflows/tests.yml/badge.svg)](https://github.com/Lelolima/Vision-Computer-Project-for-Facial-Aesthetics/actions)
[![Docker](https://img.shields.io/badge/docker-available-blue)](https://hub.docker.com/r/lelolima/vision-aesthetics)

> Sistema avançado de análise facial estética utilizando Computer Vision e Inteligência Artificial com princípios éticos embutidos.

---

## 🎥 Demo em Tempo Real

### 🔍 Análise Facial com Landmarks

<!-- SVG Animado - Análise Facial -->
<svg width="800" height="450" viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="faceGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="landmarkGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00f5ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff00aa;stop-opacity:1" />
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="2" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <style>
      .pulse { animation: pulse 1.5s ease-in-out infinite; }
      .pulse:nth-child(odd) { animation-delay: 0s; }
      .pulse:nth-child(even) { animation-delay: 0.3s; }
      .scan { animation: scan 3s ease-in-out infinite; }
      .load { animation: load 2s ease-in-out infinite; }
      .float { animation: float 4s ease-in-out infinite; }
      @keyframes pulse { 0%, 100% { r: 4; opacity: 1; } 50% { r: 7; opacity: 0.6; } }
      @keyframes scan { 0%, 100% { transform: translateY(-100px); opacity: 0; } 50% { opacity: 1; } 100% { transform: translateY(100px); opacity: 0; } }
      @keyframes load { 0% { width: 0%; } 50% { width: 70%; } 100% { width: 100%; } }
      @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
    </style>
  </defs>
  <rect width="800" height="450" fill="#0f0f1a"/>
  <g stroke="#1a1a3e" stroke-width="1">
    <line x1="0" y1="0" x2="800" y2="0"/><line x1="0" y1="100" x2="800" y2="100"/>
    <line x1="0" y1="200" x2="800" y2="200"/><line x1="0" y1="300" x2="800" y2="300"/>
    <line x1="0" y1="400" x2="800" y2="400"/><line x1="100" y1="0" x2="100" y2="450"/>
    <line x1="200" y1="0" x2="200" y2="450"/><line x1="300" y1="0" x2="300" y2="450"/>
    <line x1="400" y1="0" x2="400" y2="450"/><line x1="500" y1="0" x2="500" y2="450"/>
    <line x1="600" y1="0" x2="600" y2="450"/><line x1="700" y1="0" x2="700" y2="450"/>
  </g>
  <text x="400" y="35" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="bold" class="float">🔍 Análise Facial com IA</text>
  <g transform="translate(400, 220)">
    <ellipse cx="0" cy="0" rx="100" ry="130" fill="url(#faceGrad)" opacity="0.3"/>
    <ellipse cx="-45" cy="-20" rx="25" ry="15" fill="#1a1a3e" stroke="#667eea" stroke-width="2"/>
    <circle cx="-45" cy="-20" r="8" fill="#667eea" filter="url(#glow)"/>
    <ellipse cx="45" cy="-20" rx="25" ry="15" fill="#1a1a3e" stroke="#667eea" stroke-width="2"/>
    <circle cx="45" cy="-20" r="8" fill="#667eea" filter="url(#glow)"/>
    <path d="M 0,-10 L -8,40 L 0,50 L 8,40 Z" fill="#667eea" opacity="0.6"/>
    <path d="M -30,70 Q 0,85 30,70" fill="none" stroke="#ff00aa" stroke-width="3" filter="url(#glow)"/>
  </g>
  <g class="landmarks" filter="url(#glow)">
    <circle class="pulse" cx="400" cy="95" r="4" fill="url(#landmarkGrad)"/>
    <circle class="pulse" cx="355" cy="200" r="4" fill="#00f5ff"/>
    <circle class="pulse" cx="445" cy="200" r="4" fill="#00f5ff"/>
    <circle class="pulse" cx="400" cy="230" r="4" fill="#ff00aa"/>
    <circle class="pulse" cx="370" cy="290" r="4" fill="#ffcc00"/>
    <circle class="pulse" cx="430" cy="290" r="4" fill="#ffcc00"/>
    <circle class="pulse" cx="400" cy="340" r="4" fill="#00ff88"/>
  </g>
  <line class="scan" x1="300" y1="0" x2="500" y2="0" stroke="#00ff88" stroke-width="2" opacity="0.5"/>
  <g transform="translate(620, 80)">
    <rect x="0" y="0" width="160" height="140" rx="10" fill="#1a1a3e" stroke="#667eea" stroke-width="2"/>
    <text x="80" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">MÉTRICAS</text>
    <text x="10" y="45" fill="#aaaaaa" font-size="10">Simetria</text>
    <rect x="10" y="52" width="140" height="8" rx="2" fill="#2a2a4e"/>
    <rect x="10" y="52" width="98" height="8" rx="2" fill="url(#landmarkGrad)"/>
    <text x="155" y="60" fill="#00f5ff" font-size="10" font-weight="bold">85%</text>
    <text x="10" y="75" fill="#aaaaaa" font-size="10">Harmonia</text>
    <rect x="10" y="82" width="140" height="8" rx="2" fill="#2a2a4e"/>
    <rect x="10" y="82" width="91" height="8" rx="2" fill="url(#landmarkGrad)"/>
    <text x="155" y="90" fill="#ff00aa" font-size="10" font-weight="bold">78%</text>
    <text x="10" y="105" fill="#aaaaaa" font-size="10">Prop. Áurea</text>
    <rect x="10" y="112" width="140" height="8" rx="2" fill="#2a2a4e"/>
    <rect x="10" y="112" width="105" height="8" rx="2" fill="url(#landmarkGrad)"/>
    <text x="155" y="120" fill="#ffcc00" font-size="10" font-weight="bold">92%</text>
  </g>
  <g transform="translate(620, 240)">
    <rect x="0" y="0" width="160" height="100" rx="10" fill="#1a1a3e" stroke="#00ff88" stroke-width="2"/>
    <circle cx="20" cy="25" r="8" fill="#00ff88"><animate attributeName="opacity" values="1;0.3;1" dur="1s" repeatCount="indefinite"/></circle>
    <text x="40" y="30" fill="#00ff88" font-size="12" font-weight="bold">ANALISANDO</text>
    <rect x="10" y="45" width="140" height="6" rx="3" fill="#2a2a4e"/>
    <rect x="10" y="45" height="6" rx="3" fill="#00ff88" class="load"/>
    <text x="10" y="70" fill="#888888" font-size="9">Landmarks:</text>
    <text x="145" y="70" fill="#ffffff" font-size="10" font-weight="bold">468</text>
  </g>
  <g transform="translate(620, 360)">
    <rect x="0" y="0" width="160" height="50" rx="10" fill="#1a1a3e" stroke="#ffcc00" stroke-width="2"/>
    <text x="80" y="20" text-anchor="middle" fill="#ffcc00" font-size="10" font-weight="bold">⚖️ AUDITORIA ÉTICA</text>
    <text x="80" y="38" text-anchor="middle" fill="#00ff88" font-size="12" font-weight="bold">✅ APROVADO</text>
  </g>
  <text x="400" y="435" text-anchor="middle" fill="#444466" font-size="10">Vision-Aesthetics v1.0.0 | PyTorch + MediaPipe + AI Ethics</text>
</svg>

### ✨ Simulação GAN - Antes/Depois

<!-- SVG Animado - Simulação GAN -->
<svg width="800" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="beforeG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#444455;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#222233;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="afterG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <filter id="glow-s"><feGaussianBlur stdDeviation="4" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <style>
      .sparkle { animation: sparkle-anim 1.5s ease-in-out infinite; }
      .slider { animation: slide 4s ease-in-out infinite; }
      @keyframes sparkle-anim { 0%, 100% { opacity: 0; transform: scale(0) rotate(0deg); } 50% { opacity: 1; transform: scale(1) rotate(180deg); } }
      @keyframes slide { 0%, 100% { transform: translateX(0); } 50% { transform: translateX(150px); } }
    </style>
  </defs>
  <rect width="800" height="400" fill="#0a0a15"/>
  <text x="400" y="35" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="bold">✨ Simulação GAN - Rinoplastia</text>
  <g transform="translate(100, 60)">
    <!-- ANTES -->
    <rect x="0" y="0" width="280" height="250" fill="url(#beforeG)"/>
    <g transform="translate(140, 125)">
      <ellipse cx="0" cy="0" rx="90" ry="100" fill="#333344" opacity="0.5"/>
      <ellipse cx="-35" cy="-25" rx="18" ry="10" fill="#444455" stroke="#666677" stroke-width="1.5"/>
      <ellipse cx="35" cy="-25" rx="18" ry="10" fill="#444455" stroke="#666677" stroke-width="1.5"/>
      <path d="M -6,-15 L -18,30 L -10,38 L 0,42 L 10,38 L 18,30 L 6,-15 Z" fill="#555566"/>
      <text x="-100" y="220" fill="#aaaaaa" font-size="14" font-weight="bold">⬅ ANTES</text>
    </g>
    <!-- DEPOIS -->
    <rect x="320" y="0" width="280" height="250" fill="url(#afterG)"/>
    <g transform="translate(460, 125)">
      <ellipse cx="0" cy="0" rx="90" ry="100" fill="rgba(102,126,234,0.3)" filter="url(#glow-s)"/>
      <ellipse cx="-35" cy="-25" rx="18" ry="10" fill="#2a2a4a" stroke="#667eea" stroke-width="2"/>
      <circle cx="-35" cy="-25" r="5" fill="#667eea" filter="url(#glow-s)"/>
      <ellipse cx="35" cy="-25" rx="18" ry="10" fill="#2a2a4a" stroke="#667eea" stroke-width="2"/>
      <circle cx="35" cy="-25" r="5" fill="#667eea" filter="url(#glow-s)"/>
      <path d="M -5,-15 L -12,30 L -6,38 L 0,40 L 6,38 L 12,30 L 5,-15 Z" fill="#7a7eb8"/>
      <g class="sparkle" fill="url(#sparkleGrad)">
        <circle cx="60" cy="-50" r="3" fill="#ffff00"/>
        <circle cx="-70" cy="60" r="2" fill="#ffffff"/>
        <circle cx="80" cy="80" r="2.5" fill="#ffff00"/>
      </g>
      <text x="-80" y="220" fill="#667eea" font-size="14" font-weight="bold">DEPOIS ➔</text>
    </g>
    <!-- Slider -->
    <line x1="320" y1="0" x2="320" y2="250" stroke="#ffffff" stroke-width="3" opacity="0.8"/>
    <g class="slider">
      <circle cx="320" cy="125" r="18" fill="#ffffff" filter="url(#glow-s)"/>
      <circle cx="320" cy="125" r="12" fill="#667eea"/>
      <path d="M 314,125 L 318,121 L 318,129 Z" fill="#ffffff"/>
      <path d="M 326,125 L 322,121 L 322,129 Z" fill="#ffffff"/>
    </g>
  </g>
  <g transform="translate(100, 320)">
    <rect x="0" y="0" width="180" height="60" rx="8" fill="#1a1a2e" stroke="#667eea" stroke-width="2"/>
    <text x="90" y="25" text-anchor="middle" fill="#8888aa" font-size="9">PROCEDIMENTO</text>
    <text x="90" y="45" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Rinoplastia</text>
  </g>
  <g transform="translate(300, 320)">
    <rect x="0" y="0" width="180" height="60" rx="8" fill="#1a1a2e" stroke="#00ff88" stroke-width="2"/>
    <text x="90" y="25" text-anchor="middle" fill="#8888aa" font-size="9">MELHORIAS</text>
    <text x="90" y="45" text-anchor="middle" fill="#00ff88" font-size="12" font-weight="bold">Simetria: +18%</text>
  </g>
  <g transform="translate(500, 320)">
    <rect x="0" y="0" width="200" height="60" rx="8" fill="#1a1a2e" stroke="#ff00aa" stroke-width="2"/>
    <text x="100" y="25" text-anchor="middle" fill="#8888aa" font-size="9">MODELO GAN</text>
    <text x="100" y="45" text-anchor="middle" fill="#ff00aa" font-size="12" font-weight="bold">StyleGAN2 | GPU: ✅</text>
  </g>
</svg>

### ⚖️ Dashboard de Ética e Auditoria

<!-- SVG Animado - Ética -->
<svg width="800" height="380" viewBox="0 0 800 380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ethG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00b894;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00cec9;stop-opacity:1" />
    </linearGradient>
    <filter id="glow-g"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <style>
      .check { animation: check-anim 0.6s ease-out forwards; stroke-dasharray: 100; stroke-dashoffset: 100; }
      .pulse-ring { animation: pulse-ring-anim 2s ease-out infinite; }
      .float { animation: float-anim 3s ease-in-out infinite; }
      @keyframes check-anim { to { stroke-dashoffset: 0; } }
      @keyframes pulse-ring-anim { 0% { transform: scale(0.8); opacity: 1; } 100% { transform: scale(1.5); opacity: 0; } }
      @keyframes float-anim { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
    </style>
  </defs>
  <rect width="800" height="380" fill="#0a0a15"/>
  <text x="400" y="35" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="bold" class="float">⚖️ Dashboard de Ética e Auditoria</text>
  <!-- Escudo -->
  <g transform="translate(400, 130)" class="float">
    <path d="M 0,-50 L 40,-35 L 40,20 Q 40,50 0,65 Q -40,50 -40,20 L -40,-35 Z" fill="none" stroke="#00b894" stroke-width="3" filter="url(#glow-g)"/>
    <path d="M -18,5 L -8,15 L 18,-15" fill="none" stroke="#00b894" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" class="check"/>
  </g>
  <g transform="translate(400, 130)">
    <ellipse cx="0" cy="0" rx="55" ry="70" fill="none" stroke="#00b894" stroke-width="1" class="pulse-ring" opacity="0.3"/>
  </g>
  <!-- Painel Princípios -->
  <g transform="translate(50, 200)">
    <rect x="0" y="0" width="280" height="160" rx="10" fill="#1a1a2e" stroke="#00b894" stroke-width="2"/>
    <text x="140" y="25" text-anchor="middle" fill="#00b894" font-size="12" font-weight="bold">📋 PRINCÍPIOS ÉTICOS</text>
    <g transform="translate(15, 40)">
      <circle cx="8" cy="12" r="8" fill="#00b894" opacity="0.2"/><path d="M 4,12 L 7,15 L 12,9" fill="none" stroke="#00b894" stroke-width="2"/><text x="22" y="16" fill="#ffffff" font-size="10">Fairness (Equidade)</text>
      <circle cx="8" cy="35" r="8" fill="#00b894" opacity="0.2"/><path d="M 4,35 L 7,38 L 12,32" fill="none" stroke="#00b894" stroke-width="2"/><text x="22" y="39" fill="#ffffff" font-size="10">Transparency</text>
      <circle cx="8" cy="58" r="8" fill="#00b894" opacity="0.2"/><path d="M 4,58 L 7,61 L 12,55" fill="none" stroke="#00b894" stroke-width="2"/><text x="22" y="62" fill="#ffffff" font-size="10">Privacy</text>
      <circle cx="8" cy="81" r="8" fill="#00b894" opacity="0.2"/><path d="M 4,81 L 7,84 L 12,78" fill="none" stroke="#00b894" stroke-width="2"/><text x="22" y="85" fill="#ffffff" font-size="10">Accountability</text>
      <circle cx="8" cy="104" r="8" fill="#00cec9" opacity="0.2"/><path d="M 4,104 L 7,107 L 12,101" fill="none" stroke="#00cec9" stroke-width="2"/><text x="22" y="108" fill="#ffffff" font-size="10">Non-maleficence</text>
    </g>
  </g>
  <!-- Painel Bias -->
  <g transform="translate(470, 200)">
    <rect x="0" y="0" width="280" height="160" rx="10" fill="#1a1a2e" stroke="#fdcb6e" stroke-width="2"/>
    <text x="140" y="25" text-anchor="middle" fill="#fdcb6e" font-size="12" font-weight="bold">📊 DETECÇÃO DE BIAS</text>
    <g transform="translate(10, 45)">
      <text x="0" y="0" fill="#aaaaaa" font-size="9">Gênero</text>
      <rect x="60" y="-7" width="180" height="10" rx="3" fill="#2a2a4e"/>
      <rect x="60" y="-7" width="30" height="10" rx="3" fill="url(#ethG)"/>
      <text x="245" y="2" fill="#00b894" font-size="10" font-weight="bold">12%</text>
      <text x="0" y="25" fill="#aaaaaa" font-size="9">Etnia</text>
      <rect x="60" y="18" width="180" height="10" rx="3" fill="#2a2a4e"/>
      <rect x="60" y="18" width="38" height="10" rx="3" fill="url(#ethG)"/>
      <text x="245" y="27" fill="#00b894" font-size="10" font-weight="bold">15%</text>
      <text x="0" y="50" fill="#aaaaaa" font-size="9">Idade</text>
      <rect x="60" y="43" width="180" height="10" rx="3" fill="#2a2a4e"/>
      <rect x="60" y="43" width="22" height="10" rx="3" fill="url(#ethG)"/>
      <text x="245" y="52" fill="#00b894" font-size="10" font-weight="bold">8%</text>
      <text x="0" y="75" fill="#ffffff" font-size="10" font-weight="bold">Overall</text>
      <rect x="60" y="68" width="180" height="12" rx="4" fill="#2a2a4e"/>
      <rect x="60" y="68" width="55" height="12" rx="4" fill="url(#ethG)"/>
      <text x="245" y="77" fill="#00b894" font-size="11" font-weight="bold">LOW RISK</text>
    </g>
  </g>
  <!-- Badges -->
  <g transform="translate(50, 340)">
    <rect x="0" y="0" width="120" height="28" rx="6" fill="#1a1a2e" stroke="#00b894" stroke-width="2"/>
    <text x="60" y="18" text-anchor="middle" fill="#00b894" font-size="9" font-weight="bold">✅ EU AI Act</text>
    <rect x="130" y="0" width="120" height="28" rx="6" fill="#1a1a2e" stroke="#00b894" stroke-width="2"/>
    <text x="190" y="18" text-anchor="middle" fill="#00b894" font-size="9" font-weight="bold">✅ GDPR/LGPD</text>
    <rect x="260" y="0" width="140" height="28" rx="6" fill="#1a1a2e" stroke="#667eea" stroke-width="2"/>
    <text x="280" y="18" fill="#8888aa" font-size="9">Audit ID:</text>
    <text x="330" y="18" fill="#667eea" font-size="9" font-family="monospace">abc123def456</text>
  </g>
</svg>

---

## 🌟 Funcionalidades

- **Análise de Landmarks Faciais**: Detecção precisa de 468 pontos usando MediaPipe FaceMesh
- **Métricas Estéticas**: Cálculo baseado em proporção áurea, simetria e harmonia facial
- **Simulações Realistas com GAN**: Pré-visualização com StyleGAN/Pix2Pix
- **Framework de Ética em IA**: Auditoria de bias (EU AI Act, LGPD/GDPR)
- **Relatórios Profissionais**: Exportação PDF/JSON
- **Multi-Plataforma**: Streamlit, Desktop (PyQt5), API REST

---

## 📋 Índice

- [Instalação](#-instalação)
- [Uso](#-uso)
- [Arquitetura](#-arquitetura)
- [Ética em IA](#-ética-em-ia)
- [API](#-api)
- [Testes](#-testes)
- [Deploy](#-deploy)
- [Licença](#-licença)

---

## 🚀 Instalação

```bash
git clone https://github.com/Lelolima/Vision-Computer-Project-for-Facial-Aesthetics.git
cd Vision-Computer-Project-for-Facial-Aesthetics
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
pip install -e .
```

---

## 💻 Uso

### Streamlit App
```bash
streamlit run src/ui/streamlit_app.py  # http://localhost:8501
```

### API REST
```bash
uvicorn src.api.main:app --reload  # http://localhost:8000/docs
```

### Exemplo Python
```python
from src.core.analyzer import FacialAnalyzer
from src.ai.gan_simulator import GANSimulator
from src.ethics.ai_ethics import AIEthicsFramework

analyzer = FacialAnalyzer()
simulator = GANSimulator()
ethics = AIEthicsFramework()

results = analyzer.analyze("photo.jpg")
ethics_report = ethics.audit_analysis(results)
```

---

## 🏗️ Arquitetura

```
src/
├── core/           # Análise facial, landmarks, métricas
├── ai/             # GAN Simulator (StyleGAN, Pix2Pix)
├── ethics/         # Framework de ética (EU AI Act)
├── ui/             # Streamlit, PyQt5
└── api/            # FastAPI REST
```

---

## ⚖️ Ética em IA

| Princípio | Implementação |
|-----------|---------------|
| **Fairness** | Detecção de bias (gênero, etnia, idade) |
| **Transparency** | Explicações + intervalos de confiança |
| **Privacy** | Processamento local, consentimento |
| **Accountability** | Logs auditáveis, IDs únicos |
| **Non-maleficence** | Bloqueio de simulações prejudiciais |

---

## 📡 API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/analyze` | Analisar imagem |
| POST | `/api/v1/simulate` | Simular procedimento |
| POST | `/api/v1/ethics/audit` | Auditoria ética |
| GET | `/api/v1/health` | Health check |

---

## 🧪 Testes

```bash
pytest                       # Todos
pytest --cov=src            # Coverage
pytest tests/unit/          # Unitários
```

---

## 🚢 Docker

```bash
docker-compose up -d
# Streamlit: 8501 | API: 8000
```

---

## 📝 Licença

MIT - Veja [LICENSE](LICENSE)

---

<div align="center">

**Vision-Aesthetics v1.0.0** | Built with ❤️ + PyTorch + MediaPipe + AI Ethics

[Documentação Completa](docs/) • [Ética em IA](docs/ethics.md) • [Arquitetura](docs/architecture.md)

</div>