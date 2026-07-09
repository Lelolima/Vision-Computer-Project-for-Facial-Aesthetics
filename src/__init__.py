"""
Vision Computer Project - Pacote Principal

Análise facial estética utilizando Computer Vision e IA com princípios éticos.
"""

__version__ = "1.0.0"
__author__ = "Léllo Lima"
__email__ = "contato@exemplo.com"

from src.core.analyzer import FacialAnalyzer
from src.ai.gan_simulator import GANSimulator
from src.ethics.ai_ethics import AIEthicsFramework

__all__ = [
    "FacialAnalyzer",
    "GANSimulator",
    "AIEthicsFramework",
]