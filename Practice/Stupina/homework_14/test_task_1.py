from task_1 import MyException, num_to_roman
import pytest


class TestPyTest:
    def test_eq(self):
        assert num_to_roman(1111) == 'MCXI'

    @pytest.fixture(
        scope='function',
        params=['3212', 0, 5689],
        ids=lambda args: f"Test with args: '{args}'"
    )
    def parametrize_task_1(self, request):
        return request.param

    def test_error(self, parametrize_task_1):
        arg = parametrize_task_1
        with pytest.raises(MyException):
            num_to_roman(arg)
