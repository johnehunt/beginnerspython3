from abc import ABCMeta

class Account(metaclass=ABCMeta):
    """" A class used to represent a type of account """

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        print('Creating new Account')
        cls.instance_count += 1

    def __init__(self, account_number, account_holder, opening_balance, account_type):
        Account.increment_instance_count()
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = opening_balance
        self.type = account_type

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @property
    def balance(self):
        """ Provides the current balance """
        return self._balance

    def __str__(self):
        return 'Account[' + self.account_number +'] - ' + \
               self.account_holder + ', ' + self.type + ' account = ' + str(self.balance)

class BalanceError(Exception):
    """ Valid Ages must be between 0 and 120 """

    def __init__(self, account):
        self.account = account

class CurrentAccount(Account):

    def __init__(self, account_number, account_holder, opening_balance, account_type, overdraft_limit):
        super().__init__(account_number, account_holder, opening_balance, account_type)
        self.overdraft_limit = -overdraft_limit

    def withdraw(self, amount):
        if self._balance - amount < self.overdraft_limit:
            print('Withdrawal would exceed your overdraft limit')
            raise BalanceError(self)
        else:
            self._balance -= amount

    def __str__(self):
        return super().__str__() + ' overdraft limit: ' + str(self.overdraft_limit)


class DepositAccount(Account):

    def __init__(self, account_number, account_holder, opening_balance, account_type, interest_rate):
        super().__init__(account_number, account_holder, opening_balance, account_type)
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + 'interest rate: ' + str(self.interest_rate)

class InvestmentAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, account_type, investment_type):
        super().__init__(account_number, account_holder, opening_balance, account_type)
        self.investment_type = investment_type

    def __str__(self):
        return super().__str__() + ', type: ' + self.type