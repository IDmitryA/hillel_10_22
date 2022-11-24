from exchange_rates import usd_rates
from price import Price


class UserInputError(Exception):
    def __str__(self):
        return "Wrong input format. Use the following format: 1 UAH +/- 1 UAH"


class SignError(Exception):
    def __str__(self):
        return "Wrong sign. You can choose just between '+' and '-'"


def handle_errors(func):
    def inner(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except UserInputError as error:
                print(error)
                continue
            except SignError as error:
                print(error)
                continue
            except Exception as error:
                print(f"Something going wrong: {error}")
                continue

    return inner


@handle_errors
def main():
    user_input: list[str] = input(
        f"Enter your request in the following format: 1 UAH +/- 1 UAH.\n"
        f"Available currencies{list(usd_rates.keys()) + ['USD']}:\n"
    ).split(" ")

    #  Initial check for valid input format
    if len(user_input) != 5:
        raise UserInputError

    operand_1: str = user_input[0]
    operand_2: str = user_input[3]
    sign: str = user_input[2]
    currency_1: str = user_input[1].strip().upper()
    currency_2: str = user_input[4].strip().upper()

    #  Main check if input consist of valid items
    if any(
        [
            not operand_1.isdigit(),
            currency_1 not in (list(usd_rates.keys()) + ["USD"]),
            not operand_2.isdigit(),
            currency_2 not in (list(usd_rates.keys()) + ["USD"]),
        ]
    ):
        raise UserInputError
    elif sign not in ["+", "-"]:
        raise SignError

    #  Create two instances of "Price" using input data
    price_1: Price = Price(int(operand_1), currency_1)
    price_2: Price = Price(int(operand_2), currency_2)

    #  Main calculation process(don't use "elif sign == '-'" because of previous sign check (it can be just "+" or "-"))
    result_price = price_1 + price_2 if sign == "+" else price_1 - price_2
    print(f"{result_price.amount} {result_price.currency}")


if __name__ == "__main__":
    main()
