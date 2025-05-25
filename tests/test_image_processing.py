import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from utils.image_processing import ImageProcessor
import numpy as np

def test_image_processor_initialization():
    processor = ImageProcessor()
    assert processor is not None

def test_preprocess_image_returns_array():
    processor = ImageProcessor()
    dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
    result = processor.preprocess_image(dummy_image)
    assert isinstance(result, np.ndarray)
    assert result.shape[0] > 0 and result.shape[1] > 0