"""
Pytest Conftest - Fixtures compartilhadas para testes.
"""

import pytest
from PIL import Image
import numpy as np
import io


@pytest.fixture
def sample_color_image():
    """Cria uma imagem colorida de teste 256x256."""
    return Image.new("RGB", (256, 256), color=(128, 128, 128))


@pytest.fixture
def sample_grayscale_image():
    """Cria uma imagem em tons de cinza de teste."""
    return Image.new("L", (256, 256), color=128)


@pytest.fixture
def sample_rgba_image():
    """Cria uma imagem com canal alpha de teste."""
    return Image.new("RGBA", (256, 256), color=(128, 128, 128, 255))


@pytest.fixture
def realistic_face_image():
    """
    Cria uma imagem mais realista simulando um rosto.
    Ponytail: Em testes reais, usar imagens reais de teste.
    """
    img = Image.new("RGB", (512, 512), color=(200, 180, 160))
    pixels = img.load()

    # Simular região facial mais escura
    for i in range(150, 350):
        for j in range(100, 400):
            if pixels:
                pixels[i, j] = (150, 130, 110)

    return img


@pytest.fixture
def image_variations():
    """Cria variações de imagem para testes de robustez."""
    images = {}

    # Diferentes tamanhos
    images["small"] = Image.new("RGB", (128, 128))
    images["medium"] = Image.new("RGB", (256, 256))
    images["large"] = Image.new("RGB", (512, 512))
    images["hd"] = Image.new("RGB", (1920, 1080))

    # Diferentes formatos
    images["rgb"] = Image.new("RGB", (256, 256))
    images["grayscale"] = Image.new("L", (256, 256))
    images["rgba"] = Image.new("RGBA", (256, 256))

    return images


@pytest.fixture
def sample_analysis_results():
    """Resultados de análise de exemplo para testes."""
    return {
        "landmarks": [[x, y] for x, y in zip(range(10), range(10))],
        "aesthetic_scores": {
            "symmetry": 0.85,
            "harmony": 0.78,
            "golden_ratio": 0.92,
            "aging_signs": 0.35,
        },
        "demographic_estimates": {
            "gender": "female",
            "ethnicity": "caucasian",
            "estimated_age": 30,
        },
        "consent_obtained": True,
        "methodology_reference": "Proporção áurea e simetria facial",
        "explanations": {
            "symmetry": "Medida de simetria entre lados esquerdo e direito",
            "harmony": "Relação entre proporções faciais",
        },
        "confidence_intervals": {
            "symmetry": (0.80, 0.90),
            "harmony": (0.73, 0.83),
        },
        "disclaimer": "Esta análise não substitui avaliação profissional",
        "processed_remotely": False,
        "biometric_data_stored": False,
        "deletion_available": True,
        "audit_trail_available": True,
    }


@pytest.fixture
def analysis_with_issues():
    """Resultados de análise com problemas éticos para testes."""
    return {
        "aesthetic_scores": {
            "symmetry": 0.30,  # Score muito baixo
            "harmony": 0.25,
        },
        "demographic_estimates": {
            "gender": "female",
            "ethnicity": "black",  # Pode indicar bias
            "estimated_age": 60,
        },
        "consent_obtained": False,  # Sem consentimento
        "processed_remotely": True,  # Processamento remoto
        "biometric_data_stored": True,  # Dados armazenados
    }


@pytest.fixture
def temp_output_dir(tmp_path):
    """Cria diretório temporário para outputs de testes."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def image_bytes(sample_color_image):
    """Converte imagem para bytes."""
    buffer = io.BytesIO()
    sample_color_image.save(buffer, format="PNG")
    return buffer.getvalue()


@pytest.fixture
def base64_encoded_image(image_bytes):
    """Converte imagem para base64."""
    import base64
    return base64.b64encode(image_bytes).decode("utf-8")