from vending_machine.vending_machine import vending_machine
# リファクタリングの余地あり

class TestVendingMachine:
    def test_insert(self):
        vdd = vending_machine()
        # pytest parameterizeを使ってスマートに書く
        # 1つの関数で複数のテストが出来るようにする
        for yen in (10, 50, 100, 500, 1000):
            assert vdd.insert(yen)
        for yen in (1, 5, 2000, 5000, 10000):
            assert ~vdd.insert(yen)

    def test_get_total(self):
        vdd = vending_machine()
        for yen in (10, 50, 100, 500, 1000):
            vdd.insert(yen)
        assert vdd.get_total() == 1660

    def test_reject_money(self):
        vdd = vending_machine()
        for yen in (10, 50, 100, 500, 1000):
            vdd.insert(yen)
        assert vdd.reject_money() == 1660
        assert vdd.money == 0

        
