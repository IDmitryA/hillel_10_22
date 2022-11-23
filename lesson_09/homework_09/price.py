from dataclasses import dataclass

from exchange_rates import usd_rates


@dataclass
class Price:
    amount: int
    currency: str

    def exchange(self, other: "Price") -> None:
        """Exchanging currencies if needed"""
        if self.currency == other.currency:
            pass
        elif other.currency == "USD":
            other.amount *= usd_rates[self.currency]
        elif self.currency == "USD":
            other.amount /= usd_rates[other.currency]
        else:
            other.amount /= usd_rates[other.currency]
            other.amount *= usd_rates[self.currency]

    def __add__(self, other: "Price") -> "Price":
        Price.exchange(self, other)
        return Price(round(self.amount + other.amount, 2), self.currency)

    def __sub__(self, other: "Price") -> "Price":
        Price.exchange(self, other)
        return Price(round(self.amount - other.amount, 2), self.currency)
