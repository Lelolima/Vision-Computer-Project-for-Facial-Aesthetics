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
    <linearGradient id="faceGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="landmarkGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00f5ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff00aa;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/>
    </filter>

    <style>
      .landmark-point {
        animation: pulse 1.5s ease-in-out infinite;
      }
      .landmark-point:nth-child(odd) {
        animation-delay: 0s;
      }
      .landmark-point:nth-child(even) {
        animation-delay: 0.3s;
      }
      .scan-line {
        animation: scan 3s ease-in-out infinite;
      }
      .loading-bar {
        animation: load 2s ease-in-out infinite;
      }
      .score-number {
        animation: countUp 1s ease-out;
      }
      .floating {
        animation: float 4s ease-in-out infinite;
      }
      @keyframes pulse {
        0%, 100% { r: 4; opacity: 1; }
        50% { r: 7; opacity: 0.6; }
      }
      @keyframes scan {
        0%, 100% { transform: translateY(-100px); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(100px); opacity: 0; }
      }
      @keyframes load {
        0% { width: 0%; }
        50% { width: 70%; }
        100% { width: 100%; }
      }
      @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
      }
      @keyframes blink {
        0%, 48%, 52%, 100% { transform: scaleY(1); }
        50% { transform: scaleY(0.1); }
      }
    </style>
  </defs>

  <rect width="800" height="450" fill="#0f0f1a"/>

  <g stroke="#1a1a3e" stroke-width="1">
    <line x1="0" y1="0" x2="800" y2="0"/>
    <line x1="0" y1="50" x2="800" y2="50"/>
    <line x1="0" y1="100" x2="800" y2="100"/>
    <line x1="0" y1="150" x2="800" y2="150"/>
    <line x1="0" y1="200" x2="800" y2="200"/>
    <line x1="0" y1="250" x2="800" y2="250"/>
    <line x1="0" y1="300" x2="800" y2="300"/>
    <line x1="0" y1="350" x2="800" y2="350"/>
    <line x1="0" y1="400" x2="800" y2="400"/>
    <line x1="0" y1="450" x2="800" y2="450"/>
    <line x1="0" y1="0" x2="0" y2="450"/>
    <line x1="100" y1="0" x2="100" y2="450"/>
    <line x1="200" y1="0" x2="200" y2="450"/>
    <line x1="300" y1="0" x2="300" y2="450"/>
    <line x1="400" y1="0" x2="400" y2="450"/>
    <line x1="500" y1="0" x2="500" y2="450"/>
    <line x1="600" y1="0" x2="600" y2="450"/>
    <line x1="700" y1="0" x2="700" y2="450"/>
    <line x1="800" y1="0" x2="800" y2="450"/>
  </g>

  <text x="400" y="35" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="bold" class="floating">
    🔍 Análise Facial com IA
  </text>

  <g transform="translate(400, 220)" filter="url(#shadow)">
    <ellipse cx="0" cy="0" rx="100" ry="130" fill="url(#faceGradient)" opacity="0.3"/>

    <g class="eye" style="transform-origin: center;">
      <ellipse cx="-45" cy="-20" rx="25" ry="15" fill="#1a1a3e" stroke="#667eea" stroke-width="2">
        <animate attributeName="ry" values="15;1;15" dur="4s" repeatCount="indefinite"/>
      </ellipse>
      <circle cx="-45" cy="-20" r="8" fill="#667eea" filter="url(#glow)"/>

      <ellipse cx="45" cy="-20" rx="25" ry="15" fill="#1a1a3e" stroke="#667eea" stroke-width="2">
        <animate attributeName="ry" values="15;1;15" dur="4s" repeatCount="indefinite"/>
      </ellipse>
      <circle cx="45" cy="-20" r="8" fill="#667eea" filter="url(#glow)"/>
    </g>

    <path d="M 0,-10 L -8,40 L 0,50 L 8,40 Z" fill="#667eea" opacity="0.6"/>

    <path d="M -30,70 Q 0,85 30,70" fill="none" stroke="#ff00aa" stroke-width="3" filter="url(#glow)">
      <animate attributeName="d" values="M -30,70 Q 0,85 30,70;M -30,70 Q 0,75 30,70;M -30,70 Q 0,85 30,70" dur="3s" repeatCount="indefinite"/>
    </path>

    <path d="M -90,-80 Q -110,0 -90,100 Q 0,140 90,100 Q 110,0 90,-80"
          fill="none" stroke="#667eea" stroke-width="2" stroke-dasharray="5,5" opacity="0.5">
      <animate attributeName="stroke-dashoffset" values="0;100" dur="10s" repeatCount="indefinite"/>
    </path>
  </g>

  <g class="landmarks" filter="url(#glow)">
    <circle class="landmark-point" cx="400" cy="95" r="4" fill="url(#landmarkGradient)"/>
    <circle class="landmark-point" cx="360" cy="100" r="4" fill="url(#landmarkGradient)"/>
    <circle class="landmark-point" cx="440" cy="100" r="4" fill="url(#landmarkGradient)"/>

    <circle class="landmark-point" cx="355" cy="200" r="4" fill="#00f5ff"/>
    <circle class="landmark-point" cx="375" cy="195" r="4" fill="#00f5ff"/>
    <circle class="landmark-point" cx="425" cy="195" r="4" fill="#00f5ff"/>
    <circle class="landmark-point" cx="445" cy="200" r="4" fill="#00f5ff"/>

    <circle class="landmark-point" cx="400" cy="230" r="4" fill="#ff00aa"/>
    <circle class="landmark-point" cx="390" cy="245" r="4" fill="#ff00aa"/>
    <circle class="landmark-point" cx="410" cy="245" r="4" fill="#ff00aa"/>

    <circle class="landmark-point" cx="370" cy="290" r="4" fill="#ffcc00"/>
    <circle class="landmark-point" cx="400" cy="285" r="4" fill="#ffcc00"/>
    <circle class="landmark-point" cx="430" cy="290" r="4" fill="#ffcc00"/>

    <circle class="landmark-point" cx="400" cy="340" r="4" fill="#00ff88"/>

    <path d="M 355,200 L 445,200" stroke="#00f5ff" stroke-width="1" opacity="0.3"/>
    <path d="M 370,290 L 430,290" stroke="#ffcc00" stroke-width="1" opacity="0.3"/>
    <path d="M 400,95 L 400,230 L 400,340" stroke="#ff00aa" stroke-width="1" opacity="0.3" stroke-dasharray="3,3">
      <animate attributeName="opacity" values="0.3;0.6;0.3" dur="2s" repeatCount="indefinite"/>
    </path>
  </g>

  <line class="scan-line" x1="300" y1="0" x2="500" y2="0" stroke="#00ff88" stroke-width="2" opacity="0.5"/>

  <g transform="translate(620, 80)" filter="url(#shadow)">
    <rect x="0" y="0" width="160" height="140" rx="10" fill="#1a1a3e" stroke="#667eea" stroke-width="2"/>

    <text x="80" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">MÉTRICAS</text>

    <text x="10" y="45" fill="#aaaaaa" font-size="10">Simetria</text>
    <rect x="10" y="52" width="140" height="8" rx="2" fill="#2a2a4e"/>
    <rect x="10" y="52" width="98" height="8" rx="2" fill="url(#landmarkGradient)">
      <animate attributeName="width" values="0;98" dur="1.5s" fill="freeze"/>
    </rect>
    <text x="155" y="60" fill="#00f5ff" font-size="10" font-weight="bold" class="score-number">85%</text>

    <text x="10" y="75" fill="#aaaaaa" font-size="10">Harmonia</text>
    <rect x="10" y="82" width="140" height="8" rx="2" fill="#2a2a4e"/>
    <rect x="10" y="82" width="91" height="8" rx="2" fill="url(#landmarkGradient)">
      <animate attributeName="width" values="0;91" dur="1.5s" fill="freeze"/>
    </rect>
    <text x="155" y="90" fill="#ff00aa" font-size="10" font-weight="bold" class="score-number">78%</text>

    <text x="10" y="105" fill="#aaaaaa" font-size="10">Prop. Áurea</text>
    <rect x="10" y="112" width="140" height="8" rx="2" fill="#2a2a4e"/>
    <rect x="10" y="112" width="105" height="8" rx="2" fill="url(#landmarkGradient)">
      <animate attributeName="width" values="0;105" dur="1.5s" fill="freeze"/>
    </rect>
    <text x="155" y="120" fill="#ffcc00" font-size="10" font-weight="bold" class="score-number">92%</text>
  </g>

  <g transform="translate(620, 240)" filter="url(#shadow)">
    <rect x="0" y="0" width="160" height="100" rx="10" fill="#1a1a3e" stroke="#00ff88" stroke-width="2"/>

    <circle cx="20" cy="25" r="8" fill="#00ff88">
      <animate attributeName="opacity" values="1;0.3;1" dur="1s" repeatCount="indefinite"/>
    </circle>
    <text x="40" y="30" fill="#00ff88" font-size="12" font-weight="bold">ANALISANDO</text>

    <rect x="10" y="45" width="140" height="6" rx="3" fill="#2a2a4e"/>
    <rect x="10" y="45" height="6" rx="3" fill="#00ff88" class="loading-bar"/>

    <text x="10" y="70" fill="#888888" font-size="9">Landmarks detectados:</text>
    <text x="145" y="70" fill="#ffffff" font-size="10" font-weight="bold">468</text>

    <text x="10" y="88" fill="#888888" font-size="9">Tempo processamento:</text>
    <text x="145" y="88" fill="#ffffff" font-size="10" font-weight="bold">0.5s</text>
  </g>

  <g transform="translate(620, 360)" filter="url(#shadow)">
    <rect x="0" y="0" width="160" height="50" rx="10" fill="#1a1a3e" stroke="#ffcc00" stroke-width="2"/>
    <text x="80" y="20" text-anchor="middle" fill="#ffcc00" font-size="10" font-weight="bold">⚖️ AUDITORIA ÉTICA</text>
    <text x="80" y="38" text-anchor="middle" fill="#00ff88" font-size="12" font-weight="bold">✅ APROVADO</text>
  </g>

  <g fill="#667eea" opacity="0.5">
    <circle cx="100" cy="100" r="2">
      <animate attributeName="cy" values="100;400" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="150" cy="80" r="2">
      <animate attributeName="cy" values="80;380" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="200" cy="120" r="2">
      <animate attributeName="cy" values="120;420" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <text x="400" y="435" text-anchor="middle" fill="#444466" font-size="10">
    Vision-Aesthetics v1.0.0 | Powered by PyTorch + MediaPipe + AI Ethics
  </text>
</svg>

### ✨ Simulação GAN - Antes/Depois

<!-- SVG Animado - Simulação GAN -->
<svg width="800" height="450" viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="beforeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#444455;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#222233;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="afterGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="sparkleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ffffff;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ffffff;stop-opacity:1" />
    </linearGradient>
    <filter id="glow-strong">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="leftHalf">
      <rect x="0" y="0" width="325" height="250"/>
    </clipPath>
    <clipPath id="rightHalf">
      <rect x="75" y="0" width="325" height="250"/>
    </clipPath>

    <style>
      .sparkle {
        animation: sparkle-anim 1.5s ease-in-out infinite;
      }
      .slider-knob {
        animation: slide-knob 4s ease-in-out infinite;
      }
      .procedure-text {
        animation: text-pulse 2s ease-in-out infinite;
      }
      .comparison-line {
        animation: line-shine 2s ease-in-out infinite;
      }
      @keyframes sparkle-anim {
        0%, 100% { opacity: 0; transform: scale(0) rotate(0deg); }
        50% { opacity: 1; transform: scale(1) rotate(180deg); }
      }
      @keyframes slide-knob {
        0%, 100% { transform: translateX(0); }
        50% { transform: translateX(150px); }
      }
      @keyframes text-pulse {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
      }
      @keyframes line-shine {
        0%, 100% { stroke-opacity: 0.5; }
        50% { stroke-opacity: 1; stroke-width: 4; }
      }
      @keyframes morph {
        0%, 100% { d: path("M 250,100 C 230,120 220,150 230,180 C 240,200 260,200 270,180 C 280,150 270,120 250,100"); }
        50% { d: path("M 250,100 C 235,120 225,150 235,180 C 245,195 265,195 265,180 C 275,150 265,120 250,100"); }
      }
    </style>
  </defs>

  <rect width="800" height="450" fill="#0a0a15"/>

  <g stroke="#151525" stroke-width="1">
    <line x1="0" y1="0" x2="800" y2="0"/>
    <line x1="0" y1="50" x2="800" y2="50"/>
    <line x1="0" y1="100" x2="800" y2="100"/>
    <line x1="0" y1="150" x2="800" y2="150"/>
    <line x1="0" y1="200" x2="800" y2="200"/>
    <line x1="0" y1="250" x2="800" y2="250"/>
    <line x1="0" y1="300" x2="800" y2="300"/>
    <line x1="0" y1="350" x2="800" y2="350"/>
    <line x1="0" y1="400" x2="800" y2="400"/>
    <line x1="100" y1="0" x2="100" y2="450"/>
    <line x1="200" y1="0" x2="200" y2="450"/>
    <line x1="300" y1="0" x2="300" y2="450"/>
    <line x1="400" y1="0" x2="400" y2="450"/>
    <line x1="500" y1="0" x2="500" y2="450"/>
    <line x1="600" y1="0" x2="600" y2="450"/>
    <line x1="700" y1="0" x2="700" y2="450"/>
  </g>

  <text x="400" y="35" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="bold">
    ✨ Simulação GAN - Rinoplastia
  </text>
  <text x="400" y="55" text-anchor="middle" fill="#8888aa" font-size="11">
    Deslize para ver a transformação
  </text>

  <g transform="translate(100, 75)">
    <g clip-path="url(#leftHalf)">
      <rect x="0" y="0" width="600" height="250" fill="url(#beforeGradient)"/>

      <g transform="translate(300, 125)">
        <ellipse cx="0" cy="0" rx="100" ry="110" fill="#333344" opacity="0.5"/>

        <ellipse cx="-40" cy="-25" rx="20" ry="12" fill="#444455" stroke="#666677" stroke-width="1.5"/>
        <circle cx="-40" cy="-25" r="6" fill="#555566"/>

        <ellipse cx="40" cy="-25" rx="20" ry="12" fill="#444455" stroke="#666677" stroke-width="1.5"/>
        <circle cx="40" cy="-25" r="6" fill="#555566"/>

        <path d="M -5,-15 L -15,30 L -8,38 L 0,42 L 8,38 L 15,30 L 5,-15 Z" fill="#555566">
          <animate attributeName="d" values="
            M -5,-15 L -15,30 L -8,38 L 0,42 L 8,38 L 15,30 L 5,-15;
            M -5,-15 L -12,30 L -6,38 L 0,40 L 6,38 L 12,30 L 5,-15;
            M -5,-15 L -15,30 L -8,38 L 0,42 L 8,38 L 15,30 L 5,-15"
            dur="4s" repeatCount="indefinite"/>
        </path>
        <line x1="-12" y1="25" x2="12" y2="25" stroke="#444455" stroke-width="2" opacity="0.5"/>

        <path d="M -25,65 Q 0,72 25,65" fill="none" stroke="#666677" stroke-width="2"/>

        <path d="M -55,-40 Q -40,-50 -25,-40" fill="none" stroke="#444455" stroke-width="2"/>
        <path d="M 25,-40 Q 40,-50 55,-40" fill="none" stroke="#444455" stroke-width="2"/>
      </g>

      <text x="50" y="230" fill="#aaaaaa" font-size="14" font-weight="bold">⬅ ANTES</text>
    </g>

    <g clip-path="url(#rightHalf)">
      <rect x="0" y="0" width="600" height="250" fill="url(#afterGradient)"/>

      <g transform="translate(300, 125)">
        <ellipse cx="0" cy="0" rx="100" ry="110" fill="rgba(102,126,234,0.3)" filter="url(#glow-strong)"/>

        <ellipse cx="-40" cy="-25" rx="20" ry="12" fill="#2a2a4a" stroke="#667eea" stroke-width="2"/>
        <circle cx="-40" cy="-25" r="6" fill="#667eea" filter="url(#glow-strong)"/>

        <ellipse cx="40" cy="-25" rx="20" ry="12" fill="#2a2a4a" stroke="#667eea" stroke-width="2"/>
        <circle cx="40" cy="-25" r="6" fill="#667eea" filter="url(#glow-strong)"/>

        <path d="M -4,-15 L -10,30 L -5,38 L 0,40 L 5,38 L 10,30 L 4,-15 Z" fill="#7a7eb8">
          <animate attributeName="d" values="
            M -4,-15 L -10,30 L -5,38 L 0,40 L 5,38 L 10,30 L 4,-15;
            M -4,-15 L -8,30 L -4,38 L 0,39 L 4,38 L 8,30 L 4,-15;
            M -4,-15 L -10,30 L -5,38 L 0,40 L 5,38 L 10,30 L 4,-15"
            dur="4s" repeatCount="indefinite"/>
        </path>

        <path d="M -25,65 Q 0,75 25,65" fill="none" stroke="#aa88dd" stroke-width="2">
          <animate attributeName="d" values="M -25,65 Q 0,75 25,65;M -25,65 Q 0,70 25,65;M -25,65 Q 0,75 25,65" dur="3s" repeatCount="indefinite"/>
        </path>

        <path d="M -55,-40 Q -40,-50 -25,-40" fill="none" stroke="#667eea" stroke-width="2"/>
        <path d="M 25,-40 Q 40,-50 55,-40" fill="none" stroke="#667eea" stroke-width="2"/>

        <g class="sparkle" fill="url(#sparkleGradient)">
          <polygon points="80,-60 82,-55 87,-55 83,-50 85,-45 80,-48 75,-45 77,-50 73,-55 78,-55" transform="translate(0,0) scale(0.5)">
            <animateTransform attributeName="transform" type="rotate" from="0 80 -50" to="360 80 -50" dur="3s" repeatCount="indefinite"/>
          </polygon>
          <polygon points="80,-60 82,-55 87,-55 83,-50 85,-45 80,-48 75,-45 77,-50 73,-55 78,-55" transform="translate(-100, 50) scale(0.4)">
            <animateTransform attributeName="transform" type="rotate" from="360 -20 0" to="0 -20 0" dur="4s" repeatCount="indefinite"/>
          </polygon>
          <polygon points="80,-60 82,-55 87,-55 83,-50 85,-45 80,-48 75,-45 77,-50 73,-55 78,-55" transform="translate(100, 70) scale(0.3)">
            <animateTransform attributeName="transform" type="rotate" from="0 180 120" to="360 180 120" dur="5s" repeatCount="indefinite"/>
          </polygon>
        </g>
      </g>

      <text x="520" y="230" fill="#667eea" font-size="14" font-weight="bold">DEPOIS ➔</text>
    </g>

    <line class="comparison-line" x1="375" y1="0" x2="375" y2="250"
          stroke="#ffffff" stroke-width="3" stroke-linecap="round"
          opacity="0.8" filter="url(#glow-strong)"/>

    <g class="slider-knob" transform="translate(375, 125)">
      <circle cx="0" cy="0" r="20" fill="#ffffff" filter="url(#glow-strong)"/>
      <circle cx="0" cy="0" r="15" fill="#667eea"/>
      <path d="M -8,0 L -3,-5 L -3,5 Z" fill="#ffffff"/>
      <path d="M 8,0 L 3,-5 L 3,5 Z" fill="#ffffff"/>
    </g>
  </g>

  <g transform="translate(100, 340)">
    <rect x="0" y="0" width="200" height="80" rx="10" fill="#1a1a2e" stroke="#667eea" stroke-width="2"/>
    <text x="100" y="25" text-anchor="middle" fill="#8888aa" font-size="10">PROCEDIMENTO</text>
    <text x="100" y="48" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold" class="procedure-text">Rinoplastia</text>
    <text x="100" y="68" text-anchor="middle" fill="#667eea" font-size="11">Intensidade: 75%</text>
  </g>

  <g transform="translate(320, 340)">
    <rect x="0" y="0" width="200" height="80" rx="10" fill="#1a1a2e" stroke="#00ff88" stroke-width="2"/>
    <text x="100" y="25" text-anchor="middle" fill="#8888aa" font-size="10">MELHORIAS</text>

    <text x="10" y="48" fill="#aaaaaa" font-size="11">Simetria nasal:</text>
    <text x="140" y="48" fill="#00ff88" font-size="12" font-weight="bold">+18%</text>

    <text x="10" y="68" fill="#aaaaaa" font-size="11">Proporção:</text>
    <text x="140" y="68" fill="#ffcc00" font-size="12" font-weight="bold">1.618 ✨</text>
  </g>

  <g transform="translate(540, 340)">
    <rect x="0" y="0" width="180" height="80" rx="10" fill="#1a1a2e" stroke="#ff00aa" stroke-width="2"/>
    <text x="90" y="25" text-anchor="middle" fill="#8888aa" font-size="10">MODELO GAN</text>
    <text x="90" y="45" text-anchor="middle" fill="#ff00aa" font-size="13" font-weight="bold">StyleGAN2</text>
    <text x="90" y="65" text-anchor="middle" fill="#00ff88" font-size="10">GPU: ✅ Ativo</text>
  </g>

  <text x="400" y="435" text-anchor="middle" fill="#444466" font-size="9">
    GAN Simulator com fallback OpenCV | Auditoria ética em tempo real | EU AI Act compliant
  </text>
</svg>

### ⚖️ Dashboard de Ética e Auditoria

<!-- SVG Animado - Ética -->
<svg width="800" height="450" viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ethicsGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00b894;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00cec9;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="warningGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fdcb6e;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e17055;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="dangerGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e17055;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d63031;stop-opacity:1" />
    </linearGradient>
    <filter id="glow-green">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/>
    </filter>

    <style>
      .check-icon {
        animation: check-anim 0.6s ease-out forwards;
        stroke-dasharray: 100;
        stroke-dashoffset: 100;
      }
      @keyframes check-anim {
        to { stroke-dashoffset: 0; }
      }
      .pulse-ring {
        animation: pulse-ring-anim 2s ease-out infinite;
      }
      @keyframes pulse-ring-anim {
        0% { transform: scale(0.8); opacity: 1; }
        100% { transform: scale(1.5); opacity: 0; }
      }
      .float {
        animation: float-anim 3s ease-in-out infinite;
      }
      @keyframes float-anim {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
      }
      .shield-shine {
        animation: shield-shine-anim 3s linear infinite;
      }
      @keyframes shield-shine-anim {
        0% { opacity: 0; }
        50% { opacity: 0.5; }
        100% { opacity: 0; }
      }
    </style>
  </defs>

  <rect width="800" height="450" fill="#0a0a15"/>

  <g stroke="#151525" stroke-width="1">
    <line x1="0" y1="0" x2="800" y2="0"/>
    <line x1="0" y1="50" x2="800" y2="50"/>
    <line x1="0" y1="100" x2="800" y2="100"/>
    <line x1="0" y1="150" x2="800" y2="150"/>
    <line x1="0" y1="200" x2="800" y2="200"/>
    <line x1="0" y1="250" x2="800" y2="250"/>
    <line x1="0" y1="300" x2="800" y2="300"/>
    <line x1="0" y1="350" x2="800" y2="350"/>
    <line x1="0" y1="400" x2="800" y2="400"/>
    <line x1="100" y1="0" x2="100" y2="450"/>
    <line x1="200" y1="0" x2="200" y2="450"/>
    <line x1="300" y1="0" x2="300" y2="450"/>
    <line x1="400" y1="0" x2="400" y2="450"/>
    <line x1="500" y1="0" x2="500" y2="450"/>
    <line x1="600" y1="0" x2="600" y2="450"/>
    <line x1="700" y1="0" x2="700" y2="450"/>
  </g>

  <text x="400" y="35" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="bold" class="float">
    ⚖️ Dashboard de Ética e Auditoria
  </text>

  <g transform="translate(400, 140)" class="float">
    <path d="M 0,-60 L 50,-40 L 50,20 Q 50,60 0,80 Q -50,60 -50,20 L -50,-40 Z"
          fill="none" stroke="#00b894" stroke-width="3" filter="url(#glow-green)"/>
    <path d="M 0,-45 L 35,-30 L 35,15 Q 35,45 0,60 Q -35,45 -35,15 L -35,-30 Z"
          fill="rgba(0,184,148,0.1)" stroke="#00b894" stroke-width="2"/>
    <ellipse cx="0" cy="0" rx="40" ry="50" fill="url(#ethicsGradient)" opacity="0.1" class="shield-shine"/>
    <path class="check-icon" d="M -25,0 L -5,20 L 25,-20"
          fill="none" stroke="#00b894" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <g transform="translate(400, 140)">
    <ellipse cx="0" cy="0" rx="70" ry="90" fill="none" stroke="#00b894" stroke-width="1"
          class="pulse-ring" opacity="0.3"/>
    <ellipse cx="0" cy="0" rx="75" ry="95" fill="none" stroke="#00b894" stroke-width="1"
          class="pulse-ring" opacity="0.2" style="animation-delay: 0.5s"/>
    <ellipse cx="0" cy="0" rx="80" ry="100" fill="none" stroke="#00b894" stroke-width="1"
          class="pulse-ring" opacity="0.1" style="animation-delay: 1s"/>
  </g>

  <g transform="translate(50, 220)">
    <rect x="0" y="0" width="300" height="180" rx="12" fill="#1a1a2e" stroke="#00b894" stroke-width="2" filter="url(#shadow)"/>

    <text x="150" y="28" text-anchor="middle" fill="#00b894" font-size="13" font-weight="bold">
      📋 PRINCÍPIOS ÉTICOS
    </text>

    <g transform="translate(15, 45)">
      <circle cx="10" cy="10" r="10" fill="#00b894" opacity="0.2"/>
      <path d="M 5,10 L 9,14 L 15,6" fill="none" stroke="#00b894" stroke-width="2.5" stroke-linecap="round"/>
      <text x="30" y="14" fill="#ffffff" font-size="11">Fairness (Equidade)</text>

      <circle cx="10" cy="35" r="10" fill="#00b894" opacity="0.2"/>
      <path d="M 5,35 L 9,39 L 15,31" fill="none" stroke="#00b894" stroke-width="2.5" stroke-linecap="round"/>
      <text x="30" y="39" fill="#ffffff" font-size="11">Transparency</text>

      <circle cx="10" cy="60" r="10" fill="#00b894" opacity="0.2"/>
      <path d="M 5,60 L 9,64 L 15,56" fill="none" stroke="#00b894" stroke-width="2.5" stroke-linecap="round"/>
      <text x="30" y="64" fill="#ffffff" font-size="11">Privacy (Privacidade)</text>

      <circle cx="10" cy="85" r="10" fill="#00b894" opacity="0.2"/>
      <path d="M 5,85 L 9,89 L 15,81" fill="none" stroke="#00b894" stroke-width="2.5" stroke-linecap="round"/>
      <text x="30" y="89" fill="#ffffff" font-size="11">Accountability</text>

      <circle cx="10" cy="110" r="10" fill="#00b894" opacity="0.2"/>
      <path d="M 5,110 L 9,114 L 15,106" fill="none" stroke="#00b894" stroke-width="2.5" stroke-linecap="round"/>
      <text x="30" y="114" fill="#ffffff" font-size="11">Non-maleficence</text>

      <circle cx="10" cy="135" r="10" fill="#00cec9" opacity="0.2"/>
      <path d="M 5,135 L 9,139 L 15,131" fill="none" stroke="#00cec9" stroke-width="2.5" stroke-linecap="round"/>
      <text x="30" y="139" fill="#ffffff" font-size="11">Autonomy (Autonomia)</text>

      <circle cx="10" cy="160" r="10" fill="#00cec9" opacity="0.2"/>
      <path d="M 5,160 L 9,164 L 15,156" fill="none" stroke="#00cec9" stroke-width="2.5" stroke-linecap="round"/>
      <text x="30" y="164" fill="#ffffff" font-size="11">Beneficence</text>
    </g>
  </g>

  <g transform="translate(450, 220)">
    <rect x="0" y="0" width="300" height="180" rx="12" fill="#1a1a2e" stroke="#fdcb6e" stroke-width="2"/>

    <text x="150" y="28" text-anchor="middle" fill="#fdcb6e" font-size="13" font-weight="bold">
      📊 DETECÇÃO DE BIAS
    </text>

    <g transform="translate(15, 50)">
      <text x="0" y="0" fill="#aaaaaa" font-size="10">Gênero</text>
      <rect x="70" y="-8" width="180" height="12" rx="4" fill="#2a2a4e"/>
      <rect x="70" y="-8" width="0" height="12" rx="4" fill="url(#ethicsGradient)">
        <animate attributeName="width" values="0;40" dur="1.5s" fill="freeze"/>
      </rect>
      <text x="275" y="2" fill="#00b894" font-size="11" font-weight="bold">12%</text>

      <text x="0" y="30" fill="#aaaaaa" font-size="10">Etnia</text>
      <rect x="70" y="22" width="180" height="12" rx="4" fill="#2a2a4e"/>
      <rect x="70" y="22" width="0" height="12" rx="4" fill="url(#ethicsGradient)">
        <animate attributeName="width" values="0;50" dur="1.5s" fill="freeze" begin="0.2s"/>
      </rect>
      <text x="275" y="32" fill="#00b894" font-size="11" font-weight="bold">15%</text>

      <text x="0" y="60" fill="#aaaaaa" font-size="10">Idade</text>
      <rect x="70" y="52" width="180" height="12" rx="4" fill="#2a2a4e"/>
      <rect x="70" y="52" width="0" height="12" rx="4" fill="url(#ethicsGradient)">
        <animate attributeName="width" values="0;30" dur="1.5s" fill="freeze" begin="0.4s"/>
      </rect>
      <text x="275" y="62" fill="#00b894" font-size="11" font-weight="bold">8%</text>

      <text x="0" y="90" fill="#ffffff" font-size="11" font-weight="bold">Overall</text>
      <rect x="70" y="82" width="180" height="14" rx="5" fill="#2a2a4e"/>
      <rect x="70" y="82" width="0" height="14" rx="5" fill="url(#ethicsGradient)">
        <animate attributeName="width" values="0;70" dur="1.5s" fill="freeze" begin="0.6s"/>
      </rect>
      <text x="275" y="92" fill="#00b894" font-size="12" font-weight="bold">LOW</text>
    </g>
  </g>

  <g transform="translate(50, 410)">
    <rect x="0" y="0" width="140" height="30" rx="8" fill="#1a1a2e" stroke="#00b894" stroke-width="2"/>
    <text x="70" y="20" text-anchor="middle" fill="#00b894" font-size="10" font-weight="bold">✅ EU AI Act</text>

    <rect x="150" y="0" width="140" height="30" rx="8" fill="#1a1a2e" stroke="#00b894" stroke-width="2"/>
    <text x="220" y="20" text-anchor="middle" fill="#00b894" font-size="10" font-weight="bold">✅ GDPR/LGPD</text>

    <rect x="300" y="0" width="140" height="30" rx="8" fill="#1a1a2e" stroke="#00cec9" stroke-width="2"/>
    <text x="370" y="20" text-anchor="middle" fill="#00cec9" font-size="10" font-weight="bold">📝 Audit Log</text>

    <rect x="450" y="0" width="300" height="30" rx="8" fill="#1a1a2e" stroke="#667eea" stroke-width="2"/>
    <text x="465" y="20" fill="#8888aa" font-size="10">Audit ID:</text>
    <text x="520" y="20" fill="#667eea" font-size="10" font-family="monospace">abc123def456</text>
  </g>

  <g fill="#00b894" opacity="0.3">
    <circle cx="100" cy="100" r="2">
      <animate attributeName="cy" values="100;400;100" dur="8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.3;0;0.3" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="700" cy="80" r="2">
      <animate attributeName="cy" values="80;380;80" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.3;0;0.3" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="150" cy="400" r="2">
      <animate attributeName="cy" values="400;50;400" dur="9s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.3;0;0.3" dur="9s" repeatCount="indefinite"/>
    </circle>
  </g>

  <text x="400" y="442" text-anchor="middle" fill="#444466" font-size="9">
    AI Ethics Framework v1.0.0 | EU AI Act Compliant | Audit Trail Enabled
  </text>
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
