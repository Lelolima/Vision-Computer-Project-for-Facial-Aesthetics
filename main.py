#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Análise de Perfil Facial para Clínicas de Estética
Autor: Sistema de Visão Computacional
Data: 2024
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório src ao path
sys.path.append(str(Path(__file__).parent / 'src'))

from ui.main_interface import AestheticAnalysisApp

def main():
    """
    Função principal do aplicativo
    """
    try:
        app = AestheticAnalysisApp()
        app.run()
    except Exception as e:
        print(f"Erro ao inicializar o aplicativo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()