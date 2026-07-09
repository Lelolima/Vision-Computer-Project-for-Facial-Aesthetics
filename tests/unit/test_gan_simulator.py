"""
Testes Unitários - GAN Simulator
"""

import pytest
import numpy as np
from PIL import Image
from src.ai.gan_simulator import GANSimulator, GANSimulatorConfig


class TestGANSimulatorConfig:
    """Testes para configuração do GAN Simulator."""

    def test_default_config(self):
        """Testa configuração padrão."""
        config = GANSimulatorConfig()
        assert config.model_type == "fallback"
        assert config.resolution == 256
        assert config.device is None

    def test_custom_config(self):
        """Testa configuração customizada."""
        config = GANSimulatorConfig(
            model_type="pix2pix",
            resolution=128,
            device="cpu"
        )
        assert config.model_type == "pix2pix"
        assert config.resolution == 128
        assert config.device == "cpu"

    def test_supported_models(self):
        """Testa lista de modelos suportados."""
        assert "stylegan2" in GANSimulatorConfig.SUPPORTED_MODELS
        assert "pix2pix" in GANSimulatorConfig.SUPPORTED_MODELS
        assert "fallback" in GANSimulatorConfig.SUPPORTED_MODELS


class TestGANSimulator:
    """Testes para o simulador GAN."""

    @pytest.fixture
    def simulator_fallback(self):
        """Fixture para simulador em modo fallback."""
        return GANSimulator(GANSimulatorConfig(model_type="fallback"))

    @pytest.fixture
    def sample_image(self):
        """Fixture para imagem de teste."""
        return Image.new("RGB", (256, 256), color="white")

    def test_init_fallback_mode(self, simulator_fallback):
        """Testa inicialização em modo fallback."""
        assert simulator_fallback.config.model_type == "fallback"
        assert simulator_fallback.model is None  # Sem modelo no fallback

    def test_get_model_info(self, simulator_fallback):
        """Testa informações do modelo."""
        info = simulator_fallback.get_model_info()
        assert info["model_type"] == "fallback"
        assert info["device"] in ["cpu", "cuda"]
        assert isinstance(info["supported_procedures"], list)

    def test_simulate_rinoplastia(self, simulator_fallback, sample_image):
        """Testa simulação de rinoplastia."""
        result = simulator_fallback.simulate_procedure(
            sample_image,
            procedure="rinoplastia",
            intensity=0.5
        )
        assert isinstance(result, Image.Image)
        assert result.size == sample_image.size

    def test_simulate_preenchimento_labial(self, simulator_fallback, sample_image):
        """Testa simulação de preenchimento labial."""
        result = simulator_fallback.simulate_procedure(
            sample_image,
            procedure="preenchimento_labial",
            intensity=0.7
        )
        assert isinstance(result, Image.Image)

    def test_simulate_lifting_facial(self, simulator_fallback, sample_image):
        """Testa simulação de lifting facial."""
        result = simulator_fallback.simulate_procedure(
            sample_image,
            procedure="lifting_facial",
            intensity=0.6
        )
        assert isinstance(result, Image.Image)

    def test_intensity_range(self, simulator_fallback, sample_image):
        """Testa diferentes intensidades."""
        for intensity in [0.0, 0.25, 0.5, 0.75, 1.0]:
            result = simulator_fallback.simulate_procedure(
                sample_image,
                procedure="rinoplastia",
                intensity=intensity
            )
            assert isinstance(result, Image.Image)

    def test_blend_factor(self, simulator_fallback, sample_image):
        """Testa fator de blend."""
        result = simulator_fallback.simulate_procedure(
            sample_image,
            procedure="rinoplastia",
            intensity=0.5,
            blend_factor=0.3
        )
        assert isinstance(result, Image.Image)

    def test_unknown_procedure_fallback(self, simulator_fallback, sample_image):
        """Testa procedimento desconhecido (deve usar fallback)."""
        result = simulator_fallback.simulate_procedure(
            sample_image,
            procedure="procedimento_inexistente",
            intensity=0.5
        )
        assert isinstance(result, Image.Image)

    def test_all_procedures(self, simulator_fallback, sample_image):
        """Testa todos os procedimentos suportados."""
        procedures = [
            "rinoplastia",
            "preenchimento_labial",
            "lifting_facial",
            "reducao_papada",
            "aumento_macas",
            "afinamento_rosto",
            "juvenilizacao",
            "contorno_facial"
        ]
        for procedure in procedures:
            result = simulator_fallback.simulate_procedure(
                sample_image,
                procedure=procedure,
                intensity=0.5
            )
            assert isinstance(result, Image.Image)


class TestGANSimulatorEdgeCases:
    """Testes para casos extremos."""

    @pytest.fixture
    def simulator(self):
        return GANSimulator(GANSimulatorConfig(model_type="fallback"))

    def test_zero_intensity(self, simulator):
        """Testa intensidade zero."""
        image = Image.new("RGB", (256, 256))
        result = simulator.simulate_procedure(image, "rinoplastia", intensity=0.0)
        assert isinstance(result, Image.Image)

    def test_full_intensity(self, simulator):
        """Testa intensidade máxima."""
        image = Image.new("RGB", (256, 256))
        result = simulator.simulate_procedure(image, "rinoplastia", intensity=1.0)
        assert isinstance(result, Image.Image)

    def test_different_image_sizes(self, simulator):
        """Testa diferentes tamanhos de imagem."""
        sizes = [(128, 128), (256, 256), (512, 512), (800, 600)]
        for width, height in sizes:
            image = Image.new("RGB", (width, height))
            result = simulator.simulate_procedure(image, "rinoplastia", intensity=0.5)
            assert isinstance(result, Image.Image)

    def test_different_image_modes(self, simulator):
        """Testa diferentes modos de imagem."""
        modes = ["RGB", "L", "RGBA"]
        for mode in modes:
            image = Image.new(mode, (256, 256))
            # Converter para RGB se necessário
            if mode != "RGB":
                image = image.convert("RGB")
            result = simulator.simulate_procedure(image, "rinoplastia", intensity=0.5)
            assert isinstance(result, Image.Image)


# Ponytail: Adicionar testes de integração com GPU quando disponível
# pytest -m gpu para testes que requerem GPU