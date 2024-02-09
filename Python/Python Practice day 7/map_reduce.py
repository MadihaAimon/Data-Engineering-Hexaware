data = [1, 2, 3, 4, 5]
result1 = map(lambda x: x * 2, data)


result2 = filter(lambda x: x % 2 == 0, data)

print(result1)
print(result2)