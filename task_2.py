import re


from typing import Callable


# Generator which search for pattern matches in a string (floats and integers in this case)
def generator_numbers(text: str):
    pattern = r'(?<!\S)\d+[\.,]?\d*(?!\S)'

    for match in re.finditer(pattern, text):
        yield float(match.group(0))


# Sum numbers obtained from the generator
def sum_profit(text: str, func: Callable):
    return sum(func(text))


# Example usage 
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

assert total_income == 1351.46
