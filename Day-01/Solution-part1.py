def calibrate(string: str) -> int:
    string_length = len(string)
    first_digit = None
    last_digit = None

    i = 0
    while i < string_length:
        if first_digit is not None and last_digit is not None:
            break
        if first_digit is None and string[i].isdigit():
            first_digit = string[i]
        if last_digit is None and string[string_length - i - 1].isdigit():
            last_digit = string[string_length - i - 1]
        i += 1
    return int(first_digit + last_digit)


def calibrate_inputs() -> int:
    sum = 0
    with open("Day-01/input.txt") as file:
        while input := file.readline():
            output = calibrate(input)
            sum += output
        input = file.readline()
    return sum


print("Total sum:", calibrate_inputs())
