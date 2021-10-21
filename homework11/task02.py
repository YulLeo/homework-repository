from typing import Callable


class Order:
    """
    Returns order price with applied discount strategy
    """
    def __init__(self, price: float, discount_strategy: Callable = None):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self) -> float:
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount


def morning_discount(order: Order) -> float:
    return order.price * 0.25


def elder_discount(order: Order) -> float:
    return order.price * 0.75
