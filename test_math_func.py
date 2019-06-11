import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(7,0) == 7

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(0) == 0
    assert math_func.product(3, 0) == 0

def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) == str
    assert 'Heldo' not in result


def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result =math_func.product("hello ")
    assert result == 'hello hello '
    assert type(result) == str
    assert 'hello' in result


