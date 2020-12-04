# import pytest
#
# def add(a, b):
#     return a + b
#
# @pytest.mark.parametrize('a, b, c', ([1,2,3],[4,13,9],[7,8,15]))
# class TestAbc():
#     def test_add1(self,a,b,c):  # => 作为用例参数，接收装饰器传入的数据
#         assert add(a, b) == c
#     def test_add2(self,a,b,c):  # => 作为用例参数，接收装饰器传入的数据
#         assert add(a, c) == b
#     def test_other(self,a,b,c):
#         print("\na,b的值分别为:","{a},{b}")
#
# if __name__ == '__main__':
#     pytest.main(["-s", "demo.py","-v"])