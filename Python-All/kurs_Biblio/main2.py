a = (1, 2, 3)
b = (4, 5, 6)

l = [*a, *b]

print(l)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "d": 4}
df = {**d1, **d2}
print(df)
