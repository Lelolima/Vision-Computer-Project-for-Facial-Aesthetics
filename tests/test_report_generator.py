import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from reports.report_generator import AdvancedReportGenerator

def test_report_generator_initialization():
    generator = AdvancedReportGenerator()
    assert generator is not None

def test_generate_report_returns_str():
    generator = AdvancedReportGenerator()
    dummy_result = {"dummy": "data"}
    report = generator.generate_report(dummy_result)
    assert isinstance(report, str)
    assert len(report) > 0