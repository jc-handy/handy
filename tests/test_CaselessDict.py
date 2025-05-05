import pytest
from src.handy import CaselessDict

d=CaselessDict(
    alpha=1,
    Bravo=2,
    charlie=3,
    Delta=4
)

class TestCaselessDict:
    def test_initialization(self):
        cd = CaselessDict()
        assert len(cd) == 0
        assert isinstance(cd,dict)
        assert isinstance(cd,CaselessDict)

        cd = CaselessDict(Key="value1", key="value2")
        assert len(cd) == 1
        assert cd["key"] == "value2"
        assert cd["KEY"] == "value2"

        cd = CaselessDict({"Key": 1, "key": 2})
        assert len(cd) == 1
        assert cd["key"] == 2
        assert cd["KEY"] == 2

        cd = CaselessDict([("kEy1", "val1"), ("key1", "val2")])
        assert len(cd) == 1
        assert cd["key1"] == "val2"
        assert cd["KEY1"] == "val2"

    def test_setitem_getitem(self):
        d['gamma'] = 5
        assert d['gamma'] == 5
        assert d['GaMmA'] == 5

        d[10] = "int key"
        assert d[10] == "int key"

    def test_contains(self):
        assert "alpha" in d
        assert "AlPhA" in d
        assert "epsilon" not in d

        d[20] = '20'
        assert 20 in d
        assert 99 not in d


    def test_get(self):
        assert d.get('alpha') == 1
        assert d.get('AlPhA') == 1
        assert d.get('missing') is None
        assert d.get('missing', -1) == -1

        d[30] = "30"
        assert d.get(30) == "30"
        assert d.get(99) is None
        assert d.get(99, "not found") == "not found"

    def test_repr(self):
        x=CaselessDict()
        assert repr(x)=="CaselessDict({})"

        x['alpha']=1
        assert repr(x)=="CaselessDict({CaselessString('alpha'): 1})"

        x.update(Bravo=2,charlie=3)
        assert repr(x)=="CaselessDict({CaselessString('alpha'): 1, CaselessString('Bravo'): 2, CaselessString('charlie'): 3})"

        x[10]='ten'
        assert repr(x)=="CaselessDict({CaselessString('alpha'): 1, CaselessString('Bravo'): 2, CaselessString('charlie'): 3, 10: 'ten'})"


    def test_len(self):
        x = CaselessDict()
        assert len(x) == 0
        x["Apple"] = 1
        assert len(x) == 1
        x["apple"] = 2  # Overwrites existing key
        assert len(x) == 1
        x["Banana"] = 3
        assert len(x) == 2
        x[1] = "int_key"
        assert len(x) == 3
