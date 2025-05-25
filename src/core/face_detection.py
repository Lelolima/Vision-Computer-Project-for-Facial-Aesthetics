import cv2
import mediapipe as mp
import numpy as np
from typing import List, Tuple, Optional

class FaceDetector:
    """
    Classe responsável pela detecção de faces e extração de landmarks
    """
    
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )
    
    def detect_face(self, image: np.ndarray) -> Optional[List[Tuple[float, float]]]:
        """
        Detecta face na imagem e retorna os landmarks
        
        Args:
            image: Imagem de entrada (BGR)
            
        Returns:
            Lista de coordenadas dos landmarks ou None se não detectar face
        """
        # Converter BGR para RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Processar a imagem
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
    
    def get_face_profile_points(self, landmarks: List[Tuple[float, float]]) -> dict:
        """
        Extrai pontos específicos do perfil facial
        
        Args:
            landmarks: Lista de landmarks faciais
            
        Returns:
            Dicionário com pontos específicos do perfil
        """
        if not landmarks:
            return {}
        
        # Índices dos pontos importantes para análise estética
        profile_points = {
            'testa': landmarks[10],  # Ponto da testa
            'nariz_ponte': landmarks[6],  # Ponte do nariz
            'nariz_ponta': landmarks[1],  # Ponta do nariz
            'labio_superior': landmarks[13],  # Lábio superior
            'labio_inferior': landmarks[14],  # Lábio inferior
            'queixo': landmarks[175],  # Queixo
            'olho_esquerdo': landmarks[33],  # Canto do olho esquerdo
            'olho_direito': landmarks[263],  # Canto do olho direito
        }
        
        return profile_points
    
    def calculate_facial_proportions(self, landmarks: List[Tuple[float, float]]) -> dict:
        """
        Calcula proporções faciais importantes
        
        Args:
            landmarks: Lista de landmarks faciais
            
        Returns:
            Dicionário com medidas e proporções
        """
        profile_points = self.get_face_profile_points(landmarks)
        
        if not profile_points:
            return {}
        
        # Calcular distâncias importantes
        measurements = {
            'altura_facial': self._calculate_distance(
                profile_points['testa'], profile_points['queixo']
            ),
            'largura_nariz': self._calculate_distance(
                profile_points['olho_esquerdo'], profile_points['olho_direito']
            ) * 0.3,  # Aproximação
            'altura_nariz': self._calculate_distance(
                profile_points['nariz_ponte'], profile_points['nariz_ponta']
            ),
            'altura_labios': self._calculate_distance(
                profile_points['labio_superior'], profile_points['labio_inferior']
            )
        }
        
        return measurements
    
    def _calculate_distance(self, point1: Tuple[float, float], 
                          point2: Tuple[float, float]) -> float:
        """
        Calcula distância euclidiana entre dois pontos
        """
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)