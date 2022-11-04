from pathlib import Path
from typing import Generator

from pympler import asizeof

FILENAME = "rockyou.txt"
FILTERED_FILENAME = "filtered.txt"
CURRENT_DIR = Path(__file__).parent
FULL_FILENAME: Path = CURRENT_DIR / FILENAME
FULL_FILTERED_FILENAME: Path = CURRENT_DIR / FILTERED_FILENAME

user_parameter: str = input("Enter your parameter:\n")


def creating_filtered_file(parameter: str) -> Generator:
    with open(FULL_FILENAME) as file1:
        while True:
            line: str = file1.readline()
            if not line:
                break
            if parameter in line.lower():
                yield line.rstrip()


with open(FULL_FILTERED_FILENAME, "w") as file2:
    for element in creating_filtered_file(user_parameter):
        file2.write(f"{element}\n")


def get_file_information(filename) -> tuple:
    with open(filename) as file3:
        text: str = file3.read()
        size_text: int = asizeof.asizeof(text)
        length_text: int = text.count("\n")
    return size_text, length_text


files_information = (
    f"{FULL_FILENAME}:\n- total lines: "
    f"{get_file_information(FULL_FILENAME)[1]}"
    f"\n- total size: {get_file_information(FULL_FILENAME)[0]}\n"
    f"{FULL_FILTERED_FILENAME}:\n- total lines: "
    f"{get_file_information(FULL_FILTERED_FILENAME)[1]}\n"
    f"- total size: {get_file_information(FULL_FILTERED_FILENAME)[0]}"
)

print(files_information)
