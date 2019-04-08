import pytest
from calculator import Calculator


@pytest.fixture(scope='session', autouse=True)
def session_scope_fixture():
    print('session_scope_fixture')


@pytest.fixture(scope='module', autouse=True)
def module_scope_fixture():
    print('module_scope_fixture')


@pytest.fixture(scope='class', autouse=True)
def class_scope_fixture():
    print('class_scope_fixture')


@pytest.fixture
def calculator():
    """ Returns a Calculator instance """
    print('calculator fixture')
    return Calculator()


def test_initial_value(calculator):
    assert calculator.total == 0


def test_add_one(calculator):
    calculator.set(1)
    calculator.add()
    assert calculator.total == 1


def test_subtract_one(calculator):
    calculator.set(1)
    calculator.sub()
    assert calculator.total == -1


def test_add_one_and_one(calculator):
    calculator.set(1)
    calculator.add()
    calculator.set(1)
    calculator.add()
    assert calculator.total == 2


@pytest.mark.parametrize('input1,input2,expected', [
    (3, 1, 4),
    (3, 2, 5),
])
def test_calculator_add_operation(calculator, input1, input2, expected):
    calculator.set(input1)
    calculator.add()
    calculator.set(input2)
    calculator.add()
    assert calculator.total == expected


@pytest.mark.skip(reason='not implemented yet')
def test_calculator_multiply(calculator):
    calculator.multiply(2, 3)
    assert calculator.total == 6
