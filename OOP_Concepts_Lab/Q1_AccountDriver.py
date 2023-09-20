from Accounts import Saving

def main():
    print("Savings bank")
    hp_account = Saving("Harry Potter", 1000)
    hp_account.account_info()
    hp_account.withdraw(250)
    hp_account.withdraw(250)
    hp_account.withdraw(250)
    hp_account.withdraw(300)
    hp_account.deposit(150)
    hp_account.account_info()

if __name__ == "__main__":
    main()