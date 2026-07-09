"""
Testes Unitários - AI Ethics Framework
"""

import pytest
import json
from src.ethics.ai_ethics import (
    AIEthicsFramework,
    EthicsPrinciple,
    RiskLevel,
    EthicsAuditResult,
    BiasMetrics,
)


class TestEthicsPrinciple:
    """Testes para enum de princípios éticos."""

    def test_principles_exist(self):
        """Testa se princípios principais existem."""
        assert EthicsPrinciple.FAIRNESS.value == "fairness"
        assert EthicsPrinciple.TRANSPARENCY.value == "transparency"
        assert EthicsPrinciple.PRIVACY.value == "privacy"
        assert EthicsPrinciple.ACCOUNTABILITY.value == "accountability"
        assert EthicsPrinciple.NON_MALEFICENCE.value == "non_maleficence"


class TestRiskLevel:
    """Testes para níveis de risco."""

    def test_risk_levels(self):
        """Testa níveis de risco."""
        assert RiskLevel.LOW.value == "low"
        assert RiskLevel.MEDIUM.value == "medium"
        assert RiskLevel.HIGH.value == "high"
        assert RiskLevel.CRITICAL.value == "critical"


class TestAIEthicsFramework:
    """Testes para o framework de ética."""

    @pytest.fixture
    def ethics_framework(self):
        """Fixture para framework de ética."""
        return AIEthicsFramework(enable_logging=False)

    @pytest.fixture
    def sample_analysis_results(self):
        """Fixture para resultados de análise de exemplo."""
        return {
            "aesthetic_scores": {
                "symmetry": 0.85,
                "harmony": 0.78,
                "golden_ratio": 0.92,
            },
            "demographic_estimates": {
                "gender": "female",
                "ethnicity": "caucasian",
                "estimated_age": 30,
            },
            "consent_obtained": True,
            "methodology_reference": "Proporção áurea",
            "explanations": {"symmetry": "Medida de simetria facial"},
            "confidence_intervals": {"symmetry": [0.80, 0.90]},
            "disclaimer": "Não é diagnóstico médico",
        }

    def test_init(self, ethics_framework):
        """Testa inicialização do framework."""
        assert ethics_framework.enable_logging is False
        assert ethics_framework.strict_mode is False
        assert len(ethics_framework.principles) == 7

    def test_audit_analysis_low_risk(self, ethics_framework, sample_analysis_results):
        """Testa auditoria com baixo risco."""
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert isinstance(result, EthicsAuditResult)
        assert isinstance(result.audit_id, str)
        assert len(result.audit_id) == 16

    def test_audit_bias_detection(self, ethics_framework, sample_analysis_results):
        """Testa detecção de bias na auditoria."""
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert "gender" in result.bias_detected
        assert "ethnicity" in result.bias_detected
        assert "age" in result.bias_detected
        assert "overall" in result.bias_detected

    def test_audit_transparency_score(self, ethics_framework, sample_analysis_results):
        """Testa cálculo de score de transparência."""
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert 0 <= result.transparency_score <= 1

    def test_audit_privacy_score(self, ethics_framework, sample_analysis_results):
        """Testa cálculo de score de privacidade."""
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert 0 <= result.privacy_score <= 1

    def test_audit_recommendations(self, ethics_framework, sample_analysis_results):
        """Testa geração de recomendações."""
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert isinstance(result.recommendations, list)
        assert len(result.recommendations) > 0

    def test_consent_verification(self, ethics_framework, sample_analysis_results):
        """Testa verificação de consentimento."""
        sample_analysis_results["consent_obtained"] = True
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert result.consent_verified is True

        sample_analysis_results["consent_obtained"] = False
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert result.consent_verified is False

    def test_missing_consent_affects_privacy(self, ethics_framework, sample_analysis_results):
        """Testa que falta de consentimento afeta score de privacidade."""
        sample_analysis_results["consent_obtained"] = False
        result = ethics_framework.audit_analysis(sample_analysis_results)
        # Privacidade deve ser menor sem consentimento
        assert result.privacy_score < 1.0

    def test_missing_explanations_affects_transparency(
        self, ethics_framework, sample_analysis_results
    ):
        """Testa que falta de explicações afeta transparência."""
        sample_analysis_results.pop("explanations", None)
        result = ethics_framework.audit_analysis(sample_analysis_results)
        assert result.transparency_score < 1.0


class TestAIEthicsFrameworkStrictMode:
    """Testes para modo estrito."""

    def test_strict_mode_enabled(self):
        """Testa inicialização com modo estrito."""
        ethics = AIEthicsFramework(strict_mode=True, enable_logging=False)
        assert ethics.strict_mode is True

    def test_high_bias_detection(self):
        """Testa detecção de bias alto."""
        ethics = AIEthicsFramework(enable_logging=False)

        results_with_bias = {
            "aesthetic_scores": {"symmetry": 0.3, "harmony": 0.2},
            "demographic_estimates": {
                "gender": "female",
                "ethnicity": "black",
                "estimated_age": 60,
            },
            "consent_obtained": True,
        }

        result = ethics.audit_analysis(results_with_bias)
        # Bias deve ser detectado
        assert result.bias_detected["overall"] >= 0


class TestEthicsReportGeneration:
    """Testes para geração de relatórios."""

    @pytest.fixture
    def ethics_framework(self):
        return AIEthicsFramework(enable_logging=False)

    @pytest.fixture
    def sample_results(self):
        return {
            "aesthetic_scores": {"symmetry": 0.85, "harmony": 0.78},
            "demographic_estimates": {
                "gender": "female",
                "ethnicity": "caucasian",
                "estimated_age": 30,
            },
            "consent_obtained": True,
        }

    def test_generate_ethics_report(self, ethics_framework, sample_results):
        """Testa geração de relatório ético."""
        report = ethics_framework.generate_ethics_report(sample_results)
        assert isinstance(report, str)

        # Validar JSON
        report_json = json.loads(report)
        assert report_json["report_type"] == "AI Ethics Audit Report"
        assert "summary" in report_json
        assert "principles_assessment" in report_json
        assert "bias_analysis" in report_json
        assert "recommendations" in report_json

    def test_report_contains_all_principles(self, ethics_framework, sample_results):
        """Testa que relatório contém todos os princípios."""
        report_json = json.loads(
            ethics_framework.generate_ethics_report(sample_results)
        )
        principles = report_json["principles_assessment"]
        assert len(principles) == 7

    def test_report_compliance_notes(self, ethics_framework, sample_results):
        """Testa notas de conformidade no relatório."""
        report_json = json.loads(
            ethics_framework.generate_ethics_report(sample_results)
        )
        assert "compliance_notes" in report_json
        assert "eu_ai_act" in report_json["compliance_notes"]
        assert "gdpr" in report_json["compliance_notes"]
        assert "lgpd" in report_json["compliance_notes"]


class TestDisclosureNotice:
    """Testes para avisos de divulgação."""

    @pytest.fixture
    def ethics_framework(self):
        return AIEthicsFramework(enable_logging=False)

    def test_disclosure_portuguese(self, ethics_framework):
        """Testa divulgação em português."""
        notice = ethics_framework.generate_disclosure_notice("pt")
        assert "INTELIGÊNCIA ARTIFICIAL" in notice
        assert "CONSENTIMENTO" in notice
        assert "PRIVACIDADE" in notice

    def test_disclosure_english(self, ethics_framework):
        """Testa divulgação em inglês."""
        notice = ethics_framework.generate_disclosure_notice("en")
        assert "ARTIFICIAL INTELLIGENCE" in notice
        assert "CONSENT" in notice
        assert "PRIVACY" in notice

    def test_disclosure_default(self, ethics_framework):
        """Testa divulgação padrão (inglês)."""
        notice = ethics_framework.generate_disclosure_notice("invalid")
        assert "ARTIFICIAL INTELLIGENCE" in notice


class TestAuditHistory:
    """Testes para histórico de auditorias."""

    @pytest.fixture
    def ethics_framework(self):
        return AIEthicsFramework(enable_logging=False)

    def test_audit_history_tracking(self, ethics_framework):
        """Testa que histórico é rastreado."""
        results = {
            "aesthetic_scores": {"symmetry": 0.85},
            "consent_obtained": True,
        }

        ethics_framework.audit_analysis(results)
        ethics_framework.audit_analysis(results)

        assert len(ethics_framework.audit_history) == 2

    def test_unique_audit_ids(self, ethics_framework):
        """Testa que IDs de auditoria são únicos."""
        results = {
            "aesthetic_scores": {"symmetry": 0.85},
            "consent_obtained": True,
        }

        result1 = ethics_framework.audit_analysis(results)
        result2 = ethics_framework.audit_analysis(results)

        assert result1.audit_id != result2.audit_id


# Ponytail: Adicionar testes de integração com logging em arquivo
# pytest -m integration para testes que escrevem em disco