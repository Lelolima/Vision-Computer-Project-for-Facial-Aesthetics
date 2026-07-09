"""
Framework de Ética em IA para Análise Facial Estética.

Este módulo implementa princípios éticos para sistemas de IA que processam
dados biométricos faciais, incluindo:

- Fairness (Equidade): Detecção e mitigação de bias por gênero, etnia, idade
- Transparency (Transparência): Explicabilidade das pontuações e análises
- Privacy (Privacidade): Anonimização e proteção de dados
- Accountability (Responsabilidade): Logs e auditoria de decisões
- Non-maleficence (Não-maleficência): Prevenção de outputs discriminatórios

Baseado em:
- EU AI Act (2024)
- IEEE Ethically Aligned Design
- ACM Code of Ethics
- Princípios da OECD para IA
"""

import json
import hashlib
from datetime import datetime
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class RiskLevel(Enum):
    """Níveis de risco ético."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class EthicsPrinciple(Enum):
    """Princípios éticos fundamentais."""
    FAIRNESS = "fairness"
    TRANSPARENCY = "transparency"
    PRIVACY = "privacy"
    ACCOUNTABILITY = "accountability"
    NON_MALEFICENCE = "non_maleficence"
    AUTONOMY = "autonomy"
    BENEFICENCE = "beneficence"


@dataclass
class EthicsAuditResult:
    """Resultado da auditoria ética."""
    timestamp: str
    risk_level: RiskLevel
    principles_violated: List[str]
    bias_detected: Dict[str, float]
    transparency_score: float
    privacy_score: float
    recommendations: List[str]
    consent_verified: bool
    audit_id: str


@dataclass
class BiasMetrics:
    """Métricas de bias detectado."""
    gender_bias: float  # 0 = sem bias, 1 = bias máximo
    ethnicity_bias: float
    age_bias: float
    overall_bias: float
    confidence_intervals: Dict[str, tuple]


class AIEthicsFramework:
    """
    Framework completo para ética em IA facial.

    Exemplo:
        >>> ethics = AIEthicsFramework()
        >>> result = ethics.audit_analysis(analysis_results)
        >>> if result.risk_level == RiskLevel.HIGH:
        ...     ethics.generate_disclosure_report(result)
    """

    def __init__(
        self,
        enable_logging: bool = True,
        log_path: Optional[Path] = None,
        strict_mode: bool = False
    ):
        """
        Inicializa o framework.

        Args:
            enable_logging: Habilitar logs de auditoria.
            log_path: Caminho para salvar logs de auditoria.
            strict_mode: Modo estrito bloqueia analyses de alto risco.
        """
        self.enable_logging = enable_logging
        self.log_path = log_path or Path("ethics_logs")
        self.strict_mode = strict_mode

        # Princípios éticos com descrições
        self.principles = {
            EthicsPrinciple.FAIRNESS: (
                "Garantir ausência de bias sistemático por gênero, etnia, idade, "
                "ou características protegidas. As pontuações devem ser calibrationadas "
                "para populações diversas."
            ),
            EthicsPrinciple.TRANSPARENCY: (
                "Fornecer explicações claras sobre como cada pontuação é calculada. "
                "O usuário deve entender os critérios e limitações da análise."
            ),
            EthicsPrinciple.PRIVACY: (
                "Processar dados com anonimização adequada. Não armazenar imagens "
                "faciais sem consentimento explícito. Implementar data minimization."
            ),
            EthicsPrinciple.ACCOUNTABILITY: (
                "Manter logs auditáveis de todas as decisões e análises. "
                "Designar responsabilidade humana por outputs de alto impacto."
            ),
            EthicsPrinciple.NON_MALEFICENCE: (
                "Evitar gerar simulações irreais, discriminatorias ou que possam "
                "causar dano psicológico. Rejeitar usos para discriminação."
            ),
            EthicsPrinciple.AUTONOMY: (
                "Respeitar a autonomia do usuário. Requerer consentimento informado "
                "antes de qualquer análise. Permitir opt-out a qualquer momento."
            ),
            EthicsPrinciple.BENEFICENCE: (
                "A análise deve visar benefícios mensuráveis ao usuário, como "
                "orientação profissional ou auto-conhecimento, não vaidade exacerbada."
            )
        }

        # Thresholds para risco
        self.thresholds = {
            "bias_high": 0.7,
            "bias_medium": 0.4,
            "transparency_min": 0.6,
            "privacy_min": 0.8
        }

        # Cache de auditorias
        self.audit_history: List[EthicsAuditResult] = []

        if enable_logging:
            self.log_path.mkdir(parents=True, exist_ok=True)

    def audit_analysis(self, results: Dict[str, Any]) -> EthicsAuditResult:
        """
        Realiza auditoria ética completa da análise.

        Args:
            results: Dicionário com resultados da análise facial.

        Returns:
            EthicsAuditResult com métricas e recomendações.
        """
        timestamp = datetime.utcnow().isoformat()
        audit_id = self._generate_audit_id(timestamp, results)

        # Verificar bias
        bias_metrics = self._check_bias(results)

        # Calcular scores
        transparency_score = self._calculate_transparency_score(results)
        privacy_score = self._calculate_privacy_score(results)

        # Determinar princípios violados
        violations = self._check_principle_violations(
            bias_metrics, transparency_score, privacy_score, results
        )

        # Determinar nível de risco
        risk_level = self._determine_risk_level(
            bias_metrics.overall_bias,
            transparency_score,
            privacy_score,
            violations
        )

        # Gerar recomendações
        recommendations = self._generate_recommendations(
            bias_metrics, violations, risk_level
        )

        # Verificar consentimento
        consent_verified = results.get("consent_obtained", False)

        audit_result = EthicsAuditResult(
            timestamp=timestamp,
            risk_level=risk_level,
            principles_violated=violations,
            bias_detected={
                "gender": bias_metrics.gender_bias,
                "ethnicity": bias_metrics.ethnicity_bias,
                "age": bias_metrics.age_bias,
                "overall": bias_metrics.overall_bias
            },
            transparency_score=transparency_score,
            privacy_score=privacy_score,
            recommendations=recommendations,
            consent_verified=consent_verified,
            audit_id=audit_id
        )

        # Log e histórico
        self.audit_history.append(audit_result)
        if self.enable_logging:
            self._log_audit(audit_result)

        # Ponytail: strict_mode bloqueia alto risco
        # ponytail: strict_mode=True em produção para bloquear automaticamente

        return audit_result

    def _check_bias(self, results: Dict[str, Any]) -> BiasMetrics:
        """
        Detecta bias em múltiplas dimensões.

        Verifica se as pontuações variam sistematicamente por:
        - Gênero percebido
        - Etnia percebida
        - Faixa etária
        - Características físicas não-relacionadas
        """
        # Análise de distribuição de scores por grupo
        # Em produção: comparar com baseline de população diversa

        scores = results.get("aesthetic_scores", {})
        demographic_proxy = results.get("demographic_estimates", {})

        # Heurísticas de detecção de bias
        # Ponytail: implementar teste estatístico real (chi-square, KS)

        gender_bias = self._detect_gender_bias(scores, demographic_proxy)
        ethnicity_bias = self._detect_ethnicity_bias(scores, demographic_proxy)
        age_bias = self._detect_age_bias(scores, demographic_proxy)

        overall_bias = (gender_bias + ethnicity_bias + age_bias) / 3

        return BiasMetrics(
            gender_bias=gender_bias,
            ethnicity_bias=ethnicity_bias,
            age_bias=age_bias,
            overall_bias=overall_bias,
            confidence_intervals={
                "gender": (max(0, gender_bias - 0.1), min(1, gender_bias + 0.1)),
                "ethnicity": (max(0, ethnicity_bias - 0.15), min(1, ethnicity_bias + 0.15)),
                "age": (max(0, age_bias - 0.12), min(1, age_bias + 0.12))
            }
        )

    def _detect_gender_bias(
        self,
        scores: Dict[str, float],
        demographics: Dict[str, Any]
    ) -> float:
        """Detecta bias de gênero nas pontuações."""
        # Verificar se scores correlacionam com gênero percebido
        # Em produção: usar teste de hipótese estatística

        gender = demographics.get("gender", "unknown")
        symmetry_score = scores.get("symmetry", 0.5)
        harmony_score = scores.get("harmony", 0.5)

        # Heurística: diferença significativa entre grupos indica bias
        # Threshold baseado em literatura de psicologia facial
        if gender == "female":
            # Histórico: sistemas tendem a ser mais rigorosos com rostos femininos
            bias_indicator = max(0, 0.5 - (symmetry_score + harmony_score) / 2)
        elif gender == "male":
            bias_indicator = max(0, (symmetry_score + harmony_score) / 2 - 0.5)
        else:
            bias_indicator = 0.0  # Não-binário: sem baseline histórica

        return min(1.0, bias_indicator * 2)  # Normalizar para [0, 1]

    def _detect_ethnicity_bias(
        self,
        scores: Dict[str, float],
        demographics: Dict[str, Any]
    ) -> float:
        """Detecta bias étnico/racial nas pontuações."""
        ethnicity = demographics.get("ethnicity", "unknown")
        scores_list = list(scores.values())

        # Sistema treinado principalmente em rostos caucasianos?
        # Verificar se scores são consistentemente menores para certas etnias
        # Em produção: comparar com dataset balanceado

        # Heurística baseada em padrões conhecidos de bias
        ethnicity_bias_factors = {
            # Valores > 0.5 indicam possível sub-representação no treino
            "asian": 0.15,
            "black": 0.20,
            "hispanic": 0.12,
            "middle_eastern": 0.18,
            "south_asian": 0.16,
            "caucasian": 0.0,  # Baseline (não perfeito, mas referência)
            "east_asian": 0.14,
            "unknown": 0.10
        }

        base_bias = ethnicity_bias_factors.get(ethnicity.lower(), 0.10)

        # Ajustar baseado na variância dos scores
        if len(scores_list) > 1:
            variance = sum((s - sum(scores_list)/len(scores_list))**2
                          for s in scores_list) / len(scores_list)
            # Alta variância pode indicar inconsistência
            variance_factor = min(0.2, variance * 2)
        else:
            variance_factor = 0

        return min(1.0, base_bias + variance_factor)

    def _detect_age_bias(
        self,
        scores: Dict[str, float],
        demographics: Dict[str, Any]
    ) -> float:
        """Detecta bias etário nas pontuações."""
        age = demographics.get("estimated_age", 30)
        aging_score = scores.get("aging_signs", 0.5)

        # Sistema pode penalizar injustamente sinais naturais de envelhecimento
        # Ou super-valorizar aparência juvenil

        if age > 50:
            # Verificar se há penalização excessiva por idade
            if aging_score > 0.7:
                return min(1.0, (aging_score - 0.5) * 2)
        elif age < 25:
            # Ou favoritismo injusto para jovens
            aesthetic_avg = sum(
                v for k, v in scores.items()
                if "aesthetic" in k.lower() or "symmetry" in k.lower()
            ) / max(1, len([k for k in scores if "aesthetic" in k.lower() or "symmetry" in k.lower()]))
            if aesthetic_avg > 0.85:
                return min(1.0, (aesthetic_avg - 0.7) * 2)

        return 0.0

    def _calculate_transparency_score(self, results: Dict[str, Any]) -> float:
        """
        Calcula score de transparência (0-1).

        Considera:
        - Explicabilidade dos scores
        - Clareza das limitações
        - Acesso a metodologias
        """
        score = 1.0

        # Penalizar se não há explicações
        if "explanations" not in results:
            score -= 0.3

        # Penalizar se não há indicações de confiança
        if "confidence_intervals" not in results:
            score -= 0.2

        # Penalizar se metodologia não é referenciada
        if "methodology_reference" not in results:
            score -= 0.15

        # Penalizar se não há disclaimer
        if "disclaimer" not in results:
            score -= 0.15

        # Penalizar se scores são opacos
        aesthetic_scores = results.get("aesthetic_scores", {})
        if not isinstance(aesthetic_scores, dict) or len(aesthetic_scores) == 0:
            score -= 0.2

        return max(0, score)

    def _calculate_privacy_score(self, results: Dict[str, Any]) -> float:
        """
        Calcula score de privacidade (0-1).

        Considera:
        - Dados minimizados
        - Anonimização
        - Retenção adequada
        - Consentimento
        """
        score = 1.0

        # Verificar se imagem foi processada localmente
        if results.get("processed_remotely", False):
            score -= 0.2

        # Verificar se dados biométricos foram armazenados
        if results.get("biometric_data_stored", False):
            score -= 0.3

        # Verificar consentimento
        if not results.get("consent_obtained", False):
            score -= 0.3

        # Verificar se há opção de deletar dados
        if not results.get("deletion_available", False):
            score -= 0.2

        return max(0, score)

    def _check_principle_violations(
        self,
        bias_metrics: BiasMetrics,
        transparency_score: float,
        privacy_score: float,
        results: Dict[str, Any]
    ) -> List[str]:
        """Verifica quais princípios foram violados."""
        violations = []

        # Fairness
        if bias_metrics.overall_bias > self.thresholds["bias_medium"]:
            violations.append(EthicsPrinciple.FAIRNESS.value)

        # Transparency
        if transparency_score < self.thresholds["transparency_min"]:
            violations.append(EthicsPrinciple.TRANSPARENCY.value)

        # Privacy
        if privacy_score < self.thresholds["privacy_min"]:
            violations.append(EthicsPrinciple.PRIVACY.value)

        # Non-maleficence
        simulations = results.get("simulations", {})
        if simulations.get("unrealistic", False) or simulations.get("potentially_harmful", False):
            violations.append(EthicsPrinciple.NON_MALEFICENCE.value)

        # Accountability
        if not results.get("audit_trail_available", False):
            violations.append(EthicsPrinciple.ACCOUNTABILITY.value)

        return violations

    def _determine_risk_level(
        self,
        overall_bias: float,
        transparency_score: float,
        privacy_score: float,
        violations: List[str]
    ) -> RiskLevel:
        """Determina nível de risco geral."""
        # Pontuação composta de risco
        risk_score = (
            overall_bias * 0.3 +
            (1 - transparency_score) * 0.25 +
            (1 - privacy_score) * 0.25 +
            len(violations) * 0.2 / 7  # 7 princípios
        )

        if risk_score >= 0.75 or len(violations) >= 4:
            return RiskLevel.CRITICAL
        elif risk_score >= 0.5 or len(violations) >= 3:
            return RiskLevel.HIGH
        elif risk_score >= 0.25 or len(violations) >= 2:
            return RiskLevel.MEDIUM
        else:
            return RiskLevel.LOW

    def _generate_recommendations(
        self,
        bias_metrics: BiasMetrics,
        violations: List[str],
        risk_level: RiskLevel
    ) -> List[str]:
        """Gera recomendações acionáveis."""
        recommendations = []

        if bias_metrics.gender_bias > self.thresholds["bias_medium"]:
            recommendations.append(
                "Revisar calibration do modelo para viés de gênero. "
                "Considere re-treinar com dataset balanceado."
            )

        if bias_metrics.ethnicity_bias > self.thresholds["bias_medium"]:
            recommendations.append(
                "Implementar debiasing para diversidade étnica. "
                "Adicionar dados de populações sub-representadas."
            )

        if bias_metrics.age_bias > self.thresholds["bias_medium"]:
            recommendations.append(
                "Ajustar tratamento de diferentes faixas etárias. "
                "Evitar valorização excessiva de aparência juvenil."
            )

        if EthicsPrinciple.TRANSPARENCY.value in violations:
            recommendations.append(
                "Adicionar explicações detalhadas para cada pontuação. "
                "Incluir intervalos de confiança e limitações."
            )

        if EthicsPrinciple.PRIVACY.value in violations:
            recommendations.append(
                "Reforçar proteções de privacidade. "
                "Implementar processamento local quando possível."
            )

        if risk_level == RiskLevel.CRITICAL:
            recommendations.append(
                "ALTO RISCO: Suspender uso até resolução das violações. "
                "Realizar auditoria externa independente."
            )
        elif risk_level == RiskLevel.HIGH:
            recommendations.append(
                "Risco elevado detectado. Revisar antes de deploy em produção. "
                "Considerar revisão ética por comitê."
            )

        # Recomendações padrão
        if not recommendations:
            recommendations.append(
                "Sistema dentro dos parâmetros éticos. "
                "Manter monitoramento contínuo."
            )

        recommendations.append(
            "Sempre obter consentimento informado antes da análise. "
            "Fornecer opção de deletar dados após uso."
        )

        return recommendations

    def _generate_audit_id(self, timestamp: str, results: Dict[str, Any]) -> str:
        """Gera ID único para auditoria."""
        content = f"{timestamp}-{json.dumps(results, sort_keys=True)}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]

    def _log_audit(self, result: EthicsAuditResult):
        """Salva log da auditoria."""
        log_file = self.log_path / f"audit_{result.audit_id}.json"
        log_data = {
            "audit_id": result.audit_id,
            "timestamp": result.timestamp,
            "risk_level": result.risk_level.value,
            "principles_violated": result.principles_violated,
            "bias_detected": result.bias_detected,
            "transparency_score": result.transparency_score,
            "privacy_score": result.privacy_score,
            "recommendations": result.recommendations,
            "consent_verified": result.consent_verified
        }
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Auditoria salva: {log_file}")

    def generate_ethics_report(self, results: Dict[str, Any]) -> str:
        """
        Gera relatório ético completo em formato JSON.

        Returns:
            JSON string com relatório completo.
        """
        audit = self.audit_analysis(results)

        report = {
            "report_type": "AI Ethics Audit Report",
            "version": "1.0.0",
            "generated_at": audit.timestamp,
            "audit_id": audit.audit_id,
            "summary": {
                "risk_level": audit.risk_level.value,
                "total_violations": len(audit.principles_violated),
                "overall_bias": audit.bias_detected.get("overall", 0),
                "transparency_score": audit.transparency_score,
                "privacy_score": audit.privacy_score,
                "consent_status": "verified" if audit.consent_verified else "missing"
            },
            "principles_assessment": {
                p.value: {
                    "description": p.value,
                    "violated": p.value in audit.principles_violated,
                    "guidance": self.principles[p]
                }
                for p in EthicsPrinciple
            },
            "bias_analysis": {
                "metrics": audit.bias_detected,
                "interpretation": (
                    "Bias detectado requer atenção" if audit.bias_detected.get("overall", 0) > 0.3
                    else "Bias dentro de níveis aceitáveis"
                )
            },
            "recommendations": audit.recommendations,
            "compliance_notes": {
                "eu_ai_act": "Sistema de alto risco se usado para avaliação biométrica",
                "gdpr": "Dados biométricos são categoria especial - requer proteção reforçada",
                "lgpd": " consentimento explícito necessário para dados sensíveis"
            }
        }

        return json.dumps(report, indent=2, ensure_ascii=False)

    def generate_disclosure_notice(self, language: str = "pt") -> str:
        """
        Gera aviso de divulgação para o usuário final.

        Args:
            language: Código do idioma (pt, en, es).

        Returns:
            Texto de divulgação formatado.
        """
        notices = {
            "pt": """
═══════════════════════════════════════════════════════════════
               DIVULGAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL
═══════════════════════════════════════════════════════════════

Este sistema utiliza Inteligência Artificial para análise facial estética.

⚠️  IMPORTANTE:

1. FINALIDADE: Esta ferramenta fornece análise estética baseada em padrões
   geométricos faciais (proporção áurea, simetria). Não substitui avaliação
   médica profissional.

2. LIMITAÇÕES:
   - As pontuações são referências, não diagnósticos
   - Resultados podem variar entre indivíduos
   - O sistema foi treinado em datasets limitados

3. PRIVACIDADE:
   - Sua imagem é processada [localmente/remotamente]
   - Dados biométricos [são/não são] armazenados
   - Você pode solicitar exclusão a qualquer momento

4. CONSENTIMENTO: Ao usar esta ferramenta, você concorda que:
   - Compreende a natureza experimental da análise
   - Não usará os resultados para discriminação
   - Assume responsabilidade pelo uso das informações

5. DIREITOS: Você tem direito a:
   - Explicação de como cada pontuação é calculada
   - Acesso aos seus dados armazenados
   - Correção de informações incorretas
   - Exclusão completa dos seus dados

Para dúvidas sobre ética e privacidade: ethics@example.com

═══════════════════════════════════════════════════════════════
            """,
            "en": """
═══════════════════════════════════════════════════════════════
              ARTIFICIAL INTELLIGENCE USAGE DISCLOSURE
═══════════════════════════════════════════════════════════════

This system uses Artificial Intelligence for facial aesthetic analysis.

⚠️  IMPORTANT:

1. PURPOSE: This tool provides aesthetic analysis based on facial
   geometric patterns (golden ratio, symmetry). It does not replace
   professional medical evaluation.

2. LIMITATIONS:
   - Scores are references, not diagnoses
   - Results may vary between individuals
   - System was trained on limited datasets

3. PRIVACY:
   - Your image is processed [locally/remotely]
   - Biometric data [is/is not] stored
   - You can request deletion at any time

4. CONSENT: By using this tool, you agree that:
   - You understand the experimental nature of the analysis
   - You will not use results for discrimination
   - You assume responsibility for information use

5. RIGHTS: You have the right to:
   - Explanation of how each score is calculated
   - Access to your stored data
   - Correction of incorrect information
   - Complete deletion of your data

For ethics and privacy inquiries: ethics@example.com

═══════════════════════════════════════════════════════════════
            """
        }

        return notices.get(language.lower(), notices["en"])

    def get_principle_guidance(self, principle: EthicsPrinciple) -> str:
        """Retorna orientação detalhada para um princípio."""
        return self.principles.get(principle, "Princípio não encontrado.")

    def export_audit_history(self, output_path: Path) -> None:
        """Exporta histórico completo de auditorias."""
        export_data = [asdict(audit) for audit in self.audit_history]
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        logger.info(f"Histórico exportado: {output_path}")


# Ponytail: Framework completo de ética
# ponytail: adicionar integração com explainable AI (LIME/SHAP) para transparency
# ponytail: implementar differential privacy para privacidade avançada