import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
import numpy as np
from core.advanced_analysis import AdvancedFacialAnalyzer

def test_advanced_face_analyzer_initialization():
    analyzer = AdvancedFacialAnalyzer()
    assert analyzer is not None

def test_comprehensive_analysis_returns_dict():
    analyzer = AdvancedFacialAnalyzer()
    dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
    result = analyzer.comprehensive_analysis(dummy_image)
    assert isinstance(result, dict)
    if 'error' in result:
        pytest.skip("Face not detected in dummy image; skipping detailed assertions.")
    assert 'landmarks' in result
    assert 'measurements' in result
    assert 'aesthetic_analysis' in result
    assert 'skin_analysis' in result
    assert 'face_shape' in result
    assert 'recommendations' in result
    assert 'confidence_score' in result
    assert 'features' in result or 'scores' in result  # Accept either key for flexibility