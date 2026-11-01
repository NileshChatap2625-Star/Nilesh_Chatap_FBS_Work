strings = ["flower", "flow", "flight"]

prefixes = set()

for string in strings:
    for i in range(1, len(string) + 1):
        prefixes.add(string[:i])

common = []

for prefix in prefixes:
    if all(string.startswith(prefix) for string in strings):
        common.append(prefix)

if common:
    longest = max(common, key=len)
else:
    longest = ""

print("Longest Common Prefix:", longest)