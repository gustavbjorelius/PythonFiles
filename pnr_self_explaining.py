# https://bth.instructure.com/courses/7266/assignments/66779?module_item_id=257399

def calculate_digit_value(digit, should_double):
    """Return a digit's value according to the Luhn algorithm."""

    digit_value = int(digit)

    if should_double:
        digit_value *= 2

        # 18 becomes 9, equivalent to adding 1 + 8
        # 11 becomes 2, eq to 1 + 1
        # 10 becomes 1, eq to 1 + 0
        if digit_value > 9:
            digit_value -= 9

    return digit_value

def validate_personal_number(personal_number):
    """Return True if a 10-digit Swedish personal number is valid."""

    # A valid input must contain exactly 10 digits: YYMMDDXXXX
    if len(personal_number) != 10 or not personal_number.isdigit():
        return False

    digits_to_check = personal_number[:-1]
    provided_control_digit = int(personal_number[-1])

    checksum = 0

    for position, digit in enumerate(digits_to_check):
        should_double = position % 2 == 0
        checksum += calculate_digit_value(digit, should_double)

    # Calculate the digit needed to reach the next multiple of 10
    expected_control_digit = (10 - checksum % 10) % 10

    return expected_control_digit == provided_control_digit

print(validate_personal_number("9512245591"))