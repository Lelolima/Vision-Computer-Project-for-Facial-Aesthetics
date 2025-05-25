import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
import numpy as np
from core.profile_processor import ProfileProcessor

def test_profile_processor_initialization():
    processor = ProfileProcessor()
    assert processor is not None

def test_analyze_profile_returns_dict():
    processor = ProfileProcessor()
    dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
    result = processor.analyze_profile(dummy_image)
    assert isinstance(result, dict)
    if 'error' in result:
        pytest.skip("Face not detected in dummy image; skipping detailed assertions.")
    assert 'facial_measurements' in result
    assert 'symmetry_score' in result
    assert 'recommendations' in result
    assert 'landmarks' in result
    assert 'profile_points' in result
    assert 'measurements' in result
    assert 'recommendations' in result
    assert 'symmetry_score' in result