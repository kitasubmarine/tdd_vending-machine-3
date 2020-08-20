class Coin:
    def __init__(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value


class Coin_10(Coin):
    def __init__(self) -> None:
        super().__init__(10)


class Coin_50(Coin):
    def __init__(self) -> None:
        super().__init__(50)


class Coin_100(Coin):
    def __init__(self) -> None:
        super().__init__(100)


class Coin_500(Coin):
    def __init__(self) -> None:
        super().__init__(500)


class Coin_1000(Coin):
    def __init__(self) -> None:
        super().__init__(1000)
