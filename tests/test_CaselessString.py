import pytest
from src.handy import CaselessString

class TestCaselessString:
    def test_initialization(self):
        cs1 = CaselessString("Hello")
        assert cs1 == "Hello"
        assert str(cs1) == "Hello"

        cs2 = CaselessString("hello")
        assert cs2 == "hello"
        assert str(cs2) == "hello"

        cs3 = CaselessString(123)
        assert cs3 == "123"
        assert str(cs3) == "123"

    def test_case_insensitive_equality_with_caseless_string(self):
        cs1 = CaselessString("Apple")
        cs2 = CaselessString("apple")
        assert cs1 == cs2
        assert not (cs1 != cs2)

        cs3 = CaselessString("Banana")
        assert cs1 != cs3
        assert not (cs1 == cs3)

    def test_case_insensitive_equality_with_regular_string(self):
        cs = CaselessString("World")
        s1 = "world"
        s2 = "WORLD"
        s3 = "different"

        assert cs == s1
        assert cs == s2
        assert s1 == cs
        assert s2 == cs
        assert not (cs == s3)
        assert cs != s3

    def test_case_insensitive_str_equality(self):
        cs = CaselessString("Python")
        s1 = "python"
        s2 = "Python"
        s3 = "different"

        assert cs == s1
        assert cs == s2
        assert s1 == cs
        assert s2 == cs
        assert not (cs == s3)
        assert cs != s3

    def test_repr(self):
        cs1 = CaselessString("MixedCase")
        assert repr(cs1) == "CaselessString('MixedCase')"

        cs2 = CaselessString("String with 'quotes'")
        assert repr(cs2) == "CaselessString(\"String with 'quotes'\")", "Ensure single quotes are escaped"

        cs3 = CaselessString('"Double quotes"')
        actual_repr_3 = repr(cs3)
        print(f"repr(cs3) is: {actual_repr_3}")
        assert actual_repr_3 == "CaselessString('\"Double quotes\"')"

    def test_str(self):
        cs = CaselessString("Original Case")
        assert str(cs) == "Original Case"
