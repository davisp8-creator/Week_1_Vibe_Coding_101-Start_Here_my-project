def median(numbers):
    if not numbers:
        raise ValueError("median() arg is an empty sequence")

    values = sorted(numbers)
    n = len(values)
    mid = n // 2

    if n % 2 == 1:
        return values[mid]
    return (values[mid - 1] + values[mid]) / 2
