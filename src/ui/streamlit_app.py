"""
Streamlit Web Application - Vision Computer Project
Interface moderna com integração GAN e Ética em IA
"""

import streamlit as st
from PIL import Image
import io
import sys
from pathlib import Path

# Adicionar paths
sys.path.append(str(Path(__file__).parent.parent))

from src.core.analyzer import FacialAnalyzer
from src.ai.gan_simulator import GANSimulator, GANSimulatorConfig
from src.ethics.ai_ethics import AIEthicsFramework, RiskLevel

# Configuração da página
st.set_page_config(
    page_title="Vision Aesthetics",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: bold; color: #1f77b4;}
    .sub-header {font-size: 1.2rem; color: #666;}
    .stAlert {border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<p class="main-header">✨ Vision Computer Project</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Análise Facial Estética com IA Ética</p>', unsafe_allow_html=True)
st.markdown("---")

# Inicializar componentes em cache
@st.cache_resource
def get_analyzer():
    return FacialAnalyzer()

@st.cache_resource
def get_simulator():
    config = GANSimulatorConfig(model_type="fallback")
    return GANSimulator(config)

@st.cache_resource
def get_ethics_framework():
    return AIEthicsFramework(enable_logging=False)

analyzer = get_analyzer()
simulator = get_simulator()
ethics = get_ethics_framework()

# Sidebar
with st.sidebar:
    st.header("⚙️ Configurações")

    uploaded_file = st.file_uploader(
        "📁 Carregar Imagem",
        type=["jpg", "jpeg", "png"],
        help="Formatos: JPG, JPEG, PNG"
    )

    st.markdown("---")

    # Configurações de simulação
    st.subheader("🎨 Simulação")
    procedure = st.selectbox(
        "Procedimento",
        [
            "Nenhum",
            "Rinoplastia",
            "Preenchimento Labial",
            "Lifting Facial",
            "Redução de Papada",
            "Aumento de Maçãs",
            "Afinamento de Rosto",
            "Juvenilização",
            "Contorno Facial"
        ]
    )

    intensity = st.slider(
        "Intensidade",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1
    )

    blend_factor = st.slider(
        "Blend (suavidade)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    st.markdown("---")

    # Configurações éticas
    st.subheader("⚖️ Ética")
    consent = st.checkbox(
        "Consentimento Informado",
        value=True,
        help="Concordo com o processamento da minha imagem facial"
    )

    ethics_audit = st.checkbox(
        "Auditoria Ética",
        value=True,
        help="Realizar auditoria ética da análise"
    )

    strict_mode = st.checkbox(
        "Modo Estrito",
        value=False,
        help="Bloqueia análises com risco ético elevado"
    )

# Conteúdo principal
if uploaded_file and consent:
    # Carregar imagem
    image = Image.open(uploaded_file)

    # Layout em colunas
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original")
        st.image(image, use_column_width=True)

    # Processamento
    if st.button("🔍 Analisar & Simular", type="primary", disabled=not uploaded_file):
        with st.spinner("Analisando imagem facial..."):
            try:
                # Análise facial
                results = analyzer.analyze(str(uploaded_file))
                results["consent_obtained"] = consent

                # Auditoria ética
                if ethics_audit:
                    audit_result = ethics.audit_analysis(results)
                    results["ethics_audit"] = audit_result

                    # Modo estrito
                    if strict_mode and audit_result.risk_level == RiskLevel.HIGH:
                        st.error("🛑 Análise bloqueada: Risco ético elevado detectado")
                        st.write("Recomendações:", audit_result.recommendations)
                        st.stop()

                # Simulação
                if procedure != "Nenhum":
                    with st.spinner(f"Simulando {procedure.lower()} com GAN..."):
                        simulated = simulator.simulate_procedure(
                            image,
                            procedure=procedure.lower().replace(" ", "_").replace("ç", "c").replace("ã", "a"),
                            intensity=intensity,
                            blend_factor=blend_factor
                        )

                        with col2:
                            st.subheader(f"✨ Após: {procedure}")
                            st.image(simulated, use_column_width=True)

                            # Download da imagem simulada
                            buf = io.BytesIO()
                            simulated.save(buf, format="PNG")
                            st.download_button(
                                label="📥 Baixar Imagem Simulada",
                                data=buf.getvalue(),
                                file_name=f"simulacao_{procedure.lower().replace(' ', '_')}.png",
                                mime="image/png"
                            )
                else:
                    with col2:
                        st.subheader("Pré-visualização")
                        st.image(image, use_column_width=True)

                # Resultados da análise
                st.markdown("---")
                st.subheader("📊 Resultados da Análise")

                if "aesthetic_scores" in results:
                    cols = st.columns(4)
                    scores = results["aesthetic_scores"]

                    cols[0].metric(
                        "Simetria",
                        f"{scores.get('symmetry', 0):.0%}",
                        delta=None
                    )
                    cols[1].metric(
                        "Harmonia",
                        f"{scores.get('harmony', 0):.0%}",
                        delta=None
                    )
                    cols[2].metric(
                        "Proporção Áurea",
                        f"{scores.get('golden_ratio', 0):.0%}",
                        delta=None
                    )
                    cols[3].metric(
                        "Score Geral",
                        f"{scores.get('overall', 0):.0%}",
                        delta=None
                    )

                # Auditoria ética
                if ethics_audit and hasattr(audit_result, 'risk_level'):
                    st.markdown("---")
                    st.subheader("⚖️ Auditoria Ética")

                    risk_emoji = {
                        "low": "✅",
                        "medium": "⚠️",
                        "high": "🚨",
                        "critical": "🛑"
                    }

                    risk_level = audit_result.risk_level.value
                    st.write(
                        f"**Nível de Risco:** {risk_emoji.get(risk_level, '')} **{risk_level.upper()}**"
                    )

                    # Prov disclosure
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.metric(
                            "Transparência",
                            f"{audit_result.transparency_score:.0%}"
                        )
                    with col_b:
                        st.metric(
                            "Privacidade",
                            f"{audit_result.privacy_score:.0%}"
                        )
                    with col_c:
                        st.metric(
                            "Bias Geral",
                            f"{audit_result.bias_detected.get('overall', 0):.0%}",
                            delta="menor é melhor"
                        )

                    if audit_result.recommendations:
                        with st.expander("📋 Recomendações da Auditoria"):
                            for rec in audit_result.recommendations:
                                st.write(f"• {rec}")

                    if audit_result.consent_verified:
                        st.success("✅ Consentimento verificado")
                    else:
                        st.error("❌ Consentimento não verificado")

                # Exportar resultados
                st.markdown("---")
                st.subheader("📥 Exportar")

                # Gerar JSON de resultados
                import json
                results_json = {
                    "analysis_id": "analise_001",
                    "scores": results.get("aesthetic_scores", {}),
                    "ethics": {
                        "risk_level": audit_result.risk_level.value if ethics_audit else "N/A",
                        "bias": audit_result.bias_detected if ethics_audit else {}
                    }
                }

                st.download_button(
                    label="📄 Baixar Relatório JSON",
                    data=json.dumps(results_json, indent=2),
                    file_name="relatorio_analise.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(f"❌ Erro: {str(e)}")
                st.exception(e)

elif uploaded_file and not consent:
    st.warning("⚠️ **Atenção:** É necessário fornecer consentimento para realizar a análise.")
    st.info("Marque a caixa 'Consentimento Informado' na barra lateral para continuar.")
else:
    st.info("👆 **Comece aqui:** Carregue uma imagem facial na barra lateral para iniciar a análise.")

# Divulgação ética
with st.expander("📋 Divulgação de Uso de IA"):
    st.markdown("""
    **Importante:** Esta ferramenta utiliza Inteligência Artificial para análise estética facial.

    ### Limitações
    - Os resultados são **referências**, não diagnósticos médicos
    - Podem variar entre indivíduos e condições de iluminação
    - Não substitui avaliação profissional com especialista

    ### Privacidade
    - Sua imagem é processada localmente quando possível
    - Dados biométricos não são armazenados por padrão
    - Você pode solicitar exclusão dos dados a qualquer momento

    ### Consentimento
    Ao usar esta ferramenta, você declara que:
    - Compreende a natureza experimental da análise
    - Não usará os resultados para discriminação
    - Assume responsabilidade pelo uso das informações

    ### Base Ética
    Este sistema segue princípios do:
    - **EU AI Act (2024)**
    - **LGPD/GDPR** (Proteção de Dados)
    - **IEEE Ethically Aligned Design**
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.9em;'>"
    "Vision Computer Project v1.0.0 | "
    "Built with Streamlit + PyTorch + MediaPipe + AI Ethics Framework"
    "</div>",
    unsafe_allow_html=True
)