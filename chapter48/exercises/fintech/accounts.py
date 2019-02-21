from abc import ABCMeta
import logging

from timeit import default_timer

# Accounts module
logger = logging.getLogger(__name__)


def timer(func):
    def inner(self, value):
        logger.info('calling %s on %s with %d', func.__name__, self, value)
        start = default_timer()
        func(self, value)
        end = default_timer()
        logger.info('returned from %s it took %d seconds', func.__name__, end - start)

    return inner


class BalanceError(Exception):
    """ The Balance will be invalid """

    def __init__(self, account):
        self.account = account


class AmountError(Exception):

    def __init__(self, account, msg):
        self.account = account
        self.message = msg

    def __str__(self):
        return 'AmountError (' + self.message + ') on ' + str(self.account)


class Transaction:
    """ A Class used to represent an individual Transaction """

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount

    def __str__(self):
        return 'Transaction[' + self.action + ': ' + str(self.amount) + ']'


class Account(metaclass=ABCMeta):
    """" A class used to represent a type of account """

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        logger.debug('Creating new Account')
        cls.instance_count += 1

    def __init__(self, account_number, account_holder, opening_balance, account_type):
        Account.increment_instance_count()
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = opening_balance
        self.type = account_type
        # Note need to initialise the history list before you try to add a Transaction
        self.history = []
        self._add_deposit_transaction(opening_balance)

    def __enter__(self):
        logger.debug('__enter__')
        return self

    def __exit__(self, *args):
        logger.debug('__exit__: %s', args)
        return True

    # Method called if attribute is unknown
    def __getattr__(self, attribute):
        logger.debug('__getattr__: unknown attribute accessed - %s', attribute)
        return -1

    # Return the transaction hsitory as the iterable object for an Account
    # and any subclass of Account
    def __iter__(self):
        return iter(self.history)

    # Provide internal support for adding transactions
    # Note by convention methods starting with an '_' shoudl not be called
    # by clients of this class
    def _add_transaction(self, transaction):
        logger.debug('adding transaction %s', transaction)
        self.history.append(transaction)

    # These are convenience methods to make it easier to
    # record a deposit or withdrawal.
    def _add_deposit_transaction(self, amount):
        self._add_transaction(Transaction('deposit', amount))

    def _add_withdraw_transaction(self, amount):
        self._add_transaction(Transaction('withdraw', amount))

    @timer
    def deposit(self, amount):
        if amount < 0:
            logger.debug('You cannot deposit negative amounts')
            raise AmountError(account=self, msg='Cannot deposit negative amounts')
        else:
            self._balance += amount
            self._add_deposit_transaction(amount)

    @timer
    def withdraw(self, amount):
        if amount < 0:
            logger.debug('You cannot withdraw negative amounts')
            raise AmountError(self, 'Cannot withdraw negative amounts')
        else:
            self._balance -= amount
            self._add_withdraw_transaction(amount)

    @property
    def balance(self):
        """ Provides the current balance """
        return self._balance

    def __str__(self):
        return 'Account[' + self.account_number + '] - ' + \
               self.account_holder + ', ' + self.type + ' account = ' + str(self.balance)


class CurrentAccount(Account):

    def __init__(self, account_number, account_holder, opening_balance, overdraft_limit):
        super().__init__(account_number, account_holder, opening_balance, 'current')
        self.overdraft_limit = -overdraft_limit

    @timer
    def withdraw(self, amount):
        if amount < 0:
            logger.debug('You cannot withdraw negative amounts')
            raise AmountError(self, 'Cannot withdraw negative amounts')
        elif self.balance - amount < self.overdraft_limit:
            logger.debug('Withdrawal would exceed your overdraft limit')
            raise BalanceError(self)
        else:
            self._balance -= amount
            self._add_withdraw_transaction(amount)

    def __str__(self):
        return super().__str__() + 'overdraft limit: ' + str(self.overdraft_limit)


class DepositAccount(Account):

    def __init__(self, account_number, account_holder, opening_balance, interest_rate):
        super().__init__(account_number, account_holder, opening_balance, 'deposit')
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + 'interest rate: ' + str(self.interest_rate)


class InvestmentAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, investment_type):
        super().__init__(account_number, account_holder, opening_balance, 'investment')
        self.investment_type = investment_type

    def __str__(self):
        return super().__str__() + ', type: ' + self.type
