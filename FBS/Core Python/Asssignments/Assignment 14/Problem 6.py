numbers = [-10, -5, 2, 3, 8, 9]

unique_numbers = set(numbers)

numbers = list(unique_numbers)

max_product = numbers[0] * numbers[1]
pair = (numbers[0], numbers[1])

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]

        if product > max_product:
            max_product = product
            pair = (numbers[i], numbers[j])

print("Numbers:", pair)
print("Maximum Product:", max_product)