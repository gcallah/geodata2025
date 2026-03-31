import pytest

import data.postalcode as pc

TEST_CODE = '99999'


def test_abc_base():
    with pytest.raises(TypeError):
        pc.PostalCode(TEST_CODE)


def test_construct_us_code():
    us_code = pc.USPostalCode(TEST_CODE)
    assert isinstance(us_code, pc.USPostalCode)
