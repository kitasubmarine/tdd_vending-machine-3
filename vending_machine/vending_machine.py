from vending_machine.coin import Coin


class vending_machine:
    # リファクタリングの余地あり

    #  coinクラスを作って、40円コインがないようにする
    price = {"コーラ": 120}

    def __init__(self):
        self.money = 0
        self.storage = {"コーラ": 5}
        self.sale_amount = 0

    def insert(self, yen: Coin):
        if isinstance(yen, Coin):
            self.money += yen.get_value()
            return True
        else:
            return yen

    def get_total(self):
        return self.money

    def reject_money(self):
        tmp = self.money
        self.money = 0
        return tmp

    def buy(self, drink_name):
        for item in self.storage.keys():
            if self.storage[item] >= 1:
                self.storage[item] -= 1
