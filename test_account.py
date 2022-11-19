import pytest as pytest

from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Heather')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a2.get_name() == 'Heather'
        assert self.a1.get_balance() == 0
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        self.a1.deposit(20)
        assert self.a1.get_balance() == 20
        self.a1.deposit(0.1)
        assert self.a1.get_balance() == 20.1
        assert self.a1.deposit(20) == True
        assert self.a1.deposit(0.1) == True
        self.a2.deposit(-2)
        assert self.a2.get_balance() == 0
        assert self.a2.deposit(-20) == False
    def test_withdraw(self):
        self.a1.deposit(20)
        assert self.a1.withdraw(15) == True
        self.a1.withdraw(0.1)
        assert self.a1.get_balance() == 4.9
        assert self.a1.withdraw(0.1) == True
        assert self.a2.withdraw(-1) == False
        self.a2.deposit(20)
        assert self.a2.withdraw(30) == False

    def test_get_name(self):
        assert self.a1.get_name() == 'John'
        assert self.a2.get_name() == 'Heather'

    def test_get_balance(self):
        self.a1.deposit(20)
        self.a2.deposit(5)
        assert self.a1.get_balance() == 20
        assert self.a2.get_balance() == 5

if __name__ == '__main__':
    pytest.main()