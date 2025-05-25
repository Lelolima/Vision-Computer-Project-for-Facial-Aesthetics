import cv2
import numpy as np
from typing import Dict, List, Tuple, Optional
import mediapipe as mp
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class FacialMeasurements:
    """Estrutura para medidas faciais"""
    face_width: float
    face_height: float
    eye_distance: float
    nose_width: float
    nose_height: float
    lip_width: float
    lip_height: float
    jaw_width: float
    forehead_height: float
    cheek_width: float

@dataclass
class AestheticAnalysis:
    """Resultado da análise estética"""
    golden_ratio_score: float
    symmetry_score: float
    proportion_scores: Dict[str, float]
    recommendations: List[str]
    face_shape: str
    skin_quality_score: float

class AdvancedFacialAnalyzer:
    """
    Analisador facial avançado com IA
    """
    
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        
        # Índices dos landmarks importantes
        self.landmark_indices = {
            'face_oval': [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109],
            'left_eye': [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398],
            'right_eye': [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246],
            'nose': [1, 2, 5, 4, 6, 19, 94, 168, 8, 9, 10, 151, 195, 197, 196, 3, 51, 48, 115, 131, 134, 102, 49, 220, 305, 290, 328, 326, 2, 97, 99, 68],
            'lips': [61, 84, 17, 314, 405, 320, 307, 375, 321, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308],
            'jawline': [172, 136, 150, 149, 176, 148, 152, 377, 400, 378, 379, 365, 397, 288, 361, 323]
        }
    
    def comprehensive_analysis(self, image: np.ndarray) -> Dict:
        """
        Análise facial completa e avançada
        """
        # Detectar landmarks
        landmarks = self._detect_landmarks(image)
        if not landmarks:
            return {'error': 'Não foi possível detectar face na imagem'}
        
        # Extrair medidas
        measurements = self._extract_detailed_measurements(landmarks, image.shape)
        
        # Análise estética
        aesthetic_analysis = self._perform_aesthetic_analysis(measurements, landmarks)
        
        # Análise de qualidade da pele
        skin_analysis = self._analyze_skin_quality(image, landmarks)
        
        # Determinar formato do rosto
        face_shape = self._determine_face_shape(measurements)
        
        # Gerar recomendações personalizadas
        recommendations = self._generate_advanced_recommendations(
            measurements, aesthetic_analysis, face_shape, skin_analysis
        )
        
        return {
            'landmarks': landmarks,
            'measurements': measurements.__dict__,
            'aesthetic_analysis': aesthetic_analysis.__dict__,
            'skin_analysis': skin_analysis,
            'face_shape': face_shape,
            'recommendations': recommendations,
            'confidence_score': self._calculate_confidence_score(landmarks)
        }
    
    def _detect_landmarks(self, image: np.ndarray) -> Optional[List[Tuple[int, int]]]:
        """
        Detecta landmarks faciais com alta precisão
        """
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_image)
        
        if results.multi_face_landmarks:
            landmarks = []
            face_landmarks = results.multi_face_landmarks[0]
            h, w = image.shape[:2]
            
            for landmark in face_landmarks.landmark:
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                landmarks.append((x, y))
            
            return landmarks
        return None
    
    def _extract_detailed_measurements(self, landmarks: List[Tuple[int, int]], 
                                     image_shape: Tuple[int, int]) -> FacialMeasurements:
        """
        Extrai medidas faciais detalhadas
        """
        h, w = image_shape[:2]
        
        # Pontos de referência
        left_eye_center = self._get_center_point([landmarks[i] for i in [33, 133]])
        right_eye_center = self._get_center_point([landmarks[i] for i in [362, 263]])
        nose_tip = landmarks[1]
        mouth_center = self._get_center_point([landmarks[i] for i in [61, 291]])
        
        # Calcular medidas
        face_width = euclidean(landmarks[234], landmarks[454])
        face_height = euclidean(landmarks[10], landmarks[152])
        eye_distance = euclidean(left_eye_center, right_eye_center)
        nose_width = euclidean(landmarks[131], landmarks[360])
        nose_height = euclidean(landmarks[19], landmarks[1])
        lip_width = euclidean(landmarks[61], landmarks[291])
        lip_height = euclidean(landmarks[13], landmarks[14])
        jaw_width = euclidean(landmarks[172], landmarks[397])
        forehead_height = euclidean(landmarks[10], landmarks[151])
        cheek_width = euclidean(landmarks[116], landmarks[345])
        
        return FacialMeasurements(
            face_width=face_width,
            face_height=face_height,
            eye_distance=eye_distance,
            nose_width=nose_width,
            nose_height=nose_height,
            lip_width=lip_width,
            lip_height=lip_height,
            jaw_width=jaw_width,
            forehead_height=forehead_height,
            cheek_width=cheek_width
        )
    
    def _perform_aesthetic_analysis(self, measurements: FacialMeasurements, 
                                  landmarks: List[Tuple[int, int]]) -> AestheticAnalysis:
        """
        Realiza análise estética baseada em proporções áureas
        """
        # Proporção áurea (1.618)
        golden_ratio = 1.618
        
        # Calcular scores de proporção
        face_ratio = measurements.face_height / measurements.face_width
        eye_nose_ratio = measurements.eye_distance / measurements.nose_width
        nose_mouth_ratio = measurements.nose_width / measurements.lip_width
        
        # Score da proporção áurea
        golden_ratio_score = self._calculate_golden_ratio_score(
            face_ratio, eye_nose_ratio, nose_mouth_ratio
        )
        
        # Score de simetria
        symmetry_score = self._calculate_advanced_symmetry(landmarks)
        
        # Scores de proporções individuais
        proportion_scores = {
            'face_ratio': min(100, 100 - abs(face_ratio - golden_ratio) * 50),
            'eye_spacing': min(100, 100 - abs(eye_nose_ratio - 1.5) * 30),
            'nose_mouth': min(100, 100 - abs(nose_mouth_ratio - 1.2) * 40)
        }
        
        return AestheticAnalysis(
            golden_ratio_score=golden_ratio_score,
            symmetry_score=symmetry_score,
            proportion_scores=proportion_scores,
            recommendations=[],
            face_shape="",
            skin_quality_score=0.0
        )
    
    def _analyze_skin_quality(self, image: np.ndarray, 
                            landmarks: List[Tuple[int, int]]) -> Dict:
        """
        Analisa qualidade da pele
        """
        # Extrair região facial
        face_region = self._extract_face_region(image, landmarks)
        
        # Converter para diferentes espaços de cor
        hsv = cv2.cvtColor(face_region, cv2.COLOR_BGR2HSV)
        lab = cv2.cvtColor(face_region, cv2.COLOR_BGR2LAB)
        
        # Análise de textura
        gray = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)
        texture_score = self._calculate_texture_score(gray)
        
        # Análise de uniformidade de cor
        color_uniformity = self._calculate_color_uniformity(lab)
        
        # Detecção de imperfeições
        blemishes = self._detect_blemishes(face_region)
        
        # Score geral da pele
        overall_score = (texture_score + color_uniformity + (100 - len(blemishes))) / 3
        
        return {
            'texture_score': texture_score,
            'color_uniformity': color_uniformity,
            'blemish_count': len(blemishes),
            'overall_score': overall_score,
            'recommendations': self._generate_skin_recommendations(overall_score)
        }
    
    def _determine_face_shape(self, measurements: FacialMeasurements) -> str:
        """
        Determina o formato do rosto
        """
        face_ratio = measurements.face_height / measurements.face_width
        jaw_face_ratio = measurements.jaw_width / measurements.face_width
        forehead_face_ratio = measurements.forehead_height / measurements.face_height
        
        if face_ratio > 1.3:
            if jaw_face_ratio < 0.8:
                return "Oval"
            else:
                return "Retangular"
        elif face_ratio < 1.1:
            if jaw_face_ratio > 0.9:
                return "Quadrado"
            else:
                return "Redondo"
        else:
            if forehead_face_ratio > 0.4:
                return "Coração"
            else:
                return "Diamante"
    
    def _generate_advanced_recommendations(self, measurements: FacialMeasurements,
                                         aesthetic: AestheticAnalysis,
                                         face_shape: str,
                                         skin_analysis: Dict) -> List[str]:
        """
        Gera recomendações personalizadas avançadas
        """
        recommendations = []
        
        # Recomendações baseadas no formato do rosto
        shape_recommendations = {
            "Oval": ["Seu rosto tem proporções ideais", "Qualquer procedimento deve ser sutil"],
            "Redondo": ["Contorno facial pode alongar o rosto", "Preenchimento no queixo pode ajudar"],
            "Quadrado": ["Suavização da mandíbula com botox", "Preenchimento nas têmporas"],
            "Coração": ["Preenchimento no queixo para equilibrar", "Redução da testa se necessário"],
            "Retangular": ["Preenchimento nas bochechas", "Suavização da mandíbula"],
            "Diamante": ["Preenchimento nas têmporas e queixo", "Harmonização geral"]
        }
        
        recommendations.extend(shape_recommendations.get(face_shape, []))
        
        # Recomendações baseadas em proporções
        if aesthetic.golden_ratio_score < 70:
            recommendations.append("Harmonização facial para melhorar proporções")
        
        if aesthetic.symmetry_score < 80:
            recommendations.append("Procedimentos para melhorar simetria facial")
        
        # Recomendações baseadas na pele
        if skin_analysis['overall_score'] < 70:
            recommendations.extend(skin_analysis['recommendations'])
        
        # Recomendações específicas por medida
        if measurements.nose_width / measurements.face_width > 0.25:
            recommendations.append("Rinoplastia para refinar o nariz")
        
        if measurements.lip_height < 10:
            recommendations.append("Preenchimento labial para mais volume")
        
        return recommendations
    
    # Métodos auxiliares
    def _get_center_point(self, points: List[Tuple[int, int]]) -> Tuple[int, int]:
        """Calcula ponto central"""
        x = sum(p[0] for p in points) // len(points)
        y = sum(p[1] for p in points) // len(points)
        return (x, y)
    
    def _calculate_golden_ratio_score(self, *ratios) -> float:
        """Calcula score baseado na proporção áurea"""
        golden_ratio = 1.618
        deviations = [abs(ratio - golden_ratio) for ratio in ratios]
        avg_deviation = sum(deviations) / len(deviations)
        return max(0, 100 - avg_deviation * 50)
    
    def _calculate_advanced_symmetry(self, landmarks: List[Tuple[int, int]]) -> float:
        """Calcula simetria facial avançada"""
        # Implementação mais sofisticada de cálculo de simetria
        center_x = sum(p[0] for p in landmarks) / len(landmarks)
        
        left_points = [p for p in landmarks if p[0] < center_x]
        right_points = [p for p in landmarks if p[0] > center_x]
        
        # Calcular diferenças de simetria
        symmetry_errors = []
        for lp in left_points:
            # Encontrar ponto correspondente do lado direito
            mirrored_x = 2 * center_x - lp[0]
            closest_right = min(right_points, key=lambda rp: abs(rp[0] - mirrored_x))
            error = euclidean(lp, (2 * center_x - closest_right[0], closest_right[1]))
            symmetry_errors.append(error)
        
        avg_error = sum(symmetry_errors) / len(symmetry_errors) if symmetry_errors else 0
        return max(0, 100 - avg_error)
    
    def _extract_face_region(self, image: np.ndarray, 
                           landmarks: List[Tuple[int, int]]) -> np.ndarray:
        """Extrai região facial"""
        # Criar máscara da face
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        face_points = np.array([landmarks[i] for i in self.landmark_indices['face_oval']], dtype=np.int32)
        cv2.fillPoly(mask, [face_points], 255)
        
        # Aplicar máscara
        face_region = cv2.bitwise_and(image, image, mask=mask)
        
        # Extrair bounding box
        x, y, w, h = cv2.boundingRect(face_points)
        return face_region[y:y+h, x:x+w]
    
    def _calculate_texture_score(self, gray_image: np.ndarray) -> float:
        """Calcula score de textura da pele"""
        # Usar Laplaciano para detectar variações de textura
        laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
        # Normalizar para score 0-100
        return min(100, max(0, 100 - laplacian_var / 10))
    
    def _calculate_color_uniformity(self, lab_image: np.ndarray) -> float:
        """Calcula uniformidade de cor"""
        # Calcular desvio padrão dos canais a e b
        _, a, b = cv2.split(lab_image)
        std_a = np.std(a)
        std_b = np.std(b)
        avg_std = (std_a + std_b) / 2
        return max(0, 100 - avg_std)
    
    def _detect_blemishes(self, image: np.ndarray) -> List[Tuple[int, int]]:
        """Detecta imperfeições na pele"""
        # Converter para escala de cinza
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Aplicar filtro para detectar pontos escuros
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        diff = cv2.absdiff(gray, blurred)
        
        # Threshold para detectar imperfeições
        _, thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
        
        # Encontrar contornos
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        blemishes = []
        for contour in contours:
            if cv2.contourArea(contour) > 5:  # Filtrar pontos muito pequenos
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    blemishes.append((cx, cy))
        
        return blemishes
    
    def _generate_skin_recommendations(self, score: float) -> List[str]:
        """Gera recomendações para cuidados com a pele"""
        if score >= 80:
            return ["Pele em excelente estado", "Manutenção com hidratação"]
        elif score >= 60:
            return ["Limpeza de pele profissional", "Tratamentos de hidratação"]
        else:
            return ["Peeling químico", "Tratamento para uniformização", "Cuidados intensivos"]
    
    def _calculate_confidence_score(self, landmarks: List[Tuple[int, int]]) -> float:
        """Calcula score de confiança da detecção"""
        # Baseado na quantidade e qualidade dos landmarks detectados
        if len(landmarks) >= 468:  # MediaPipe face mesh completo
            return 95.0
        elif len(landmarks) >= 400:
            return 85.0
        elif len(landmarks) >= 300:
            return 75.0
        else:
            return 60.0