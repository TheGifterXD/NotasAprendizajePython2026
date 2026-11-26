def square_root_bisection(num, tolerance=0.01, max_iterations=10):

    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if num == 0 or num == 1:
        print(f'The square root of {num} is {num}')
        return num

    low = 0
    high = 1
    if num > 1:
        high = num
    
    for num_of_iterations in range(max_iterations):
        mid = (low + high) / 2
    
        if high - low <= tolerance or mid ** 2 == num:
            print(f'The square root of {num} is approximately {mid}')
            return mid

        if mid ** 2 < num:
            low = mid
        elif mid ** 2 > num:
            high = mid

    print(f'Failed to converge within {max_iterations} iterations')
    return None
