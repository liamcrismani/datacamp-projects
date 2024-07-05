from validation_functions import validate_email, validate_name
import pytest


@pytest.fixture
def prepare_data():
    top_level_domains = [".org", ".net", ".edu", ".ac", ".gov", ".com", ".io"]
    return top_level_domains


def test_validate_name():
    assert validate_name("Bob") is True, "3 character string not seen as valid"
    assert validate_name(123) is False, "Integers seen as valid"
    assert validate_name("ab") is False, "2 character string seen as valid"


def test_validate_email(prepare_data):
    assert validate_email("test@yahoo.com") is True, \
        "Email test@yahoo.com should pass, but has failed."
    assert validate_email("test@yahoo.co.uk") is False, \
        "Email test@yahoo.co.uk has passed, but should fail."
