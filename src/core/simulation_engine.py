import numpy as np
from typing import Dict, List, Tuple, Optional
from scipy.spatial.distance import euclidean
from scipy.interpolate import griddata
from skimage import transform, filters
import matplotlib.pyplot as plt
import cv2

class AdvancedSimulationEngine:
    """
    Motor de simulação avançada para procedimentos estéticos
    """
    
    def __init__(self):
        self.transformation_cache = {}
    
    def simulate_procedure(self, image: np.ndarray, landmarks: List[Tuple[int, int]], 
                         procedure_type: str, intensity: float = 0.5) -> np.ndarray:
        """
        Simula procedimento estético com transformações avançadas
        
        Args:
            image: Imagem original
            landmarks: Pontos faciais detectados
            procedure_type: Tipo de procedimento ('rhinoplasty', 'lip_enhancement', etc)
            intensity: Intensidade da transformação (0.0 a 1.0)
            
        Returns:
            Imagem com simulação aplicada
        """
        if procedure_type == 'rhinoplasty':
            return self.simulate_rhinoplasty(image, landmarks, intensity)
        elif procedure_type == 'lip_enhancement':
            return self.simulate_lip_enhancement(image, landmarks, intensity)
        elif procedure_type == 'face_contouring':
            return self.simulate_face_contouring(image, landmarks, intensity)
        elif procedure_type == 'brow_lift':
            return self.simulate_brow_lift(image, landmarks, intensity)
        elif procedure_type == 'skin_rejuvenation':
            return self.simulate_skin_rejuvenation(image, intensity)
        else:
            return image
    
    def simulate_rhinoplasty(self, image: np.ndarray, landmarks: List[Tuple[int, int]], 
                           intensity: float = 0.5) -> np.ndarray:
        """
        Simula rinoplastia com transformação avançada
        """
        # Identificar pontos do nariz
        nose_indices = [1, 2, 3, 4, 5, 6, 19, 94, 97, 98, 99, 129, 134, 166, 198, 199]
        nose_points = [landmarks[i] for i in nose_indices if i < len(landmarks)]
        
        if not nose_points:
            return image
        
        # Criar máscara para a região do nariz
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        nose_contour = np.array(nose_points, dtype=np.int32)
        cv2.fillPoly(mask, [nose_contour], 255)
        
        # Aplicar transformação de afinamento
        result = image.copy()
        h, w = image.shape[:2]
        
        # Ponto central do nariz
        nose_tip = landmarks[1] if 1 < len(landmarks) else nose_points[0]
        nose_bridge = landmarks[6] if 6 < len(landmarks) else nose_points[1]
        
        # Criar grid de deformação
        grid_x, grid_y = np.mgrid[0:h, 0:w]
        
        # Calcular deslocamento baseado na intensidade
        displacement = int(5 * intensity)
        
        # Aplicar transformação apenas na região do nariz
        for y in range(h):
            for x in range(w):
                if mask[y, x] > 0:
                    # Calcular distância ao centro do nariz
                    dx = x - nose_tip[0]
                    dy = y - nose_tip[1]
                    distance = np.sqrt(dx**2 + dy**2)
                    
                    # Aplicar transformação proporcional à distância
                    if distance < 50:
                        weight = (1 - distance/50) * intensity
                        offset_x = int(dx * weight * 0.2)
                        
                        # Aplicar transformação
                        src_x = max(0, min(w-1, x - offset_x))
                        result[y, x] = image[y, src_x]
        
        return result
    
    def simulate_lip_enhancement(self, image: np.ndarray, landmarks: List[Tuple[int, int]], 
                               intensity: float = 0.5) -> np.ndarray:
        """
        Simula preenchimento labial
        """
        # Índices dos pontos dos lábios
        upper_lip_indices = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
        lower_lip_indices = [146, 91, 181, 84, 17, 314, 405, 321, 375, 291]
        
        upper_lip_points = [landmarks[i] for i in upper_lip_indices if i < len(landmarks)]
        lower_lip_points = [landmarks[i] for i in lower_lip_indices if i < len(landmarks)]
        
        if not upper_lip_points or not lower_lip_points:
            return image
        
        # Criar máscaras para os lábios
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        
        upper_contour = np.array(upper_lip_points, dtype=np.int32)
        lower_contour = np.array(lower_lip_points, dtype=np.int32)
        
        cv2.fillPoly(mask, [upper_contour, lower_contour], 255)
        
        # Aplicar dilatação para simular aumento
        kernel_size = int(3 + intensity * 5)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        dilated_mask = cv2.dilate(mask, kernel, iterations=1)
        
        # Aplicar transformação
        result = image.copy()
        indices = np.where(dilated_mask > 0)
        
        # Aplicar cor de lábio mais vibrante
        lip_color_boost = np.array([1.0, 0.8, 1.0]) # Aumentar componente vermelho
        
        for y, x in zip(indices[0], indices[1]):
            if mask[y, x] == 0:  # Apenas na borda expandida
                # Encontrar pixel mais próximo na máscara original
                non_zero = cv2.findNonZero(mask)
                distances = np.sqrt((non_zero[:,:,0] - x) ** 2 + (non_zero[:,:,1] - y) ** 2)
                nearest_idx = np.argmin(distances)
                nx, ny = non_zero[nearest_idx][0]
                
                # Copiar cor do pixel mais próximo
                result[y, x] = image[ny, nx]
                
                # Aplicar aumento de cor
                result[y, x] = np.clip(result[y, x] * lip_color_boost, 0, 255).astype(np.uint8)
        
        return result
    
    def simulate_face_contouring(self, image: np.ndarray, landmarks: List[Tuple[int, int]], 
                               intensity: float = 0.5) -> np.ndarray:
        """
        Simula contorno facial
        """
        # Implementação básica - em produção seria mais sofisticada
        result = image.copy()
        
        # Extrair pontos do contorno facial
        jawline_indices = [172, 136, 150, 149, 176, 148, 152, 377, 400, 378, 379, 365, 397, 288, 361, 323]
        jawline_points = [landmarks[i] for i in jawline_indices if i < len(landmarks)]
        
        if not jawline_points:
            return image
        
        # Criar máscara para o contorno facial
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        jawline_contour = np.array(jawline_points, dtype=np.int32)
        cv2.fillPoly(mask, [jawline_contour], 255)
        
        # Aplicar sombreamento para simular contorno
        shadow_intensity = 0.85 - (intensity * 0.15)  # Mais intensidade = mais sombra
        
        # Aplicar sombreamento apenas na região da mandíbula
        for y in range(mask.shape[0]):
            for x in range(mask.shape[1]):
                if mask[y, x] > 0:
                    # Verificar se está próximo da borda
                    is_edge = False
                    for dy in [-2, -1, 0, 1, 2]:
                        for dx in [-2, -1, 0, 1, 2]:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < mask.shape[0] and 0 <= nx < mask.shape[1]:
                                if mask[ny, nx] == 0:
                                    is_edge = True
                                    break
                        if is_edge:
                            break
                    
                    # Aplicar sombreamento nas bordas
                    if is_edge:
                        result[y, x] = (result[y, x] * shadow_intensity).astype(np.uint8)
        
        return result
    
    def simulate_brow_lift(self, image: np.ndarray, landmarks: List[Tuple[int, int]], 
                         intensity: float = 0.5) -> np.ndarray:
        """
        Simula elevação de sobrancelhas
        """
        # Índices das sobrancelhas
        left_brow_indices = [336, 296, 334, 293, 276, 283, 282, 295, 285]
        right_brow_indices = [70, 63, 105, 66, 107, 55, 65, 52, 53]
        
        left_brow_points = [landmarks[i] for i in left_brow_indices if i < len(landmarks)]
        right_brow_points = [landmarks[i] for i in right_brow_indices if i < len(landmarks)]
        
        if not left_brow_points or not right_brow_points:
            return image
        
        # Criar máscara para as sobrancelhas
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        
        left_contour = np.array(left_brow_points, dtype=np.int32)
        right_contour = np.array(right_brow_points, dtype=np.int32)
        
        cv2.fillPoly(mask, [left_contour, right_contour], 255)
        
        # Expandir a máscara para incluir a área acima das sobrancelhas
        h, w = mask.shape[:2]
        for x in range(w):
            for y in range(h):
                if mask[y, x] > 0:
                    # Marcar pixels acima da sobrancelha
                    for offset in range(1, int(20 * intensity)):
                        if y - offset >= 0:
                            mask[y - offset, x] = 255
        
        # Aplicar transformação de elevação
        result = image.copy()
        shift_amount = int(5 * intensity)
        
        for y in range(shift_amount, h):
            for x in range(w):
                if mask[y, x] > 0:
                    result[y - shift_amount, x] = image[y, x]
        
        return result
    
    def simulate_skin_rejuvenation(self, image: np.ndarray, intensity: float = 0.5) -> np.ndarray:
        """
        Simula rejuvenescimento da pele
        """
        # Detectar pele
        skin_mask = self._create_skin_mask(image)
        
        # Aplicar suavização e melhoria de textura
        blurred = cv2.GaussianBlur(image, (15, 15), 0)
        
        # Ajustar brilho e contraste
        alpha = 1.0 + (0.1 * intensity)  # Contraste
        beta = 3 * intensity  # Brilho
        
        brightened = cv2.convertScaleAbs(blurred, alpha=alpha, beta=beta)
        
        # Aplicar apenas na região da pele
        result = image.copy()
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                if skin_mask[y, x] > 0:
                    # Misturar com a imagem original baseado na intensidade
                    result[y, x] = cv2.addWeighted(image[y, x], 1 - intensity, 
                                                brightened[y, x], intensity, 0)
        
        return result
    
    def _create_skin_mask(self, image: np.ndarray) -> np.ndarray:
        """
        Cria máscara para detecção de pele
        """
        # Converter para YCrCb
        ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        
        # Definir limites para cor da pele
        lower_skin = np.array([0, 135, 85], dtype=np.uint8)
        upper_skin = np.array([255, 180, 135], dtype=np.uint8)
        
        # Criar máscara
        mask = cv2.inRange(ycrcb, lower_skin, upper_skin)
        
        # Aplicar operações morfológicas para limpar a máscara
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        # Aplicar filtro gaussiano
        mask = cv2.GaussianBlur(mask, (3, 3), 0)
        
        return mask