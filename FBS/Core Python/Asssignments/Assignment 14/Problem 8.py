strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in strings:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print("Anagram Groups:")

for group in groups.values():
    print(group)