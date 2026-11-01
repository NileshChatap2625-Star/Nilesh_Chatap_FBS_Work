numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 10

pairs = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.add((numbers[i], numbers[j]))

print("Pairs of numbers that add up to", target, "are:", pairs)