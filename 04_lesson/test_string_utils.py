import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123abc", "123abc"),
    ("", ""),
    ("   sky", "   sky"),
])
def test_capitilize(input_str, expected):
    assert utils.capitilize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   sky pro   ", "sky pro   "),
    ("", ""),
    (" ", ""),
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3:4", ":", ["1", "2", "3", "4"]),
    ("", ",", []),
    ("a,b", "", ["a,b"]),
    ("a b c", " ", ["a", "b", "c"]),
])
def test_to_list(input_str, delimiter, expected):
    assert utils.to_list(input_str, delimiter) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False),
    ("SkyPro", "", True),
    ("123", "2", True),
    ("Hello", "h", False),
])
def test_contains(input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "yP", "Skro"),
    ("aaaaa", "a", ""),
    ("", "a", ""),
    ("SkyPro", "x", "SkyPro"),
    ("Hello World", " ", "HelloWorld"),
])
def test_delete_symbol(input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected
