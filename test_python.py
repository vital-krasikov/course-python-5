from myfunctions import my_filter, my_map
from math import pi, sqrt, pow, hypot


# для тестирования filter используем функцию my_filter с 4го занятия
def test_filter():
    assert my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5]
    assert my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2]
    assert my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5]
    assert my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b']


# для тестирования map дописали туда же аналогичную обертку для map
def test_map():
    assert my_map([1, 2, 3, 4, 5], lambda x: 2 * x + 3) == [5, 7, 9, 11, 13]
    assert my_map([1, 2, 3, 4, 5], lambda x: x ** 2) == [1, 4, 9, 16, 25]
    assert my_map(['a', 'b', 'c', 'd'], lambda x: 'a' + x + 'o') == ['aao', 'abo', 'aco', 'ado']


def test_sorted():
    assert sorted(['one', 'two', 'list', '', 'dict']) == ['', 'dict', 'list', 'one', 'two']
    assert sorted(('one', 'two', 'list', '', 'dict')) == ['', 'dict', 'list', 'one', 'two']
    assert sorted({'one', 'two', 'list', '', 'dict'}) == ['', 'dict', 'list', 'one', 'two']
    assert sorted('long string') == [' ', 'g', 'g', 'i', 'l', 'n', 'n', 'o', 'r', 's', 't']
    assert sorted({'id': 1, 'name': 'London', 'IT_VLAN': 320, 'User_VLAN': 1010, 'Mngmt_VLAN': 99, 'to_name': None,
                   'to_id': None, 'port': 'G1/0/11'}) == ['IT_VLAN', 'Mngmt_VLAN', 'User_VLAN', 'id', 'name', 'port',
                                                          'to_id', 'to_name']


def test_pi():
    assert pi == 3.141592653589793


def test_sqrt():
    assert sqrt(0) == 0
    assert sqrt(1) == 1
    assert sqrt(4) == 2
    assert sqrt(9) == 3


def test_pow():
    assert pow(2, 2) == 4
    assert pow(3, 3) == 27
    assert pow(9, 1/2) == 3
    assert pow(625, 1/4) == 5


def test_hypot():
    assert hypot(3, 4) == 5
    assert hypot(1, 2) == sqrt(5)
    assert hypot(2, 3) == sqrt(13)
