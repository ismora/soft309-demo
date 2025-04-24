# Definir casos de prueba usando pytest
import pytest
from src.math_ops import add, subtract, multiply, divide

class TestMathOperations:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
    
    def test_subtract(self):
        assert subtract(5, 2) == 3
        assert subtract(10, 10) == 0
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
    
    def test_divide(self):
        assert divide(10, 2) == 5
        with pytest.raises(ValueError):
            divide(5, 0)
    
    def test_flaky_example(self):
        # Test deliberadamente inestable para demostración
        import random
        assert random.choice([True, False])