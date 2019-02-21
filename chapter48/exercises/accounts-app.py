import logging
import logging.config
import yaml
import fintech.accounts as accounts

with open('accounts.logging.config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger()

acc1 = accounts.CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = accounts.DepositAccount('345', 'John', 23.55, 0.5)
acc3 = accounts.InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')

logger.info(acc1)
logger.info(acc2)
logger.info(acc3)

acc1.deposit(23.45)
acc1.withdraw(12.33)
logger.info('balance:', acc1.balance)

logger.info('Number of Account instances created:', accounts.Account.instance_count)

try:
    logger.info('balance:', acc1.balance)
    acc1.withdraw(300.00)
    logger.info('balance:', acc1.balance)
except accounts.BalanceError as e:
    logger.error('Handling a Balance Exception')
    logger.exception(e)

with accounts.CurrentAccount ('891', 'Adam', 5.0, 50.0) as acc:
    acc.deposit(23.0)
    acc.withdraw(12.50)
    logger.info(acc.balance)

logger.info('acc1.branch:', acc1.branch)

for transaction in acc1:
    logger.info(transaction)

try:
    acc1.deposit(-1.0)
except accounts.AmountError as e:
    logger.error('Exception following a deposit')
    logger.exception(e)
