import cv2
import numpy as np
from typing import Tuple, Optional
from scipy import ndimage

# Certifique-se de que todas as funções e métodos estejam corretamente implementados e documentados.
# Se houver funções não utilizadas ou imports desnecessários, remova-os para manter o código limpo.
from skimage import filters, morphology

class ImageProcessor:
    """
    Classe avançada para processamento de imagens
    """
    
    def __init__(self):
        pass
    
    def resize_for_display(self, image: np.ndarray, max_width: int = 500, max_height: int = 400) -> np.ndarray:
        """
        Redimensiona imagem mantendo proporção
        """
        h, w = image.shape[:2]
        
        # Calcular nova dimensão mantendo proporção
        scale = min(max_width/w, max_height/h)
        
        if scale < 1:
            new_w = int(w * scale)
            new_h = int(h * scale)
            return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
        
        return image
    
    def enhance_image_quality(self, image: np.ndarray) -> np.ndarray:
        """
        Melhora qualidade da imagem usando técnicas avançadas
        """
        # Redução de ruído
        denoised = cv2.bilateralFilter(image, 9, 75, 75)
        
        # Melhoria de contraste usando CLAHE
        lab = cv2.cvtColor(denoised, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        
        enhanced = cv2.merge([l, a, b])
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
        
        return enhanced
    
    def apply_skin_smoothing(self, image: np.ndarray, intensity: float = 0.3) -> np.ndarray:
        """
        Aplica suavização de pele avançada
        """
        # Criar máscara de pele
        skin_mask = self._create_skin_mask(image)
        
        # Aplicar filtro bilateral apenas na área da pele
        smoothed = cv2.bilateralFilter(image, 15, 80, 80)
        
        # Misturar com imagem original baseado na intensidade
        result = image.copy().astype(np.float32)
        smoothed = smoothed.astype(np.float32)
        
        for i in range(3):
            result[:,:,i] = np.where(skin_mask > 0, 
                                   result[:,:,i] * (1-intensity) + smoothed[:,:,i] * intensity,
                                   result[:,:,i])
        
        return result.astype(np.uint8)
    
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
    
    def apply_advanced_morphing(self, image: np.ndarray, landmarks: list, 
                              transformation_points: dict, intensity: float = 0.5) -> np.ndarray:
        """
        Aplica transformação morfológica avançada usando thin plate splines
        """
        from scipy.spatial.distance import cdist
        
        h, w = image.shape[:2]
        result = image.copy()
        
        # Implementar thin plate spline transformation
        # Esta é uma versão simplificada - em produção usaria bibliotecas especializadas
        
        for region, delta in transformation_points.items():
            if region in landmarks:
                center = landmarks[region]
                radius = 30
                
                # Criar máscara circular
                y, x = np.ogrid[:h, :w]
                mask = (x - center[0])**2 + (y - center[1])**2 <= radius**2
                
                # Aplicar transformação suave
                if mask.any():
                    coords = np.column_stack(np.where(mask))
                    for coord in coords:
                        distance = np.sqrt((coord[1] - center[0])**2 + (coord[0] - center[1])**2)
                        if distance <= radius:
                            weight = (1 - distance/radius) * intensity
                            new_x = int(coord[1] + delta[0] * weight)
                            new_y = int(coord[0] + delta[1] * weight)
                            
                            if 0 <= new_x < w and 0 <= new_y < h:
                                result[coord[0], coord[1]] = image[new_y, new_x]
        
        return result
    
    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocesses the image by converting to grayscale and normalizing pixel values.
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        norm = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
        return norm