def validate_personal_number(personal_number):
    """Return True if a 10-digit personal number has a valid Luhn checksum."""

    if len(personal_number) != 10 or not personal_number.isdigit():
        return False

    checksum = sum(
        value * 2 - 9 if position % 2 == 0 and value * 2 > 9
        else value * 2 if position % 2 == 0
        else value
        for position, value in enumerate(map(int, personal_number[:-1]))
    )

    return (10 - checksum % 10) % 10 == int(personal_number[-1])

print(validate_personal_number('9512245591'))