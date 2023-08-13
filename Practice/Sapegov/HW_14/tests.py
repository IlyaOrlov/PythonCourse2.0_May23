import pytest
import Sap14_1
from Sap14_1 import to_roman


class TestSap14Suite:

    @pytest.fixture(
        scope='function',
        params=[('8', 'VIII'), ('4509', 'MMMMDIX'), ('5000', 'MMMMM')],
        ids=lambda args: f"Test with args: '{args}'"
    )
    def positive_parametrs(self, request):
        return request.param

    def test_to_roman1(self, positive_parametrs):
        arg, res = positive_parametrs
        assert to_roman(arg) == res

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
