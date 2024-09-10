# patch的用法
import unittest
from unittest.mock import patch


def f1():
    return 'f1'


def f2():
    return 'f2'


class Testf(unittest.TestCase):
    # 这里直接写patch(f1)会报错，因为官方格式必须是@patch('module.ClassName2')
    """
    target, attribute = target.rsplit('.', 1)
    ValueError: not enough values to unpack (expected 2, got 1)
    During handling of the above exception, another exception occurred:
    TypeError: Need a valid target to patch. You supplied: 'f1'
    """

    # 因为就是这个文件里的，所以就写上当前文件的名字就可以
    @unittest.mock.patch("test_patch_2.f1")
    def test_f1(self, fun):
        # 因为patch了f1，所以下面的fun指的就是f1了
        fun.return_value = 'sb'
        print(f1())  # sb
        print(f2())  # f2


if __name__ == "__main__":
    unittest.main()
