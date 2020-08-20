import pytest

from vending_machine.vending_machine import vending_machine
from vending_machine.coin import Coin_10, Coin_50, Coin_100, Coin_500, Coin_1000

# リファクタリングの余地あり


class TestVendingMachine:
    @pytest.mark.parametrize("inputs", [(Coin_10), (Coin_50), (Coin_100), (Coin_500), (Coin_1000)])
    def test_insert(self, inputs):
        vdd = vending_machine()
        input_coin = inputs()

        assert vdd.insert(input_coin)
        assert vdd.get_total() == input_coin.get_value()

    @pytest.mark.parametrize("inputs", [(30), ("100"), ("hoge")])
    def test_insert_invalid(self, inputs):
        vdd = vending_machine()
        input_coin = inputs

        assert vdd.insert(input_coin) == input_coin

    def test_get_total(self):
        vdd = vending_machine()
        for input_coin in (Coin_10(), Coin_50(), Coin_100(), Coin_500(), Coin_1000()):
            vdd.insert(input_coin)
        assert vdd.get_total() == 1660

    def test_reject_money(self):
        vdd = vending_machine()
        for input_coin in (Coin_10(), Coin_50(), Coin_100(), Coin_500(), Coin_1000()):
            vdd.insert(input_coin)
        assert vdd.reject_money() == 1660
        assert vdd.money == 0

