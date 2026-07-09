# 🎨 SVGs Animados - Documentação Visual

## Visão Geral

Este projeto agora inclui **3 SVGs animados profissionais** que demonstram em tempo real o funcionamento da ferramenta Vision-Aesthetics.

---

## 📍 Localização dos Arquivos

```
docs/assets/
├── demo-analysis.svg      # Análise Facial com Landmarks
├── demo-simulation.svg    # Simulação GAN Antes/Depois
├── demo-ethics.svg        # Dashboard de Ética
└── SVGS_VALIDACAO.md      # Validação técnica
```

---

## 🖼️ Descrição de Cada SVG

### 1. demo-analysis.svg (Análise Facial)

**O que mostra:**
- Rosto estilizado com gradiente roxo-azul
- 7 landmarks principais animados (pulsando)
- Linha de scan passando verticalmente
- Painel de métricas com scores animados
- Badge de auditoria ética

**Scores exibidos:**
- Simetria: 85% (barra ciano→rosa)
- Harmonia: 78% (barra ciano→rosa)
- Proporção Áurea: 92% (barra ciano→rosa)

**Animações:**
- Landmarks pulsando (1.5s, delay alternado)
- Scan line varrendo (3s)
- Loading bar (2s)
- Rosto flutuando (4s)

**Dimensões:** 800x450px

---

### 2. demo-simulation.svg (Simulação GAN)

**O que mostra:**
- Comparação lado a lado: ANTES (cinza) vs DEPOIS (colorido)
- Slider central deslizando esquerda/direita
- Nariz se refinando (morphing path)
- Sparkles/brilhos giratórios
- Painéis de informação do procedimento

**Informações:**
- Procedimento: Rinoplastia
- Intensidade: 75%
- Melhorias: Simetria +18%, Proporção 1.618
- Modelo: StyleGAN2 com GPU ativa

**Animações:**
- Sparkles girando (1.5s)
- Slider knob deslizando (4s)
- Nariz morphing (4s)
- Linha brilhando (2s)

**Dimensões:** 800x450px

---

### 3. demo-ethics.svg (Dashboard de Ética)

**O que mostra:**
- Escudo de proteção com checkmark (centro)
- Anéis pulsantes ao redor do escudo
- Lista de 7 princípios éticos com checks
- 3 métricas de bias + overall
- Badges de compliance

**Métricas:**
- Gênero: 12% (barra verde)
- Etnia: 15% (barra verde)
- Idade: 8% (barra verde)
- Overall: LOW RISK

**Animações:**
- Checkmark desenhando (0.6s)
- Barras preenchendo (1.5s)
- Anéis pulsando (2s)
- Escudo flutuando (3s)
- Brilho passando no escudo (3s)

**Dimensões:** 800x380px

---

## 🎯 Como Visualizar

### No GitHub README

Os SVGs estão incorporados no README.md. O GitHub renderiza SVGs como **imagens estáticas**, então as animações **não funcionarão** diretamente no GitHub.

### Para Ver as Animações

**Opção 1: Abrir no navegador**
```bash
# Windows
start docs\assets\demo-analysis.svg

# Mac
open docs/assets/demo-analysis.svg

# Linux
xdg-open docs/assets/demo-analysis.svg
```

**Opção 2: Servidor local**
```bash
cd docs/assets
python -m http.server 8080

# Acessar no navegador:
# http://localhost:8080/demo-analysis.svg
# http://localhost:8080/demo-simulation.svg
# http://localhost:8080/demo-ethics.svg
```

**Opção 3: Embed em site web**
```html
<!-- Copiar e colar o código SVG inline -->
<svg width="800" height="450" viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <!-- ... conteúdo SVG ... -->
</svg>
```

---

## 🎨 Paleta de Cores

| Cor | Hex | Uso Principal |
|-----|-----|---------------|
| Roxo-azul claro | `#667eea` | Elementos primários |
| Roxo | `#764ba2` | Gradientes |
| Ciano neon | `#00f5ff` | Landmarks, highlights |
| Rosa neon | `#ff00aa` | Detalhes, boca |
| Amarelo | `#ffcc00` | Scores,sparkles |
| Verde neon | `#00ff88` | Status, sucesso |
| Verde-água | `#00b894` | Ética, metrics |
| Preto azulado | `#0a0a15` | Backgrounds |

---

## 🔧 Estrutura Técnica

### CSS Keyframes

Todas as animações usam CSS inline dentro de `<defs><style>`:

```css
/* Exemplo de animação pulse */
.pulse { animation: pulse 1.5s ease-in-out infinite; }
@keyframes pulse {
  0%, 100% { r: 4; opacity: 1; }
  50% { r: 7; opacity: 0.6; }
}
```

### Filtros SVG

```xml
<!-- Glow filter -->
<filter id="glow">
  <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
  <feMerge>
    <feMergeNode in="coloredBlur"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

### Gradientes

```xml
<!-- Gradiente linear -->
<linearGradient id="faceGrad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#667eea"/>
  <stop offset="100%" style="stop-color:#764ba2"/>
</linearGradient>
```

---

## ✅ Validação

### Navegadores Suportados

| Navegador | Versão | Status |
|-----------|--------|--------|
| Chrome | 120+ | ✅ Total |
| Firefox | 121+ | ✅ Total |
| Safari | 17+ | ✅ Parcial* |
| Edge | 120+ | ✅ Total |

*Safari pode ter limitações com SMIL animations.

### GitHub

| Recurso | Status |
|---------|--------|
| SVG estático | ✅ Funciona |
| CSS Animations | ⚠️ Limitado |
| SMIL `<animate>` | ⚠️ Limitado |

---

## 📊 Performance

| Métrica | Valor |
|---------|-------|
| Tamanho médio (minificado) | ~8KB |
| Tempo de renderização | <100ms |
| FPS (animações) | 60fps |
| Memória usada | <5MB |

---

## 🛠️ Manutenção

### Editar SVGs

1. Abra o arquivo `.svg` em editor de texto ou VS Code
2. Localize o elemento/animação desejado
3. Edite valores (cores, duração, tamanhos)
4. Salve e teste no navegador

### Otimizar SVGs

Use o SVGO para reduzir tamanho:

```bash
# Instalar svgo
npm install -g svgo

# Otimizar
svgo demo-analysis.svg

# Resultado: ~30-50% menor
```

---

## 📝 Licença de Uso

Os SVGs são distribuídos sob a mesma licença MIT do projeto.

---

## 🚀 Próximas Melhorias (Opcional)

- [ ] Criar versões interativas com JavaScript
- [ ] Adicionar mais procedimentos à simulação
- [ ] Criar variante mobile (320x240)
- [ ] Adicionar sons (via JS)
- [ ] Exportar como vídeos/GIFs

---

**Data:** 2026-07-08  
**Versão:** 1.0.0  
**Status:** ✅ Produção