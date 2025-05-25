import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
import numpy as np
from core.simulation_engine import AdvancedSimulationEngine

def test_simulation_engine_initialization():
    engine = AdvancedSimulationEngine()
    assert engine is not None

def test_simulate_rhinoplasty_returns_image():
    engine = AdvancedSimulationEngine()
    dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
    dummy_landmarks = [(10, 10)] * 200  # Sufficient length for indices
    result = engine.simulate_rhinoplasty(dummy_image, dummy_landmarks)
    assert result is not None

def test_simulate_lip_enhancement_returns_image():
    engine = AdvancedSimulationEngine()
    dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
    dummy_landmarks = [(10, 10)] * 200
    result = engine.simulate_lip_enhancement(dummy_image, dummy_landmarks)
    assert result is not None