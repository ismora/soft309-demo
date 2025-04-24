from faker import Faker
import pytest
from calculadora import multiplicar

fake = Faker()

@pytest.mark.parametrize("a, b, expected", [
    (fake.random_int(1, 10), fake.random_int(1, 10), None) for _ in range(5)
])
def test_multiplicar(a, b, expected):
    expected = a * b  # Resultado calculado dinámicamente
    assert multiplicar(a, b) == expected

# Ejecucón: pytest .\test_datos_parametrizados.py -v