import pytest
import Loginova_14


class TestMyProv:

    def test_to_roman(self):
        assert (Loginova_14.m1.to_roman(3459) == 'MMMCDLIX')

    def test_my_error1(self):
        with pytest.raises(Loginova_14.MyError):
            Loginova_14.m1.to_roman('3459')

    def test_my_error2(self):
        with pytest.raises(Loginova_14.MyError):
            Loginova_14.m1.to_roman(5521)

    def test_my_error3(self):
        with pytest.raises(Loginova_14.MyError):
            Loginova_14.m1.to_roman(-2)
