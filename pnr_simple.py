def validate_personal_number(personal_number):
    """Return True if a 10-digit personal number has a valid Luhn checksum."""

    if len(personal_number) != 10 or not personal_number.isdigit():
        return False

    checksum = 0

    for position, digit in enumerate(personal_number[:-1]):
        value = int(digit)

        if position % 2 == 0:
            value *= 2
            if value > 9:
                value -= 9

        checksum += value

    expected_control_digit = (10 - checksum % 10) % 10
    return expected_control_digit == int(personal_number[-1])


print(validate_personal_number("9512245591"))  # False