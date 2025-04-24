import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.operations import suma, resta

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2