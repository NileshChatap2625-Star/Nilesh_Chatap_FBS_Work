numbers = [1, 2, 3, 4, 5, 6]
target = 10

combinations = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                combination = tuple(sorted((numbers[i], numbers[j], numbers[k])))
                combinations.add(combination)

print("Unique Combinations:")

for combination in combinations:
    print(combination)