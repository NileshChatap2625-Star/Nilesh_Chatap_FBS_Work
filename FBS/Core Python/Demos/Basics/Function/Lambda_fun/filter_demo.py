## filter is used to filter value and it neglate vlaue of falsy, nonem, zero(0), false, [], ' '



data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = tuple(filter(lambda num: num % 2 == 0, data))
# res = tuple(filter(lambda num: num * num, data))

print(res)