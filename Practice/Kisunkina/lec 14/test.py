import pytest
from homework_14 import RomanNumber
from homework_14 import Error


class TestMyProv:
    _test_roman = RomanNumber()

    @pytest.mark.parametrize("number, roman_number", [(9, "IX"), (1050, "ML")])
    def test_to_roman(self, number, roman_number):
        assert self._test_roman.to_roman(number) == roman_number

    @pytest.mark.parametrize("number", ['3459', 5521, -2])
    def test_my_error1(self, number):
        with pytest.raises(Error):
            self._test_roman.to_roman(number)
