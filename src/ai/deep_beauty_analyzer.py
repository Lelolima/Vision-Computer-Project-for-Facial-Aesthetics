import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import cv2
from typing import Dict, List, Tuple, Optional
from facenet_pytorch import MTCNN, InceptionResnetV1
from insightface.app import FaceAnalysis

class DeepBeautyAnalyzer:
    """
    Analisador de beleza facial usando modelos de deep learning avançados
    """
    
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Inicializar detector facial InsightFace
        self.face_analyzer = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
        self.face_analyzer.prepare(ctx_id=0, det_size=(640, 640))
        
        # Inicializar modelo FaceNet para embeddings faciais
        self.facenet = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)
        
        # Inicializar detector MTCNN para landmarks precisos
        self.mtcnn = MTCNN(keep_all=True, device=self.device)
        
        # Carregar modelo de análise estética (simulado)
        self.beauty_model = self._create_beauty_model()
        
    def _create_beauty_model(self):
        """
        Cria modelo de análise estética baseado em CNN
        """
        class BeautyNet(nn.Module):
            def __init__(self):
                super(BeautyNet, self).__init__()
                # Camadas convolucionais
                self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
                self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
                self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
                self.conv4 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
                
                # Pooling
                self.pool = nn.MaxPool2d(2, 2)
                
                # Camadas fully connected
                self.fc1 = nn.Linear(256 * 14 * 14, 512)
                self.fc2 = nn.Linear(512, 256)
                self.fc3 = nn.Linear(256, 15)  # 15 atributos estéticos
                
                # Dropout para regularização
                self.dropout = nn.Dropout(0.5)
            
            def forward(self, x):
                # Camadas convolucionais com ReLU e pooling
                x = self.pool(F.relu(self.conv1(x)))
                x = self.pool(F.relu(self.conv2(x)))
                x = self.pool(F.relu(self.conv3(x)))
                x = self.pool(F.relu(self.conv4(x)))
                
                # Reshape para camadas fully connected
                x = x.view(-1, 256 * 14 * 14)
                
                # Camadas fully connected com dropout
                x = F.relu(self.fc1(x))
                x = self.dropout(x)
                x = F.relu(self.fc2(x))
                x = self.dropout(x)
                
                # Camada de saída
                x = self.fc3(x)
                return x
        
        model = BeautyNet().to(self.device)
        return model
    
    def analyze_face(self, image: np.ndarray) -> Dict:
        """
        Analisa face usando modelos de deep learning
        """
        # Converter BGR para RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Detectar faces com InsightFace
        faces = self.face_analyzer.get(rgb_image)
        
        if not faces:
            return {'error': 'Nenhuma face detectada'}
        
        # Obter a face principal
        face = faces[0]
        
        # Extrair região facial
        bbox = face.bbox.astype(int)
        x1, y1, x2, y2 = bbox
        face_img = rgb_image[y1:y2, x1:x2]
        
        # Redimensionar para entrada do modelo
        face_resized = cv2.resize(face_img, (224, 224))
        
        # Converter para tensor
        face_tensor = torch.from_numpy(face_resized).permute(2, 0, 1).float().unsqueeze(0).to(self.device)
        face_tensor = face_tensor / 255.0
        
        # Extrair embedding facial com FaceNet
        with torch.no_grad():
            embedding = self.facenet(face_tensor).cpu().numpy()[0]
        
        # Analisar atributos estéticos com modelo personalizado
        with torch.no_grad():
            beauty_scores = self.beauty_model(face_tensor).cpu().numpy()[0]
        
        # Normalizar scores para 0-100
        normalized_scores = (beauty_scores - beauty_scores.min()) / (beauty_scores.max() - beauty_scores.min()) * 100
        
        # Mapear para atributos estéticos
        beauty_attributes = {
            'simetria_facial': normalized_scores[0],
            'proporcao_aurea': normalized_scores[1],
            'harmonia_nasal': normalized_scores[2],
            'definicao_labial': normalized_scores[3],
            'estrutura_ossea': normalized_scores[4],
            'qualidade_pele': normalized_scores[5],
            'expressividade_olhos': normalized_scores[6],
            'contorno_facial': normalized_scores[7],
            'juventude_aparente': normalized_scores[8],
            'atratividade_geral': normalized_scores[9],
            'textura_pele': normalized_scores[10],
            'uniformidade_tom': normalized_scores[11],
            'definicao_mandibula': normalized_scores[12],
            'harmonia_sobrancelhas': normalized_scores[13],
            'equilibrio_proporcoes': normalized_scores[14]
        }
        
        # Extrair atributos faciais do InsightFace
        gender = 'Feminino' if face.gender == 0 else 'Masculino'
        age = face.age
        
        # Extrair landmarks faciais
        landmarks = face.landmark_3d_68 if hasattr(face, 'landmark_3d_68') else face.landmark_2d_106
        landmarks = landmarks.astype(int).tolist()
        
        return {
            'beauty_attributes': beauty_attributes,
            'embedding': embedding.tolist(),
            'gender': gender,
            'age': age,
            'landmarks': landmarks,
            'bbox': bbox.tolist()
        }
    
    def compare_faces(self, image1: np.ndarray, image2: np.ndarray) -> Dict:
        """
        Compara duas faces para análise antes/depois
        """
        # Analisar ambas as faces
        analysis1 = self.analyze_face(image1)
        analysis2 = self.analyze_face(image2)
        
        if 'error' in analysis1 or 'error' in analysis2:
            return {'error': 'Não foi possível analisar ambas as faces'}
        
        # Calcular similaridade de embeddings
        embedding1 = np.array(analysis1['embedding'])
        embedding2 = np.array(analysis2['embedding'])
        
        similarity = np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
        
        # Calcular diferenças nos atributos estéticos
        attr1 = analysis1['beauty_attributes']
        attr2 = analysis2['beauty_attributes']
        
        differences = {}
        for key in attr1.keys():
            differences[key] = attr2[key] - attr1[key]
        
        # Calcular melhoria geral
        overall_improvement = np.mean(list(differences.values()))
        
        return {
            'similarity': similarity * 100,  # Porcentagem de similaridade
            'differences': differences,
            'overall_improvement': overall_improvement,
            'is_same_person': similarity > 0.75  # Threshold para mesma pessoa
        }
    
    def generate_aging_simulation(self, image: np.ndarray, years: int = 10) -> np.ndarray:
        """
        Simula envelhecimento facial
        """
        # Implementação simplificada - em produção usaria GANs específicas
        # Detectar face
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = self.face_analyzer.get(rgb_image)
        
        if not faces:
            return image
        
        # Obter a face principal
        face = faces[0]
        bbox = face.bbox.astype(int)
        x1, y1, x2, y2 = bbox
        
        # Extrair região facial
        face_img = image[y1:y2, x1:x2]
        
        # Aplicar efeitos de envelhecimento
        aged_face = face_img.copy()
        
        # Fator de envelhecimento
        aging_factor = min(1.0, years / 50.0)
        
        # 1. Reduzir saturação
        hsv = cv2.cvtColor(aged_face, cv2.COLOR_BGR2HSV)
        hsv[:,:,1] = hsv[:,:,1] * (1 - aging_factor * 0.3)  # Reduzir saturação
        aged_face = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        
        # 2. Adicionar rugas (usando detecção de bordas)
        gray = cv2.cvtColor(aged_face, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        # Misturar com imagem original
        aged_face = cv2.addWeighted(aged_face, 1-aging_factor*0.4, edges_colored, aging_factor*0.4, 0)
        
        # 3. Reduzir elasticidade (simular flacidez)
        # Aplicar leve distorção para baixo
        rows, cols = aged_face.shape[:2]
        map_y, map_x = np.indices((rows, cols), dtype=np.float32)
        
        # Aplicar distorção vertical
        center_y = rows // 2
        map_y = map_y + (map_y - center_y) * aging_factor * 0.05
        
        # Aplicar mapeamento
        aged_face = cv2.remap(aged_face, map_x, map_y, cv2.INTER_LINEAR)
        
        # Inserir face envelhecida de volta na imagem original
        result = image.copy()
        result[y1:y2, x1:x2] = aged_face
        
        return result