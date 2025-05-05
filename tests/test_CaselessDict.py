import pytest
from src.handy import CaselessDict

class TestCaselessDict:
    def test_initialization(self):
        cd1 = CaselessDict()
        assert len(cd1) == 0

        cd2 = CaselessDict({"Key": 1, "key": 2})
        assert len(cd2) == 1
        assert cd2["key"] == 2
        assert cd2["KEY"] == 2

        cd3 = CaselessDict(Key="value1", key="value2")
        assert len(cd3) == 1
        assert cd3["key"] == "value2"
        assert cd3["KEY"] == "value2"

        cd4 = CaselessDict([("kEy1", "val1"), ("key1", "val2")])
        assert len(cd4) == 1
        assert cd4["key1"] == "val2"
        assert cd4["KEY1"] == "val2"

    def test_setitem_getitem(self):
        cd = CaselessDict()
        cd["Apple"] = 1
        assert cd["apple"] == 1
        assert cd["APPLE"] == 1

        cd["Banana"] = 2
        assert cd["banana"] == 2

        cd["Orange"] = 3
        assert cd["orange"] == 3

        cd[1] = "int_key"
        assert cd[1] == "int_key"

    def test_contains(self):
        cd = CaselessDict({"Apple": 1})
        assert "apple" in cd
        assert "APPLE" in cd
        assert "Banana" not in cd
        assert 1 not in cd  # Non-string key

        cd[1] = "int_key"
        assert 1 in cd

    def test_get(self):
        cd = CaselessDict({"Apple": 1})
        assert cd.get("apple") == 1
        assert cd.get("APPLE") == 1
        assert cd.get("Banana") is None
        assert cd.get("Banana", 0) == 0

        cd[1] = "int_key"
        assert cd.get(1) == "int_key"
        assert cd.get(2) is None
        assert cd.get(2, "not found") == "not found"

    def test_repr(self):
        cd1 = CaselessDict({"Key": 1})
        assert repr(cd1) == "CaselessDict({CaselessString('Key'): 1})"

        cd2 = CaselessDict({"key1": "value1", "KEY2": "value2"})
        expected_repr_1 = "CaselessDict({CaselessString('key1'): 'value1', CaselessString('KEY2'): 'value2'})"
        expected_repr_2 = "CaselessDict({CaselessString('KEY2'): 'value2', CaselessString('key1'): 'value1'})"
        assert repr(cd2) == expected_repr_1 or repr(cd2) == expected_repr_2

        cd3 = CaselessDict({1: "int", "str": 2})
        expected_repr_3 = "CaselessDict({1: 'int', CaselessString('str'): 2})"
        expected_repr_4 = "CaselessDict({CaselessString('str'): 2, 1: 'int'})"
        assert repr(cd3) == expected_repr_3 or repr(cd3) == expected_repr_4

    def test_len(self):
        cd = CaselessDict()
        assert len(cd) == 0
        cd["Apple"] = 1
        assert len(cd) == 1
        cd["apple"] = 2  # Overwrites existing key
        assert len(cd) == 1
        cd["Banana"] = 3
        assert len(cd) == 2
        cd[1] = "int_key"
        assert len(cd) == 3
