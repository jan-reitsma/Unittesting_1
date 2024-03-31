import unittest
from unittest.mock import MagicMock, patch

import main

class MyMockTestCase(unittest.TestCase):
    def test_1(self):
        '''Mock a method in a class and test if it has been called'''
        real1 = main.MyClass()
        real1.get_values = MagicMock(name="Mock method")
        real1.get_values()
        real1.get_values.assert_called_once()

    def test_2(self):
        '''Mock a function, another function that calls this function
        is now calling the mock function
        '''
        real2 = main.AnotherClass()
        real2.fun2 = MagicMock(name="Mock Version of fun2")
        real2.fun1(5) # fun1 is a real function
        real2.fun2.assert_called_with(10) # fun2 is a mock function

    def test_3(self):
        '''Mock a method of a class, same as test_1'''
        real3 = main.B()
        real3.something = MagicMock(name="Mock Version of something")
        real3.method()
        real3.something.assert_called_once_with(1,2,3)

    def test_4(self):
        '''Mock a class; create a mock object of this mock class; set return value
        of a method of this class; call a function outsideof this class, test if
        the return value of the mocked method is coming back.'''
        with patch('main.B') as mock: # mock of Class B
            instance = mock.return_value
            instance.method.return_value = 1
            result = main.fun1()
            assert result == 1

if __name__ == '__main__':
    unittest.main(verbosity=3)