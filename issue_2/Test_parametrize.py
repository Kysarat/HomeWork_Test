from Morse_code import decode
import pytest


@pytest.mark.parametrize('exp,test_input', [
    ('JULIA', '.--- ..- .-.. .. .-'),
    ('SOS', '... --- ...'),
    ('', '')
])
def test_string(test_input, exp):
    assert decode(test_input) == exp


@pytest.mark.parametrize('exp,test_input', [
    (pytest.raises(KeyError), 'Julia')
])
def test_exception(test_input, exp):
    with exp:
        assert decode(test_input) == exp
