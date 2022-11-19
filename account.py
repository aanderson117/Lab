class Account:
    def __init__(self, name: str):
        """""
        Function to create account with a name and initial balance
        :type name: str
        :param name: Name of the account
        """
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float):
        """
        Function to deposit money into the account
        Transaction will not affect account balance if amount is negative or zero
        :type amount: float
        :param amount: Amount to deposit
        :return: Returns true if the transaction went through, false if it did not go through
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float):
        """
        Function to withdraw money from the account.
        Transaction will not affect balance if amount is negative or zero
        :type amount: float
        :param amount: Amount to withdraw
        :return: Returns true if transaction went through, false if it did not go through
        """
        if self.__account_balance > amount:
            if amount > 0:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):
        """
        Function to get the balance of the account
        :return: Returns account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        Function to get the account name
        :return: Returns account name
        """
        return self.__account_name
