class Colorizer:
    colors = {
        "grey": 90,
        "red": 91,
        "green": 92,
        "yellow": 93,
        "blue": 94,
        "pink": 95,
        "cyan": 96,
    }

    def __init__(self, color):
        self.color: int = self.colors.get(color)

    def __enter__(self):
        return print(f"\033[{self.color}m", end="")

    def __exit__(self, type, value, traceback):
        return print("\033[0m", end="")


with Colorizer("red"):
    print("printed in red")

print("printed in default color")
