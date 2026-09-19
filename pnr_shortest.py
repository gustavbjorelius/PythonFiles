def validate_personal_number(personal_number):
    """Return True if a 10-digit personal number has a valid Luhn checksum."""

    if len(personal_number) != 10 or not personal_number.isdigit():
        return False

    checksum = 0

    for position, digit in enumerate(map(int, personal_number)):
                        
        value = digit * (2 if position % 2 == 0 else 1)
        checksum += value // 10 + value % 10

    return checksum % 10 == 0

print(validate_personal_number('9512245591'))