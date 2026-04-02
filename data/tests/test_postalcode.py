import pytest

import data.postalcode as pc

TEST_CODE = '99999'


def test_abc_base():
    with pytest.raises(TypeError):
        pc.PostalCode(TEST_CODE)


def test_construct_us_code():
    us_code = pc.USPostalCode(TEST_CODE)
    assert isinstance(us_code, pc.USPostalCode)


def test_construct_us_code_bad_type():
    with pytest.raises(TypeError):
        pc.USPostalCode(42)


def test_construct_us_code_bad_length():
    with pytest.raises(ValueError):
        pc.USPostalCode('kjshfjkshdjfkhdjkfhdjkhfjksdhfjk')


def test_construct_us_code_bad_chars():
    with pytest.raises(ValueError):
        pc.USPostalCode('k' * pc.US_POSTCODE_LEN)
