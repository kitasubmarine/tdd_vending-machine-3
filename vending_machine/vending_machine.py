class vending_machine:
    def __init__(self):
        self.money=0

    def insert(self,yen):
        available_yen = [1,5,10,50,100,500,1000]
        if yen in available_yen:
            self.money += yen
            return yen
        else:
            return yen

    def get_total(self,yen):
        return self.money
    
    def reject_money(self):
        tmp=self.money
        self.money=0
        return tmp

