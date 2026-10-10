def max(numbers):
    kandidat = numbers[0]
    for number in numbers[1:]:
       if kandidat < number:
           kandidat = number

    return kandidat

numbers = [ 72, 9, -14, 25, -101, -61, 33]
highest = max(numbers)

print(highest)
