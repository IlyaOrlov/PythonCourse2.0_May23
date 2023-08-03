import pytest
import Loginova_14


class TestMyProv:
    _m_test = Loginova_14.MyFun()

    def test_to_roman(self):
        assert (self._m_test.to_roman(3459) == 'MMMCDLIX')

    @pytest.mark.parametrize("number", ['3459', 5521, -2])
    def test_my_error1(self, number):
        with pytest.raises(Loginova_14.MyError):
            self._m_test.to_roman(number)
