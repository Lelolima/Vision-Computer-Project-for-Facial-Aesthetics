import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
import json
from typing import Dict, List
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class AdvancedReportGenerator:
    """
    Gerador de relatórios avançados para análise estética
    """
    
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Configurar estilo dos gráficos
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    
    def generate_comprehensive_report(self, analysis_data: Dict, 
                                    patient_info: Dict = None) -> str:
        """
        Gera relatório completo da análise
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_name = f"relatorio_estetico_{timestamp}"
        
        # Criar estrutura do relatório
        report_data = {
            'timestamp': timestamp,
            'patient_info': patient_info or {},
            'analysis_results': analysis_data,
            'visualizations': []
        }
        
        # Gerar visualizações
        self._create_beauty_radar_chart(analysis_data, report_name)
        self._create_measurements_chart(analysis_data, report_name)
        self._create_recommendations_chart(analysis_data, report_name)
        
        # Gerar relatório HTML
        html_report = self._generate_html_report(report_data, report_name)
        
        # Salvar dados JSON
        json_path = self.output_dir / f"{report_name}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        return str(html_report)
    
    def _create_beauty_radar_chart(self, data: Dict, report_name: str):
        """
        Cria gráfico radar das características de beleza
        """
        if 'beauty_scores' not in data:
            return
        
        beauty_scores = data['beauty_scores']
        
        # Preparar dados
        categories = list(beauty_scores.keys())
        values = list(beauty_scores.values())
        
        # Criar gráfico radar com Plotly
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Scores Atuais',
            line_color='rgb(0, 123, 255)'
        ))
        
        # Adicionar linha de referência (score ideal)
        ideal_scores = [85] * len(categories)
        fig.add_trace(go.Scatterpolar(
            r=ideal_scores,
            theta=categories,
            fill='toself',
            name='Score Ideal',
            line_color='rgb(255, 193, 7)',
            opacity=0.3
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=True,
            title="Análise de Características Estéticas",
            font=dict(size=12)
        )
        
        # Salvar
        chart_path = self.output_dir / f"{report_name}_radar.html"
        fig.write_html(str(chart_path))
    
    def _create_measurements_chart(self, data: Dict, report_name: str):
        """
        Cria gráfico de medidas faciais
        """
        if 'measurements' not in data:
            return
        
        measurements = data['measurements']
        
        # Criar gráfico de barras
        fig = px.bar(
            x=list(measurements.keys()),
            y=list(measurements.values()),
            title="Medidas Faciais (pixels)",
            labels={'x': 'Medidas', 'y': 'Valor (px)'},
            color=list(measurements.values()),
            color_continuous_scale='viridis'
        )
        
        fig.update_layout(
            xaxis_tickangle=-45,
            height=500
        )
        
        # Salvar
        chart_path = self.output_dir / f"{report_name}_measurements.html"
        fig.write_html(str(chart_path))
    
    def _create_recommendations_chart(self, data: Dict, report_name: str):
        """
        Cria gráfico de recomendações
        """
        if 'suggestions' not in data:
            return
        
        suggestions = data['suggestions']
        
        if not suggestions:
            return
        
        # Preparar dados
        procedures = [s['procedimento'] for s in suggestions]
        priorities = [s['prioridade'] for s in suggestions]
        improvements = [s['score_melhoria'] for s in suggestions]
        
        # Mapear prioridades para cores
        color_map = {'Alta': 'red', 'Média': 'orange', 'Baixa': 'green'}
        colors = [color_map.get(p, 'blue') for p in priorities]
        
        # Criar gráfico
        fig = go.Figure(data=[
            go.Bar(
                x=procedures,
                y=improvements,
                marker_color=colors,
                text=priorities,
                textposition='auto'
            )
        ])
        
        fig.update_layout(
            title="Recomendações de Procedimentos",
            xaxis_title="Procedimentos",
            yaxis_title="Melhoria Esperada (%)",
            xaxis_tickangle=-45
        )
        
        # Salvar
        chart_path = self.output_dir / f"{report_name}_recommendations.html"
        fig.write_html(str(chart_path))
    
    def _generate_html_report(self, report_data: Dict, report_name: str) -> Path:
        """
        Gera relatório HTML completo
        """
        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relatório de Análise Estética</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ text-align: center; margin-bottom: 30px; }}
                .section {{ margin-bottom: 25px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
                .score {{ font-weight: bold; color: #007bff; }}
                .recommendation {{ background-color: #f8f9fa; padding: 10px; margin: 5px 0; border-radius: 3px; }}
                .chart-container {{ text-align: center; margin: 20px 0; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Relatório de Análise Facial Estética</h1>
                <p>Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            </div>
            
            <div class="section">
                <h2>Resumo da Análise</h2>
                <p>Este relatório apresenta uma análise completa das características faciais utilizando tecnologia de visão computacional e inteligência artificial.</p>
            </div>
            
            <div class="section">
                <h2>Scores de Beleza</h2>
                {self._format_beauty_scores(report_data.get('analysis_results', {}).get('beauty_scores', {}))}
            </div>
            
            <div class="section">
                <h2>Medidas Faciais</h2>
                {self._format_measurements(report_data.get('analysis_results', {}).get('measurements', {}))}
            </div>
            
            <div class="section">
                <h2>Recomendações</h2>
                {self._format_recommendations(report_data.get('analysis_results', {}).get('suggestions', []))}
            </div>
            
            <div class="chart-container">
                <iframe src="{report_name}_radar.html" width="100%" height="600"></iframe>
            </div>
            
            <div class="chart-container">
                <iframe src="{report_name}_measurements.html" width="100%" height="600"></iframe>
            </div>
            
            <div class="chart-container">
                <iframe src="{report_name}_recommendations.html" width="100%" height="600"></iframe>
            </div>
        </body>
        </html>
        """
        
        # Salvar HTML
        html_path = self.output_dir / f"{report_name}.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return html_path
    
    def _format_beauty_scores(self, scores: Dict) -> str:
        if not scores:
            return "<p>Nenhum score disponível.</p>"
        
        html = "<ul>"
        for aspect, score in scores.items():
            formatted_aspect = aspect.replace('_', ' ').title()
            html += f'<li>{formatted_aspect}: <span class="score">{score:.1f}/100</span></li>'
        html += "</ul>"
        return html
    
    def _format_measurements(self, measurements: Dict) -> str:
        if not measurements:
            return "<p>Nenhuma medida disponível.</p>"
        
        html = "<ul>"
        for measure, value in measurements.items():
            formatted_measure = measure.replace('_', ' ').title()
            html += f'<li>{formatted_measure}: {value:.1f} pixels</li>'
        html += "</ul>"
        return html
    
    def _format_recommendations(self, suggestions: List) -> str:
        if not suggestions:
            return "<p>Nenhuma recomendação específica. Perfil dentro dos padrões ideais.</p>"
        
        html = ""
        for suggestion in suggestions:
            html += f'''
            <div class="recommendation">
                <h4>{suggestion['procedimento']}</h4>
                <p><strong>Área:</strong> {suggestion['area']}</p>
                <p><strong>Prioridade:</strong> {suggestion['prioridade']}</p>
                <p><strong>Descrição:</strong> {suggestion['descricao']}</p>
                <p><strong>Melhoria Esperada:</strong> {suggestion['score_melhoria']}%</p>
            </div>
            '''
        return html
    
    def generate_report(self, analysis_data: dict, patient_info: dict = None) -> str:
        """
        Wrapper for generate_comprehensive_report to maintain compatibility with tests.
        """
        return self.generate_comprehensive_report(analysis_data, patient_info)