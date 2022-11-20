from dataclasses import dataclass


@dataclass
class Price:
    amount: int
    currency: str

    def __add__(self, other: "Price") -> "Price":
        return Price(round(self.amount + other.amount, 2), self.currency)

    def __sub__(self, other: "Price") -> "Price":
        return Price(round(self.amount - other.amount, 2), self.currency)
