# module name : patchTest
import unittest
from unittest import mock


def verbose_adder(arg1, arg2, kwarg1='default'):
    print(kwarg1)  # side-effect
    return arg1 + arg2  # post-condition


def func_to_test():
    return verbose_adder(10, 10)


def print_test_info(*args, **kwargs):
    print('this is a microphone check.')
    print('arguments:', args, kwargs)
    return mock.DEFAULT  # NOTICE here


class TestPatch(unittest.TestCase):
    @mock.patch('patchTest.verbose_adder')
    def test_func_to_test__decorator(self, mock_obj):
        mock_obj.return_value = 3
        mock_obj.side_effect = print_test_info
        assert func_to_test() == 3

    def test_func_to_test__context(self):
        with mock.patch('patchTest.verbose_adder') as mock_obj:
            mock_obj.return_value = 3
            mock_obj.side_effect = print_test_info
            assert func_to_test() == 3

    def test_func_to_test__context_2(self):
        with mock.patch('patchTest.verbose_adder', return_value=3, side_effect=print_test_info):
            assert func_to_test() == 3

    @mock.patch('patchTest.verbose_adder', return_value=3, side_effect=print_test_info)
    def test_func_to_test__decorator_2(self, verbose_adder):
        assert func_to_test() == 3


if __name__ == '__main__':
    unittest.main()
