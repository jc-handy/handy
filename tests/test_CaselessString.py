import pytest
from src.handy import CaselessString

alpha=CaselessString('alpha')
bravo=CaselessString('bravo')
charlie=CaselessString('charlie')

Alpha=CaselessString('Alpha')
Bravo=CaselessString('Bravo')
Charlie=CaselessString('Charlie')

class TestCaselessString:
    def test_initialization(self):
        assert isinstance(alpha,str)
        assert isinstance(alpha,CaselessString)
        assert alpha == 'alpha'

    def test_equality_with_CaselessString(self):
        assert alpha == alpha
        assert alpha == Alpha
        assert alpha != bravo
        assert not (alpha == bravo)

    def test_equality_with_str(self):
        assert alpha == 'alpha'
        assert alpha == 'Alpha'
        assert 'alpha' == alpha
        assert 'Alpha' == alpha
        assert alpha != 'bravo'
        assert not (alpha == 'bravo')

    def test_other_comparisons(self):
        assert alpha<Bravo<charlie
        assert charlie>Bravo>alpha
        assert alpha<'Bravo'<charlie
        assert charlie>'Bravo'>alpha

    def test_repr(self):
        repr(alpha) == CaselessString('alpha')
        repr(Bravo) == CaselessString('Bravo')
        repr(charlie) == CaselessString('charlie')

    def test_sorting(self):
        l=[Bravo,alpha,charlie]
        assert repr(l) == "[CaselessString('Bravo'), CaselessString('alpha'), CaselessString('charlie')]"
        l.sort()
        assert repr(l) == "[CaselessString('alpha'), CaselessString('Bravo'), CaselessString('charlie')]"
        l.sort(reverse=True)
        assert repr(l) == "[CaselessString('charlie'), CaselessString('Bravo'), CaselessString('alpha')]"

        l=['Bravo',alpha,charlie]
        assert repr(l) == "['Bravo', CaselessString('alpha'), CaselessString('charlie')]"
        l.sort()
        assert repr(l) == "[CaselessString('alpha'), 'Bravo', CaselessString('charlie')]"
        l.sort(reverse=True)
        assert repr(l) == "[CaselessString('charlie'), 'Bravo', CaselessString('alpha')]"

    def test_str(self):
        bravo=CaselessString('Bravo')
        assert type(str(bravo)) == str
        assert bravo == str(bravo)
        assert str(bravo) == bravo
