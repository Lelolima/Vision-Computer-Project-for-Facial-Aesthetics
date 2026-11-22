"""
Vision Computer Project - Pacote Principal

Análise facial estética utilizando Computer Vision e IA com princípios éticos.
"""

__version__ = "1.0.0"
__author__ = "Léllo Lima"
__email__ = "contato@exemplo.com"




def __getattr__(name):
    """Importação preguiçosa: evita carregar torch/mediapipe ao importar o pacote."""
    if name == "FacialAnalyzer":
        from src.core.analyzer import FacialAnalyzer
        return FacialAnalyzer
    if name == "GANSimulator":
        from src.ai.gan_simulator import GANSimulator
        return GANSimulator
    if name == "AIEthicsFramework":
        from src.ethics.ai_ethics import AIEthicsFramework
        return AIEthicsFramework
    raise AttributeError(name)


__all__ = [
    "FacialAnalyzer",
    "GANSimulator",
    "AIEthicsFramework",
]