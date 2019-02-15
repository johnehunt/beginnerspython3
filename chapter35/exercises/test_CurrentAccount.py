import pytest
import fintech.accounts as accounts


@pytest.fixture
def current_account():
    """Returns a CurrentAccount instance"""
    print('CurrentAccount fixture')
    return accounts.CurrentAccount('123', 'John', 0.0, 100.0)


def test_opening_balance(current_account):
    assert current_account.balance == 0.0


def test_deposit(current_account):
    current_account.deposit(5.0)
    assert current_account.balance == 5.0


def test_deposit_twice(current_account):
    current_account.deposit(5.0)
    current_account.deposit(5.0)
    assert current_account.balance == 10.0


def test_deposit_negative_amount(current_account):
    with pytest.raises(accounts.AmountError):
        current_account.deposit(-10.00)


def test_deposit_zero(current_account):
    current_account.deposit(0.00)
    assert current_account.balance == 0.0


def test_withdraw(current_account):
    current_account.withdraw(5.0)
    assert current_account.balance == -5.0


def test_withdraw_negative_amount(current_account):
    with pytest.raises(accounts.AmountError):
        current_account.withdraw(-5.0)


def test_withdraw_zero(current_account):
    current_account.withdraw(0.0)
    assert current_account.balance == 0.0


def test_withdraw_twice(current_account):
    current_account.withdraw(5.0)
    current_account.withdraw(5.0)
    assert current_account.balance == -10.0


def test_deposit_and_withdraw(current_account):
    current_account.deposit(10.0)
    current_account.withdraw(5.0)
    assert current_account.balance == 5.0


def test_withdraw_above_overdraftlimit(current_account):
    with pytest.raises(accounts.BalanceError):
        current_account.withdraw(200.0)
