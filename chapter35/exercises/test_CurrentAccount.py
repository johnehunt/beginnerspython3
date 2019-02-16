import pytest
import fintech.accounts as accounts


@pytest.fixture
def current_account():
    """Returns a CurrentAccount instance"""
    print('CurrentAccount fixture')
    return accounts.CurrentAccount('123', 'John', 0.0, 100.0)


def test_opening_balance(current_account):
    assert current_account.balance == 0.0


def test_alternative_opening_balance():
    current_account = accounts.CurrentAccount('123', 'John', 10.0, 100.0)
    assert current_account.balance == 10.00


def test_negative_opening_balance():
    current_account = accounts.CurrentAccount('123', 'John', -10.0, 100.0)
    assert current_account.balance == -10.00


def test_current_account_attributes(current_account):
    assert current_account.account_holder == 'John'
    assert current_account.account_number == '123'
    assert current_account.overdraft_limit == -100.0
    assert current_account.type == 'current'


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


def test_withdraw_and_deposit(current_account):
    current_account.withdraw(5.0)
    current_account.deposit(10.0)
    assert current_account.balance == 5.0


def test_withdraw_above_overdraftlimit(current_account):
    with pytest.raises(accounts.BalanceError):
        current_account.withdraw(200.0)


def test_initial_transaction_history_length(current_account):
    assert len(current_account.history) == 1


def test_initial_transaction_details(current_account):
    transaction = current_account.history[0]
    assert transaction.action == 'deposit'
    assert transaction.amount == 0.0


def test_deposit_transaction_history(current_account):
    current_account.deposit(10.0)
    current_account.deposit(5.0)
    assert len(current_account.history) == 3
    transaction1 = current_account.history[1]
    transaction2 = current_account.history[2]
    assert transaction1.action == 'deposit'
    assert transaction1.amount == 10.0
    assert transaction2.action == 'deposit'
    assert transaction2.amount == 5.0


def test_withdrawal_transaction_history(current_account):
    current_account.withdraw(10.0)
    current_account.withdraw(5.0)
    assert len(current_account.history) == 3
    transaction1 = current_account.history[1]
    transaction2 = current_account.history[2]
    assert transaction1.action == 'withdraw'
    assert transaction1.amount == 10.0
    assert transaction2.action == 'withdraw'
    assert transaction2.amount == 5.0


def test_withdrawal_and_deposit_transaction_history(current_account):
    current_account.deposit(10.0)
    current_account.withdraw(5.0)
    assert len(current_account.history) == 3
    transaction1 = current_account.history[1]
    transaction2 = current_account.history[2]
    assert transaction1.action == 'deposit'
    assert transaction1.amount == 10.0
    assert transaction2.action == 'withdraw'
    assert transaction2.amount == 5.0
