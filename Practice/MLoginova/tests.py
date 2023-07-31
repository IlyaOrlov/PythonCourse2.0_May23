import pytest
import Loginova_14


class TestMyProv:
    @pytest.fixture(
        scope='function',
        params=[(566, 'DLXVI'), ('7', 'NonValidInput'), (-5, 'NonValidInput'), (10000000, 'NonValidInput')],
        ids=lambda args: f"Test fun with args: {args}"
    )
    def parametrize_sum(self, request):
        return request.param

    def test_my_sum(self, parametrize_sum):
        res = Loginova_14.m1.to_roman()
        assert(res, parametrize_sum)
