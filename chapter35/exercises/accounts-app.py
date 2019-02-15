import fintech.accounts as accounts

acc1 = accounts.CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = accounts.DepositAccount('345', 'John', 23.55, 0.5)
acc3 = accounts.InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')

print(acc1)
print(acc2)
print(acc3)

acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.balance)

print('Number of Account instances created:', accounts.Account.instance_count)

try:
    print('balance:', acc1.balance)
    acc1.withdraw(300.00)
    print('balance:', acc1.balance)
except accounts.BalanceError as e:
    print('Handling Exception')
    print(e)

with accounts.CurrentAccount ('891', 'Adam', 5.0, 50.0) as acc:
    acc.deposit(23.0)
    acc.withdraw(12.50)
    print(acc.balance)

print('acc1.branch:', acc1.branch)

for transaction in acc1:
    print(transaction)

acc1.deposit(-1.0)