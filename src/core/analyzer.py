"""
Fachada de análise facial usada pela API.

Delega para ``AdvancedFacialAnalyzer`` (MediaPipe FaceMesh). Não retorna
pontuações fixas: se nenhuma face for detectada, lança ``FaceNotDetectedError``.
"""

from typing import Any, Dict, Optional

import cv2
import numpy as np


class FaceNotDetectedError(ValueError):
    """Nenhuma face detectada na imagem."""


class InvalidImageError(ValueError):
    """Bytes recebidos não são uma imagem decodificável."""


class FacialAnalyzer:
    """Analisador facial principal (wrapper de AdvancedFacialAnalyzer)."""

    def __init__(self, model_path: Optional[str] = None):
        self.model_path = model_path
        self._engine = None

    @property
    def engine(self):
        if self._engine is None:
            from src.core.advanced_analysis import AdvancedFacialAnalyzer

            self._engine = AdvancedFacialAnalyzer()
        return self._engine

    def analyze_array(self, image_bgr: np.ndarray) -> Dict[str, Any]:
        result = self.engine.comprehensive_analysis(image_bgr)
        if "error" in result:
            raise FaceNotDetectedError(result["error"])
        aesthetic = result["aesthetic_analysis"]
        return {
            "landmarks": [[float(x), float(y)] for x, y in result["landmarks"]],
            "aesthetic_scores": {
                "symmetry": float(aesthetic["symmetry_score"]),
                "golden_ratio": float(aesthetic["golden_ratio_score"]),
                "skin_quality": float(aesthetic["skin_quality_score"]),
            },
            "face_shape": result["face_shape"],
            "confidence_score": float(result["confidence_score"]),
            "methodology_reference": "Proporção áurea e simetria facial (MediaPipe FaceMesh)",
        }

    def analyze_from_bytes(self, data: bytes) -> Dict[str, Any]:
        arr = np.frombuffer(data, dtype=np.uint8)
        image = cv2.imdecode(arr, cv2.IMREAD_COLOR) if arr.size else None
        if image is None:
            raise InvalidImageError("Não foi possível decodificar a imagem")
        return self.analyze_array(image)

    def analyze(self, image_path: str) -> Dict[str, Any]:
        with open(image_path, "rb") as fh:
            return self.analyze_from_bytes(fh.read())


__all__ = ["FacialAnalyzer", "FaceNotDetectedError", "InvalidImageError"]
