# Auditoria técnica — 2026-11-22

Escopo: diagnóstico real (código executado, não README), correções P0–P2, CI e documentação.
Ambiente: Windows 11, Python 3.11 (uv), torch CPU. Sem GPU, sem câmera, sem pesos de modelos.

## Estado anterior

| Item | Resultado |
|------|-----------|
| Finalidade | Análise estética facial (MediaPipe FaceMesh), simulação de procedimentos (OpenCV/GAN), auditoria ética, API FastAPI, UIs Streamlit/Tkinter |
| Instalação | `requirements.txt` sem `scikit-learn`, `matplotlib`, `seaborn` (importados em `src/core/advanced_analysis.py`, `src/reports/`) |
| Testes | `pytest` **interrompido na coleta**: 3 erros (`ModuleNotFoundError: src.core.analyzer`) |
| CI | Nenhum workflow no repositório (só o "Dependency Graph" automático do GitHub, falhando) |
| Vulnerabilidades (pip-audit) | 127 avisos em pins de `requirements.txt`: pillow 10.2.0, torch 2.2.0, streamlit 1.30.0, fastapi 0.109.0, python-multipart 0.0.6, requests 2.31.0, tqdm 4.66.1, pytest 7.4.4, black 24.1.0 |
| Segredos | Nenhum encontrado (busca por padrões de tokens/chaves em todo o histórico `git log -p --all`). gitleaks não estava disponível na máquina |

## Problemas encontrados e correções

| # | Sev. | Problema | Evidência | Correção |
|---|------|----------|-----------|----------|
| 1 | P0 | API não importa: `src/__init__.py` e `src/api/main.py` importam `src.core.analyzer`, que não existia | erro de coleta em 3 arquivos de teste | criado `src/core/analyzer.py`; `src/__init__.py` com import preguiçoso |
| 2 | P0 | `GANSimulator()` sempre quebrava: `torchvision.transforms.Clamp` não existe | `AttributeError` ao importar a API | `transforms.Lambda(lambda t: t.clamp(0, 1))` |
| 3 | P1 | **Dados simulados passando por reais**: `FacialAnalyzer.analyze` devolvia `symmetry/harmony/golden_ratio = 0.5` fixos; `/analyze` chamava `analyze_from_bytes` inexistente (500) | leitura do código; novo teste `test_analyze_without_face_returns_422_not_fake_scores` | fachada delega ao `AdvancedFacialAnalyzer` (MediaPipe). Sem rosto → 422; não-imagem → 400 |
| 4 | P1 | `_fallback_lip_enhance` usava variáveis indefinidas (`h_lower`, `h` sobrescrito) — simulação labial sempre falhava | `test_simulate_preenchimento_labial`, `test_all_procedures` falhavam | corrigido índice de linhas |
| 5 | P1 | `simulate_lip_enhancement` quebrava quando `cv2.findNonZero` retorna `(N,2)` ou `None`; também recalculava isso por pixel | `test_simulate_lip_enhancement_returns_image` falhava | `reshape(-1, 2)` fora do laço |
| 6 | P2 | `audit_id` não era único para chamadas no mesmo instante com os mesmos dados | `test_unique_audit_ids` falhava | inclui `uuid4` no hash |
| 7 | P2 | Teste `test_default_config` esperava `device is None`, mas o código (e a docstring) auto-detecta `cpu/cuda` | falha do teste | teste ajustado para `in ("cpu","cuda")` — comportamento do código preservado |
| 8 | P0 | Dependências vulneráveis | pip-audit | pins atualizados para versões corrigidas e validadas localmente; `torchaudio` (não usado) removido |
| 9 | P1 | Sem CI | — | `.github/workflows/ci.yml`: ruff (E9/F63/F7/F82), `compileall`, pytest; `permissions: contents: read`; actions fixadas por SHA |
| 10 | P3 | `__pycache__` versionado; testes gravam relatórios no repo | `git ls-files` | removidos do índice; `.gitignore` atualizado |
| 11 | P2 | README/.env.example prometiam variáveis e recursos inexistentes | `grep getenv` → só `CORS_ORIGINS`, `ETHICS_STRICT_MODE` | documentação ajustada; `JWT_SECRET` de exemplo esvaziado |

## Testes executados (resultados reais)

```
# antes (main)
python -m pytest --no-cov  -> Interrupted: 3 errors during collection
# antes, só os módulos coletáveis (com o novo analyzer.py ausente)
-> 3 failed, 24 passed, 13 errors
# depois
python -m pytest -p no:cacheprovider --no-cov -o log_cli=false
-> 54 passed, 2 skipped
ruff check --select E9,F63,F7,F82 src tests main.py -> All checks passed!
```

Os 2 skips são de `test_advanced_analysis.py`: imagem sintética sem rosto → MediaPipe não detecta face (comportamento correto). Não há imagem real de rosto no repositório e nenhuma foi baixada.

## Não executado / riscos residuais

- Análise facial com rosto real: não validada (sem imagens de teste com rosto; não baixei datasets).
- Modos GAN (Pix2Pix/CycleGAN/StyleGAN): não há checkpoints; só o fallback OpenCV foi exercitado.
- Streamlit, Tkinter (`main.py`) e PyQt5 não foram iniciados (sem display). `ui.main_interface` importa sem erro.
- Docker/docker-compose não construídos.
- `GET /api/v1/report/{id}` continua não implementado (documentado).
- Upgrade grande de versões (numpy 2, pandas 3, opencv 5): validado pelos testes existentes, mas a cobertura é baixa nas UIs.
- Badge Docker Hub do README aponta para imagem não verificada.
