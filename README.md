# Project Vision Computer

## Visão Geral
O Project Vision Computer é uma plataforma avançada de análise facial e simulação para aplicações estéticas e dermatológicas. Utiliza IA, visão computacional e visualização de dados para fornecer análise facial completa, pontuação de beleza e simulação de procedimentos estéticos.

## Funcionalidades
- Detecção de pontos faciais (landmarks) com MediaPipe
- Medidas faciais avançadas e análise de simetria
- Pontuação estética baseada em proporções faciais e razão áurea
- Análise de qualidade da pele
- Simulação de procedimentos estéticos (rinoplastia, preenchimento labial, contorno facial, lifting de sobrancelhas, rejuvenescimento da pele)
- Geração de relatórios detalhados em HTML e JSON
- Interface moderna com Streamlit e interface desktop

## Estrutura do Projeto
```
├── main.py
├── requirements.txt
├── src/
│   ├── ai/
│   ├── core/
│   ├── reports/
│   ├── ui/
│   └── utils/
├── tests/
├── reports/
```

## Instalação
1. Clone o repositório:
   ```bash
   git clone <repo-url>
   cd Project Vision Computer
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
- Execute a aplicação principal:
  ```bash
  python main.py
  ```
- Para rodar a interface Streamlit:
  ```bash
  streamlit run src/ui/streamlit_app.py
  ```
- Para executar os testes:
  ```bash
  pytest
  ```

## Testes
- Todos os módulos principais possuem testes unitários na pasta `tests/`.
- Imagens dummy são usadas para cobertura de testes; imagens reais são necessárias para funcionalidade completa.

## Dependências
- Python 3.12+
- OpenCV
- NumPy
- SciPy
- scikit-image
- matplotlib
- seaborn
- pandas
- plotly
- mediapipe
- scikit-learn
- streamlit

## Licença
MIT License

## Autores
- Wellington de Lima Catarina

## Agradecimentos
- MediaPipe pela detecção de pontos faciais
- OpenCV e scikit-image para processamento de imagens
- Streamlit para desenvolvimento rápido de UI