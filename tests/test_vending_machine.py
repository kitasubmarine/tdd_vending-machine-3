from vending_machine.vending_machine import vending_machine

class test_vending_machine:
    def test_insert(self):
        vdd = vending_machine()
        yen = 1
        assert (vdd.insert(yen) == 10) or (vdd.insert(yen) == 50) /
        or (vdd.insert(yen) == 100) or (vdd.insert(yen) == 500) or (vdd.insert(yen) == 1000)