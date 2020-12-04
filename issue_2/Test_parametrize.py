from Morse_code import decode
import pytest


@pytest.mark.parametrize(
    'test_input, exp',
    [('.--- ..- .-.. .. .-', 'JULIA'), ('... --- ...', 'SOS'), ('', '')],
)
def test_string(test_input, exp):
    assert decode(test_input) == exp


@pytest.mark.parametrize('test_input,exp', [('Julia', KeyError)])
def test_exception(test_input, exp):
    with pytest.raises(exp, match=test_input):
        decode(test_input)
