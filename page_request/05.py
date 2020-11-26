
import pytest

# @pytest.fixture()
# def fixtureFunc():
#     return 'fixtureFunc'
#
# def test_fixture(fixtureFunc):
#     print('我调用了{}'.format(fixtureFunc))
#
# class TestFixture(object):
#     def test_fixture_class(self, fixtureFunc):
#         print('在类中使用fixture "{}"'.format(fixtureFunc))
#
# if __name__=='__main__':
#     pytest.main(['-v', '05.py'])



# @pytest.fixture()
# def fixtureFunc():
#     print('\n fixture->fixtureFunc')
#
# @pytest.mark.usefixtures('fixtureFunc')
# def test_fixture():
#     print('in test_fixture')
#
# @pytest.mark.usefixtures('fixtureFunc')
# class TestFixture(object):
#     def test_fixture_class(self):
#         print('in class with text_fixture_class')
#
# if __name__=='__main__':
#     pytest.main(['-v', '05.py'])



# @pytest.fixture(autouse=True)
# def fixtureFunc():
#     print('\n fixture->fixtureFunc')
#
# def test_fixture():
#     print('in test_fixture')
#
# class TestFixture(object):
#     def test_fixture_class(self):
#         print('in class with text_fixture_class')
# if __name__=='__main__':
#     pytest.main(['-v', '05.py'])



@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('\n-----------------')
    print('我是module fixture')
    print('-----------------')

@pytest.fixture(scope='class')
def class_fixture():
    print('\n-----------------')
    print('我是class fixture')
    print('-------------------')

@pytest.fixture(scope='function', autouse=True)
def func_fixture():
    print('\n-----------------')
    print('我是function fixture')
    print('-------------------')

def test_1():
    print('\n 我是test1')

@pytest.mark.usefixtures('class_fixture')
class TestFixture1(object):
    def test_2(self):
        print('\n我是class1里面的test2')
    def test_3(self):
        print('\n我是class1里面的test3')

@pytest.mark.usefixtures('class_fixture')
class TestFixture2(object):
    def test_4(self):
       print('\n我是class2里面的test4')
    def test_5(self):
        print('\n我是class2里面的test5')


#单参数单值
@pytest.mark.parametrize("user",["18221124104"])
def test(user):
    print(user)
    assert user=="18221124104"

if __name__=='__main__':
    pytest.main(['-v', '--setup-show', '05.py'])
