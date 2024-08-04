def square_numbers(numberSet):
    return {n ** 2 for n in numberSet}

numberSet = {1, 2, 3, 4, 5}
result = square_numbers(numberSet)
print(result)
