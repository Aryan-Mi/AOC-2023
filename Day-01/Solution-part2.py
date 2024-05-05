def match_input(i: int, string: str, string_length: int):
    if string[i].isdigit():
        return string[i]
    if (i + 3) <= string_length:
        text_number = string[i : i + 3]
        match text_number:
            case "one":
                return "1"
            case "two":
                return "2"
            case "six":
                return "6"
    if (i + 4) <= string_length:
        text_number = string[i : i + 4]
        match text_number:
            case "four":
                return "4"
            case "five":
                return "5"
            case "nine":
                return "9"
    if (i + 5) <= string_length:
        text_number = string[i : i + 5]
        match text_number:
            case "three":
                return "3"
            case "seven":
                return "7"
            case "eight":
                return "8"
    else:
        return None


def calibrate(string: str) -> int:
    string_length = len(string)
    first_digit = None
    last_digit = None

    i = 0
    while i < string_length:
        matched = match_input(i, string, string_length)
        if matched is not None:
            if first_digit is None:
                first_digit = matched
            last_digit = matched
        i += 1
    return int(first_digit + last_digit)


def calibrate_input() -> int:
    sum = 0
    with open("Day-01/input.txt") as file:
        while input := file.readline():
            output = calibrate(input)
            sum += output
        input = file.readline()
    return sum


# print("Total sum:", calibrate("4nineeightseven2"))
print("Part 2 total sum:", calibrate_input())
