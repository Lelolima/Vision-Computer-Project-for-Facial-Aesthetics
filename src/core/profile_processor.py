import cv2
import numpy as np
from typing import Dict, List, Tuple
from .face_detection import FaceDetector

class ProfileProcessor:
    """
    Classe responsável pelo processamento e análise do perfil facial
    """
    
    def __init__(self):
        self.face_detector = FaceDetector()
    
    def analyze_profile(self, image: np.ndarray) -> Dict:
        """
        Analisa o perfil facial completo
        
        Args:
            image: Imagem de entrada
            
        Returns:
            Dicionário com análise completa do perfil
        """
        landmarks = self.face_detector.detect_face(image)
        
        if not landmarks:
            return {'error': 'Nenhuma face detectada na imagem'}
        
        profile_points = self.face_detector.get_face_profile_points(landmarks)
        measurements = self.face_detector.calculate_facial_proportions(landmarks)
        
        analysis = {
            'landmarks': landmarks,
            'profile_points': profile_points,
            'measurements': measurements,
            'recommendations': self._generate_recommendations(measurements),
            'symmetry_score': self._calculate_symmetry(landmarks)
        }
        
        return analysis
    
    def simulate_rhinoplasty(self, image: np.ndarray, 
                           adjustment_factor: float = 0.1) -> np.ndarray:
        """
        Simula procedimento de rinoplastia
        
        Args:
            image: Imagem original
            adjustment_factor: Fator de ajuste (0.0 a 1.0)
            
        Returns:
            Imagem com simulação da rinoplastia
        """
        landmarks = self.face_detector.detect_face(image)
        
        if not landmarks:
            return image
        
        # Criar cópia da imagem para modificação
        result_image = image.copy()
        
        # Pontos do nariz para modificação
        nose_points = self._get_nose_contour(landmarks)
        
        # Aplicar transformação suave
        result_image = self._apply_nose_transformation(
            result_image, nose_points, adjustment_factor
        )
        
        return result_image
    
    def simulate_lip_enhancement(self, image: np.ndarray, 
                               volume_increase: float = 0.2) -> np.ndarray:
        """
        Simula preenchimento labial
        
        Args:
            image: Imagem original
            volume_increase: Aumento de volume (0.0 a 1.0)
            
        Returns:
            Imagem com simulação do preenchimento
        """
        landmarks = self.face_detector.detect_face(image)
        
        if not landmarks:
            return image
        
        result_image = image.copy()
        
        # Pontos dos lábios
        lip_points = self._get_lip_contour(landmarks)
        
        # Aplicar aumento de volume
        result_image = self._apply_lip_enhancement(
            result_image, lip_points, volume_increase
        )
        
        return result_image
    
    def _generate_recommendations(self, measurements: Dict) -> List[str]:
        """
        Gera recomendações baseadas nas medidas faciais
        """
        recommendations = []
        
        if not measurements:
            return recommendations
        
        # Análise da proporção nasal
        if 'altura_nariz' in measurements and 'altura_facial' in measurements:
            nose_ratio = measurements['altura_nariz'] / measurements['altura_facial']
            
            if nose_ratio > 0.15:
                recommendations.append(
                    "Rinoplastia pode harmonizar as proporções faciais"
                )
        
        # Análise labial
        if 'altura_labios' in measurements:
            if measurements['altura_labios'] < 15:
                recommendations.append(
                    "Preenchimento labial pode dar mais volume e definição"
                )
        
        return recommendations
    
    def _calculate_symmetry(self, landmarks: List[Tuple[float, float]]) -> float:
        """
        Calcula score de simetria facial (0-100)
        """
        if not landmarks:
            return 0.0
        
        # Implementação simplificada de cálculo de simetria
        # Baseada na comparação entre lados esquerdo e direito
        
        # Pontos de referência para simetria
        left_points = landmarks[0:len(landmarks)//2]
        right_points = landmarks[len(landmarks)//2:]
        
        # Calcular diferenças
        differences = []
        for i in range(min(len(left_points), len(right_points))):
            diff = abs(left_points[i][0] - right_points[i][0])
            differences.append(diff)
        
        # Score de simetria (invertido - menor diferença = maior score)
        avg_diff = np.mean(differences) if differences else 0
        symmetry_score = max(0, 100 - avg_diff)
        
        return symmetry_score
    
    def _get_nose_contour(self, landmarks: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """
        Extrai contorno do nariz dos landmarks
        """
        # Índices aproximados dos pontos do nariz
        nose_indices = [1, 2, 5, 6, 19, 20, 94, 125, 141, 235, 236, 237, 238, 239, 240, 241, 242]
        
        nose_points = []
        for idx in nose_indices:
            if idx < len(landmarks):
                nose_points.append(landmarks[idx])
        
        return nose_points
    
    def _get_lip_contour(self, landmarks: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """
        Extrai contorno dos lábios dos landmarks
        """
        # Índices aproximados dos pontos dos lábios
        lip_indices = [61, 84, 17, 314, 405, 320, 307, 375, 321, 308, 324, 318]
        
        lip_points = []
        for idx in lip_indices:
            if idx < len(landmarks):
                lip_points.append(landmarks[idx])
        
        return lip_points
    
    def _apply_nose_transformation(self, image: np.ndarray, 
                                 nose_points: List[Tuple[float, float]], 
                                 factor: float) -> np.ndarray:
        """
        Aplica transformação no nariz
        """
        # Implementação simplificada de transformação
        # Em um projeto real, usaria técnicas mais avançadas de morphing
        
        if not nose_points:
            return image
        
        # Criar máscara para a região do nariz
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        
        # Converter pontos para array numpy
        points = np.array(nose_points, dtype=np.int32)
        
        # Criar contorno
        cv2.fillPoly(mask, [points], 255)
        
        # Aplicar suavização na região
        kernel = np.ones((5,5), np.float32) / 25
        smoothed = cv2.filter2D(image, -1, kernel)
        
        # Combinar imagens
        result = image.copy()
        result[mask > 0] = smoothed[mask > 0]
        
        return result
    
    def _apply_lip_enhancement(self, image: np.ndarray, 
                             lip_points: List[Tuple[float, float]], 
                             volume: float) -> np.ndarray:
        """
        Aplica aumento de volume nos lábios
        """
        if not lip_points:
            return image
        
        # Implementação simplificada
        # Em produção, usaria técnicas mais sofisticadas
        
        result = image.copy()
        
        # Aplicar realce de cor nos lábios
        points = np.array(lip_points, dtype=np.int32)
        
        # Criar máscara
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [points], 255)
        
        # Aumentar saturação na região dos lábios
        hsv = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
        hsv[mask > 0, 1] = np.clip(hsv[mask > 0, 1] * (1 + volume), 0, 255)
        result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        
        return result