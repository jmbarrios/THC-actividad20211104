from itertools import product
import pytest
import homework


@pytest.mark.parametrize('num1, num2, expected', [
    (1, 2, 3),
    (5, -6, -1),
    (3.4, 1, 4.4),
    (3.4, .6, 4),
    (2, 2+3j, 4+3j),
    (2.1+.4j, 3+1j, 5.1+1.4j)
])
def test_suma_numeros(num1, num2, expected):
    assert homework.suma(num1, num2) == expected


@pytest.mark.parametrize('input1, input2', 
    product([1], [[], 'a', {'b': 2}])
)
def test_suma_error(input1, input2):
    with pytest.raises(ValueError):
        homework.suma(input1, input2)


@pytest.mark.parametrize('input1, input2', 
    product([[], 'a', {'b': 2}], [1])
)
def test_suma_error(input1, input2):
    with pytest.raises(ValueError):
        homework.suma(input1, input2)