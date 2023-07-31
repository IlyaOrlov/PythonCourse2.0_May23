import pytest
import my_ops


class TestMySum:
    @pytest.fixture(
        scope='function',
        params=[(10, 20, 30), (-10, -20, -30), (10, 0, 10), (10, -10, 0)],
        ids=lambda args: f"Test fun with args: {args}"
    )
    def parametrize_sum(self, request):
        return request.param

    def test_my_sum(self, parametrize_sum):
        arg1, arg2, expected = parametrize_sum
        res = my_ops.my_sum(arg1, arg2)
        assert(res, expected)


class TestMyDif:
    @pytest.fixture(
        scope='function',
        params=[(10, 20, -20), (-10, -20, 10), (10, 0, 10), (10, -10, 20)],
        ids=lambda args: f"Test fun with args: {args}"
    )
    def parametrize_dif(self, request):
        return request.param


    def test_my_dif(self, parametrize_dif):
        arg1, arg2, expected = parametrize_dif
        res = my_ops.my_dif(arg1, arg2)
        assert(res, expected)
