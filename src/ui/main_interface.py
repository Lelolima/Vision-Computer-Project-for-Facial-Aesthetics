import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np
from pathlib import Path
import sys

# Adicionar path para imports
sys.path.append(str(Path(__file__).parent.parent))

from core.profile_processor import ProfileProcessor
from utils.image_processing import ImageProcessor

class AestheticAnalysisApp:
    """
    Interface principal do aplicativo de análise estética
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Análise Facial - Clínica Estética")
        self.root.geometry("1200x800")
        
        # Inicializar processadores
        self.profile_processor = ProfileProcessor()
        self.image_processor = ImageProcessor()
        
        # Variáveis
        self.current_image = None
        self.original_image = None
        self.analysis_results = None
        
        # Configurar interface
        self.setup_ui()
    
    def setup_ui(self):
        """
        Configura a interface do usuário
        """
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="Sistema de Análise Facial para Procedimentos Estéticos",
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Frame de controles
        controls_frame = ttk.LabelFrame(main_frame, text="Controles", padding="10")
        controls_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Botões de controle
        ttk.Button(
            controls_frame, 
            text="Carregar Imagem", 
            command=self.load_image
        ).grid(row=0, column=0, pady=5, sticky=tk.W+tk.E)
        
        ttk.Button(
            controls_frame, 
            text="Analisar Perfil", 
            command=self.analyze_profile
        ).grid(row=1, column=0, pady=5, sticky=tk.W+tk.E)
        
        # Separador
        ttk.Separator(controls_frame, orient='horizontal').grid(
            row=2, column=0, sticky=(tk.W, tk.E), pady=10
        )
        
        # Simulações
        ttk.Label(controls_frame, text="Simulações:", font=('Arial', 12, 'bold')).grid(
            row=3, column=0, pady=(10, 5), sticky=tk.W
        )
        
        # Rinoplastia
        ttk.Label(controls_frame, text="Rinoplastia:").grid(row=4, column=0, sticky=tk.W)
        self.rhinoplasty_scale = ttk.Scale(
            controls_frame, from_=0, to=1, orient=tk.HORIZONTAL
        )
        self.rhinoplasty_scale.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=2)
        
        ttk.Button(
            controls_frame, 
            text="Simular Rinoplastia", 
            command=self.simulate_rhinoplasty
        ).grid(row=6, column=0, pady=5, sticky=tk.W+tk.E)
        
        # Preenchimento labial
        ttk.Label(controls_frame, text="Preenchimento Labial:").grid(row=7, column=0, sticky=tk.W)
        self.lip_scale = ttk.Scale(
            controls_frame, from_=0, to=1, orient=tk.HORIZONTAL
        )
        self.lip_scale.grid(row=8, column=0, sticky=(tk.W, tk.E), pady=2)
        
        ttk.Button(
            controls_frame, 
            text="Simular Preenchimento", 
            command=self.simulate_lip_enhancement
        ).grid(row=9, column=0, pady=5, sticky=tk.W+tk.E)
        
        # Botão reset
        ttk.Button(
            controls_frame, 
            text="Resetar Imagem", 
            command=self.reset_image
        ).grid(row=10, column=0, pady=20, sticky=tk.W+tk.E)
        
        # Frame de imagem
        image_frame = ttk.LabelFrame(main_frame, text="Visualização", padding="10")
        image_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Canvas para imagem
        self.image_canvas = tk.Canvas(image_frame, bg='white', width=500, height=400)
        self.image_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame de resultados
        results_frame = ttk.LabelFrame(main_frame, text="Análise e Resultados", padding="10")
        results_frame.grid(row=1, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0))
        
        # Text widget para resultados
        self.results_text = tk.Text(results_frame, width=40, height=25, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Configurar redimensionamento
        image_frame.columnconfigure(0, weight=1)
        image_frame.rowconfigure(0, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
    
    def load_image(self):
        """
        Carrega imagem do arquivo
        """
        file_path = filedialog.askopenfilename(
            title="Selecionar Imagem",
            filetypes=[
                ("Imagens", "*.jpg *.jpeg *.png *.bmp *.tiff"),
                ("Todos os arquivos", "*.*")
            ]
        )
        
        if file_path:
            try:
                # Carregar imagem
                self.original_image = cv2.imread(file_path)
                self.current_image = self.original_image.copy()
                
                # Redimensionar para exibição
                display_image = self.image_processor.resize_for_display(
                    self.current_image, max_width=500, max_height=400
                )
                
                # Converter para PIL e exibir
                self.display_image(display_image)
                
                # Limpar resultados anteriores
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(tk.END, "Imagem carregada com sucesso!\n")
                self.results_text.insert(tk.END, f"Arquivo: {Path(file_path).name}\n")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar imagem: {str(e)}")
    
    def display_image(self, image):
        """
        Exibe imagem no canvas
        """
        # Converter BGR para RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Converter para PIL
        pil_image = Image.fromarray(rgb_image)
        
        # Converter para PhotoImage
        self.photo = ImageTk.PhotoImage(pil_image)
        
        # Limpar canvas e exibir imagem
        self.image_canvas.delete("all")
        self.image_canvas.create_image(
            self.image_canvas.winfo_width()//2,
            self.image_canvas.winfo_height()//2,
            anchor=tk.CENTER,
            image=self.photo
        )
    
    def analyze_profile(self):
        """
        Analisa o perfil facial
        """
        if self.current_image is None:
            messagebox.showwarning("Aviso", "Por favor, carregue uma imagem primeiro.")
            return
        
        try:
            # Realizar análise
            self.analysis_results = self.profile_processor.analyze_profile(self.current_image)
            
            # Exibir resultados
            self.display_analysis_results()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na análise: {str(e)}")
    
    def display_analysis_results(self):
        """
        Exibe os resultados da análise
        """
        if not self.analysis_results:
            return
        
        self.results_text.delete(1.0, tk.END)
        
        if 'error' in self.analysis_results:
            self.results_text.insert(tk.END, f"Erro: {self.analysis_results['error']}\n")
            return
        
        # Título
        self.results_text.insert(tk.END, "=== ANÁLISE FACIAL ===\n\n")
        
        # Medidas
        if 'measurements' in self.analysis_results:
            self.results_text.insert(tk.END, "MEDIDAS FACIAIS:\n")
            measurements = self.analysis_results['measurements']
            
            for key, value in measurements.items():
                formatted_key = key.replace('_', ' ').title()
                self.results_text.insert(tk.END, f"• {formatted_key}: {value:.1f}px\n")
            
            self.results_text.insert(tk.END, "\n")
        
        # Score de simetria
        if 'symmetry_score' in self.analysis_results:
            score = self.analysis_results['symmetry_score']
            self.results_text.insert(tk.END, f"SIMETRIA FACIAL: {score:.1f}/100\n\n")
        
        # Recomendações
        if 'recommendations' in self.analysis_results:
            self.results_text.insert(tk.END, "RECOMENDAÇÕES:\n")
            recommendations = self.analysis_results['recommendations']
            
            if recommendations:
                for i, rec in enumerate(recommendations, 1):
                    self.results_text.insert(tk.END, f"{i}. {rec}\n")
            else:
                self.results_text.insert(tk.END, "Nenhuma recomendação específica. Perfil dentro dos padrões ideais.\n")

    def simulate_rhinoplasty(self):
        """
        Simula procedimento de rinoplastia na imagem atual
        """
        if self.current_image is None:
            messagebox.showwarning("Aviso", "Por favor, carregue uma imagem primeiro.")
            return
        intensity = self.rhinoplasty_scale.get()
        try:
            result = self.profile_processor.simulate_rhinoplasty(self.current_image, intensity=intensity)
            self.current_image = result
            self.display_image(result)
            self.results_text.insert(tk.END, "\nSimulação de rinoplastia aplicada.\n")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na simulação de rinoplastia: {str(e)}")

    def simulate_lip_enhancement(self):
        """
        Simula preenchimento labial na imagem atual
        """
        if self.current_image is None:
            messagebox.showwarning("Aviso", "Por favor, carregue uma imagem primeiro.")
            return
        intensity = self.lip_scale.get()
        try:
            result = self.profile_processor.simulate_lip_enhancement(self.current_image, volume_increase=intensity)
            self.current_image = result
            self.display_image(result)
            self.results_text.insert(tk.END, "\nSimulação de preenchimento labial aplicada.\n")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na simulação de preenchimento labial: {str(e)}")

    def reset_image(self):
        """
        Restaura a imagem original carregada
        """
        if self.original_image is not None:
            self.current_image = self.original_image.copy()
            self.display_image(self.current_image)
            self.results_text.insert(tk.END, "\nImagem restaurada ao original.\n")
        else:
            messagebox.showinfo("Info", "Nenhuma imagem original para restaurar.")