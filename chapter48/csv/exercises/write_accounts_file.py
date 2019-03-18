import csv
import fintech.accounts as accounts


def write_account_transaction_to_csv(filename, account):
    print('Starting write of dict CSV example')
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['transaction_type', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # Write out the transactions
        for transaction in account.history:
            writer.writerow({'transaction_type': transaction.action,
                             'amount': transaction.amount})


print('Starting')
acc = accounts.CurrentAccount('123', 'John', 10.05, 100.0)
acc.deposit(23.45)
acc.withdraw(12.33)

print('Writing Account Transactions')
write_account_transaction_to_csv('accounts.csv', acc)

print('Done')
