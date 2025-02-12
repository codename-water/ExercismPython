def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors_sum = 0
    for i in range(1, number):
        if not number % i:
            factors_sum += i

    if factors_sum == number:
        return 'perfect'
    elif factors_sum > number:
        return 'abundant'
    else:
        return 'deficient'
