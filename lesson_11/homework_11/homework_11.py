from threading import Thread
from typing import Generator

THREADS_NUMBER = 5


def iter_number() -> Generator:
    """
    This function calculates total number of checks needed to recognize prime numbers in the list
    and returns Generator that creates a list of tuples (thread_start, thread_end) for each thread.
    Intervals from 'thread_start' to 'thread_end' in each thread will be different,
    but checks number and time to make them of each interval will be just about equal.
    """
    start: int = int(input("Enter star of range:\n"))
    end: int = int(input("Enter end of range:\n"))
    # use (start-1), (end-1) because checking of each number starts from "2" but not "1"
    total_checks: int = ((end - 1) ** 2 + (end - 1)) / 2 - ((start - 1) ** 2 + (start - 1)) / 2 + (start - 1)
    thread_checks: float = total_checks / THREADS_NUMBER
    current_checks: float = thread_checks
    checks_counter = 0
    thread_start = thread_end = start
    while thread_end <= end:
        for i in range(start, end + 1):
            if checks_counter <= current_checks:
                checks_counter += i
                thread_end: int = thread_end + 1 if thread_end < end else end
            else:
                yield thread_start, thread_end
                current_checks += thread_checks
                thread_start = thread_end + 1


def get_primes(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    print(results)
    return results


def run_threads():
    interval: Generator = iter_number()
    arguments: list[tuple] = [next(interval) for i in range(THREADS_NUMBER)]  # create intervals for each thread
    threads: list[Thread] = [Thread(target=get_primes, args=argument) for argument in arguments]
    for thread in threads:
        thread.start()


def main():
    run_threads()


if __name__ == "__main__":
    main()
