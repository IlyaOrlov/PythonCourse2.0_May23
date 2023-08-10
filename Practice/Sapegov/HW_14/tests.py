import pytest
import Sap14_1
from Sap14_1 import to_roman


class TestSap14Suite:

    def test_to_roman1(self):
        assert(to_roman('8') == 'VIII')

    def test_to_roman2(self):
        assert(to_roman('4509') == 'MMMMDIX')

    def test_to_roman3(self):
        assert(to_roman('5000') == 'MM')

    @pytest.fixture(
        scope='function',
        params=['5521', '-2', '33'],
        ids=lambda args: f"Test with args: '{args}'"
    )
    def parametrs(self, request):
        return request.param

    def test_exception(self, parametrs):
        raises_args = parametrs
        with pytest.raises(Sap14_1.NonValidInputError):
            to_roman(raises_args)


if __name__ == '__main__':
    pytest.main()
