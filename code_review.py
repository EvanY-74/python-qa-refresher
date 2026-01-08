def average(numbers):
    if len(numbers) == 0:
        raise ValueError('numbers list cannot be empty')
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
