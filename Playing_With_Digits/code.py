def dig_pow(n, p):
    n_str = str(n)
    sum = 0
    for digit in n_str:
        digit = int(digit)
        sum += digit ** p
        p += 1

    if not sum % n:
        return int(sum / n)
    return -1