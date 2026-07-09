# Guia de Contribuição - Vision Computer Project

Obrigado por contribuir! Este documento explica como participar.

## 📋 Código de Conduta

- Seja respeitoso e inclusivo
- Foque em melhorias construtivas
- Respeite a diversidade de experiências

## 🚀 Como Contribuir

### 1. Reportar Bugs

Use o template de issue e inclua:
- Versão do Python
- Passos para reproduzir
- Comportamento esperado vs. observado
- Logs de erro (se aplicável)

### 2. Sugerir Funcionalidades

Antes de implementar:
- Verifique se já existe issue similar
- Discuta a abordagem na issue
- Espere aprovação dos mantenedores

### 3. Enviar Pull Requests

```bash
# Fork e clone
git clone https://github.com/SEU_USER/Vision-Computer-Project-for-Facial-Aesthetics.git

# Branch para feature
git checkout -b feat/minha-feature

# Desenvolva com testes
# Commit seguindo Conventional Commits
git commit -m "feat: adiciona minha feature"

# Push e PR
git push origin feat/minha-feature
```

## 📏 Padrões de Código

### Python Style Guide

Seguimos [PEP 8](https://pep8.org/) com Black:

```bash
# Formatação
black src/ tests/

# Linting
flake8 src/ --max-line-length=88

# Type checking
mypy src/ --strict
```

### Docstrings

Use Google Style:

```python
def analyze_image(image_path: str, threshold: float = 0.5) -> dict:
    """
    Analisa imagem facial e retorna métricas.

    Args:
        image_path: Caminho para imagem.
        threshold: Limiar para detecção (0-1).

    Returns:
        Dicionário com scores estéticos e landmarks.

    Raises:
        FileNotFoundError: Se imagem não existe.
        ValueError: Se threshold fora de faixa.
    """
```

### Type Hints

Sempre use type hints:

```python
from typing import Optional, List, Dict, Any

def process(
    data: List[Dict[str, Any]],
    max_items: Optional[int] = None
) -> Dict[str, float]:
    ...
```

## 🧪 Testes

### Executar Testes

```bash
# Todos os testes
pytest

# Com coverage
pytest --cov=src --cov-report=html

# Testes específicos
pytest tests/unit/test_gan_simulator.py -v

# Apenas testes rápidos
pytest -m "not slow"
```

### Cobertura Mínima

| Módulo | Cobertura Mínima |
|--------|-----------------|
| Core | 85% |
| AI | 80% |
| Ethics | 90% |
| UI | 70% |

### Escrever Testes

```python
import pytest
from src.ai.gan_simulator import GANSimulator

class TestGANSimulator:
    @pytest.fixture
    def simulator(self):
        return GANSimulator()

    def test_simulate_procedure(self, simulator):
        """Testa simulação básica."""
        # Arrange
        image = create_test_image()

        # Act
        result = simulator.simulate_procedure(image, "rinoplastia")

        # Assert
        assert isinstance(result, Image.Image)
```

## 📝 Commits

### Conventional Commits

```
feat: Nova funcionalidade
fix: Correção de bug
docs: Documentação
style: Formatação (não altera lógica)
refactor: Refatoração (não é feature nem fix)
test: Adicionar/testes
chore: Manutenção (build, deps, etc)
```

### Exemplos

```bash
# Feature
git commit -m "feat: adiciona simulação com StyleGAN"

# Bug fix
git commit -m "fix: corrige detecção de landmarks em baixa luz"

# Breaking change
git commit -m "feat!: muda API de análise facial"
git commit -m "feat: muda API de análise

BREAKING CHANGE: analyze() agora requer parâmetro consent"
```

## 🔍 Code Review

### Checklist do Reviewer

- [ ] Código segue padrões
- [ ] Testes adicionados/atualizados
- [ ] Documentação atualizada
- [ ] Sem segredos/credenciais
- [ ] Performance considerada
- [ ] Ética revisada (se aplicável)

### Feedback Construtivo

✅ **Bom:**
> "Considere extrair esta lógica em função separada para reuso."

❌ **Evite:**
> "Está muito complicado."

## 📚 Áreas para Contribuição

### Prioritárias

- [ ] Implementação completa do MediaPipe analyzer
- [ ] Modelos GAN pré-treinados
- [ ] Explicabilidade (SHAP/LIME)
- [ ] Traduções (i18n)
- [ ] Performance (GPU optimization)

### Boas Primeiras Issues

Procure por labels:
- `good first issue`
- `help wanted`
- `documentation`

## 🛠️ Setup de Desenvolvimento

```bash
# Clone
git clone https://github.com/Lelolima/Vision-Computer-Project-for-Facial-Aesthetics.git
cd Vision-Computer-Project-for-Facial-Aesthetics

# Ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Install dev dependencies
pip install -e ".[dev]"

# Pre-commit hooks (opcional)
pip install pre-commit
pre-commit install
```

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob MIT License.

## 🙏 Reconhecimento

Contribuidores serão listados no README.md.

---

Dúvidas? Abra uma issue ou discuta no GitHub Discussions.