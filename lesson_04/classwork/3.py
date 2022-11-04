from typing import Generator, Iterable

data = [3, 4, 54, 54, 3, 2, 45, 56, 654, 42, 2, 5, 3, 68, 33, 36]


class User:
    def __init__(self, username: str, age: int) -> None:
        self.username: str = username
        self.age: int = age

    def __repr__(self) -> str:
        return f"{self.username=}, {self.age}"


def only_adults(users: Iterable) -> Generator:
    for user in users:
        if user.age > 18:
            yield user


mary = User(username="Mary", age=12)
john = User(username="John", age=22)
gleb = User(username="Gleb", age=19)

user_list = [mary, john, gleb]

adult_users = only_adults(user_list)
print(list(adult_users))

# def deduplicate(some_data: Iterable) -> Generator:
#     values = set()
#     for el in some_data:
#         if el in values:
#             continue
#         values.add(el)
#         yield el
#
#
# for element in deduplicate(data):
#     print(element)


# def get_list_without_duplicates(some_data: list) -> list:
#     new_data = []
#     for element in some_data:
#         if element in new_data:
#             continue
#         else:
#             new_data.append(element)
#     return new_data

# filtered = get_list_without_duplicates(data)

# print(f"{data=}")
# print(f"{filtered=}")
