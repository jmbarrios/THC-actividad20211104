import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ('Juan', 'Hola Juan.'),
    ('Alexis', 'Hola Alexis.'),
    ('Paola', 'Hola Paola.')
])
def test_saludo_nombre(test_input, expected):
    assert homework.saludo(test_input) == expected


def test_saludo_no_nombre():
    assert homework.saludo() == 'Hola extraño.'