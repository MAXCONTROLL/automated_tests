import pytest

#TEST INT
#positive test
@pytest.mark.parametrize("a", [(0), (1), (-1), (-100), (100)])
def test_if_class_is_int(a):
    assert isinstance(a,int)

#negative test
@pytest.mark.parametrize("a", [(0.), ('Hello'), (-100.1), (' '), ([])])
def test_if_class_is_int(a):
    try:
        assert isinstance(a,int)
    except AssertionError:
        pass


@pytest.mark.parametrize("a, b, c", [(5, 5, 10), (0, 0, 0), (-100, 100, 0)])
def test_if_int_result_is_correct1(a, b, c):
    assert a + b == c

@pytest.mark.parametrize("a, b, c", [(1, 0, 0), (5, 1, 5), (-1, -1, 1)])
def test_if_int_result_is_correct2(a, b, c):
    assert a * b == c


def test_int_methods_is_incorrect():
    a = 0
    try:
        assert a.strip()
    except AttributeError:
        pass

#TEST LIST
#positive test
@pytest.mark.parametrize("a", [([]), (list())])
def test_if_class_is_list(a):
    assert isinstance(a,list)

#negative test
@pytest.mark.parametrize("a", [({}), (tuple()), (set())])
def test_if_class_is_list(a):
    try:
        assert isinstance(a,list)
    except AssertionError:
        pass


def test_list_methods_is_correct():
    list_ = []
    list_.append(5)
    assert list_ == [5,]

def test_list_index():
    list_ = ['один', 'два', 'три', 'четыре', 'пять']
    assert list_[1] == 'два'


def test_list_methods_is_incorrect():
    list_ = ['h', 'o']
    set_ = set('hello')

    try:
        assert list_.issubset(set_)
    except AttributeError:
        pass
