"""
Setup configuration for Vision Computer Project - Facial Aesthetics.

Instalando como pacote:
    pip install -e .

Build para distribuição:
    python setup.py sdist bdist_wheel
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read me do README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Requirements
requirements = (this_directory / "requirements.txt").read_text().splitlines()
# Filtrar comentários e linhas vazias
requirements = [r.strip() for r in requirements if r.strip() and not r.startswith("#")]

setup(
    name="vision-aesthetics",
    version="1.0.0",
    author="Léllo Lima",
    author_email="contato@exemplo.com",
    description="Sistema de análise facial estética com IA ética",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lelolima/Vision-Computer-Project-for-Facial-Aesthetics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "opencv-python-headless>=4.9.0",
        "mediapipe>=0.10.11",
        "torch>=2.2.0",
        "torchvision>=0.17.0",
        "numpy>=1.26.0",
        "Pillow>=10.2.0",
        "scikit-image>=0.22.0",
        "scipy>=1.12.0",
        "fastapi>=0.109.0",
        "streamlit>=1.30.0",
        "PyQt5>=5.15.10",
        "pandas>=2.2.0",
        "pydantic>=2.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-asyncio>=0.23.0",
            "mypy>=1.8.0",
            "black>=24.1.0",
            "ruff>=0.1.14",
        ],
        "gpu": [
            "torch>=2.2.0+cu118",
            "torchvision>=0.17.0+cu118",
            "--extra-index-url https://download.pytorch.org/whl/cu118",
        ],
        "gan": [
            "transformers>=4.37.0",
            "accelerate>=0.26.0",
        ],
        "ethics": [
            "shap>=0.43.0",
            "interpret>=0.3.0",
        ],
        "complete": [
            "insightface>=0.7.3",
            "facenet-pytorch>=2.5.3",
            "reportlab>=4.0.9",
            "sqlalchemy>=2.0.25",
        ],
    },
    entry_points={
        "console_scripts": [
            "vision-aesthetics=src.cli:main",
            "analyze-face=src.core.analyzer:main",
        ],
    },
    include_package_data=True,
    package_data={
        "src": ["py.typed"],
    },
    keywords=[
        "facial-analysis",
        "computer-vision",
        "aesthetics",
        "gan",
        "ai-ethics",
        "medical-ai",
        "deeplearning",
    ],
)