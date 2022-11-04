from pathlib import Path
from typing import Generator

# from pympler import asizeof

CLASSWORK_DIR = Path(__file__).parent
FILENAME = CLASSWORK_DIR / "text.txt"
ROCKYOU_FILENAME = CLASSWORK_DIR / "rockyou.txt"
PATTERN = "john"

john = []

# with open(ROCKYOU_FILENAME) as file:
#     lines: list = file.readlines()
#     for line in lines:
#         if PATTERN in line.lower():
#             john.append(PATTERN)


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename) as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if pattern in line.lower():
                yield line


johns = list(filter_lines(ROCKYOU_FILENAME, "john"))

print(len(johns))
