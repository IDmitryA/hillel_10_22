import functools


# MODIFIED DECORATOR:
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if isinstance(func(*args, **kwargs), str):
            return func(*args, **kwargs)[::-1]
        else:
            return None

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUTPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
