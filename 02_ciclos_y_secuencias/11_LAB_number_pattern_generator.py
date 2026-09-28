def number_pattern(n):
    numbers = []
    if type(n) != int:
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    for num in range(1, n + 1):
        numbers.append(str(num))
    return " ".join(numbers)
