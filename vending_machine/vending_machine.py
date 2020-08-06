class vending_machine:
 # リファクタリングの余地あり

#  coinクラスを作って、40円コインがないようにする
    price={'コーラ': 120}
    def __init__(self):
        self.money=0
        self.storage={'コーラ': 5}


    def insert(self,yen):
        available_yen = [10,50,100,500,1000]
        if yen in available_yen:
            self.money += yen
            return True
        else:
            return False

    def get_total(self):
        return self.money
    
    def reject_money(self):
        tmp=self.money
        self.money=0
        return tmp

    def buy(self, drink_name):
        for item in self.storage.keys():
            if self.storage[item] >= 1:
                self.storage[item] -= 1

