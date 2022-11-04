from typing import Generator
from uuid import UUID, uuid4

"""
class User:
    def __init__(self, username: str) -> None:
        self.id_: UUID = self.get_id(username)
        self.username: str = username

    def get_id(self, value: str) -> UUID:
        return uuid3(NAMESPACE_DNS, value)

    def __str__(self) -> str:
        return f"{self.username=}, {self.id_}"
"""


def create_uniq_uuid() -> Generator:
    data = set()
    while True:
        new_value: UUID = uuid4()
        if new_value in data:
            continue
        data.add(new_value)
        yield new_value


class User:
    random_uuid: Generator = create_uniq_uuid()

    def __init__(self, username: str) -> None:
        self.id_: UUID = next(self.random_uuid)
        self.username: str = username

    def __str__(self) -> str:
        return f"{self.username=}, {self.id_}"


john = User(username="John")
another_john = User(username="John")
mary = User(username="Mary")

print(john)
print(another_john)
print(mary)
