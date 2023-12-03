from functools import reduce
import re


def extract_calibration_value(x: int, y: str):
    numbers = re.sub(r"\D", "", y)
    return x + int(numbers[0] + numbers[-1])

def extract_calibration_value_b(x: int, y: str):
    numbers = re.sub(r"one", "o1e", y)
    numbers = re.sub(r"two", "t2o", numbers)
    numbers = re.sub(r"three", "t3e", numbers)
    numbers = re.sub(r"four", "f4r", numbers)
    numbers = re.sub(r"five", "f5e", numbers)
    numbers = re.sub(r"six", "s6x", numbers)
    numbers = re.sub(r"seven", "s7n", numbers)
    numbers = re.sub(r"eight", "e8t", numbers)
    numbers = re.sub(r"nine", "n9e", numbers)
    # numbers = re.sub(r"zero", "0", numbers)
    numbers = re.sub(r"\D", "", numbers)
    return x + int(numbers[0] + numbers[-1])


if __name__ == "__main__":
    print(__file__)
    day = __file__.split("\\")[-1].split(".")[0]
    with open(f"./inputs/{day}.txt") as f:
        my_string = f.read().strip()

    calibration_value = reduce(extract_calibration_value, my_string.split("\n"), 0)
    print(calibration_value)

    calibration_value_b = reduce(extract_calibration_value_b, my_string.split("\n"), 0)
    print(calibration_value_b)
