def spiralize(number):
    d = (number - 1) // 2
    return (16 * d * d * d + 30 * d * d + 26 * d + 3) // 3
