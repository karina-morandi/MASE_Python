from AccountObj import Account


class CheckingAccount(Account):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= (super().get_acc_balance() + self.__overdraft_limit):
            bal = super().get_acc_balance() - amount
            super().set_balance(bal)
        else:
            print("Exceeded overdraft limit in account:")
            super().account_info()
            print("Overdraft limit is: €{0}".format(self.__overdraft_limit))