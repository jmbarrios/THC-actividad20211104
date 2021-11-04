import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ('019-8cb66519-47f6-4f29-9648-2d1f76301c8a', 0.19),
    ('000-06cd4b23-ad63-460d-b4cd-4211f8b5c564', 0),
    ('100-556bab5c-ea17-42e0-b0a3-d21fcabb7ad4', 1),
    ('067-8cb66519-47f6-4f29-9648-2d1f76301c8a', 0.67)
])
def test_obten_probabilidad(test_input, expected):
    assert homework.obten_probabilidad(test_input) == expected