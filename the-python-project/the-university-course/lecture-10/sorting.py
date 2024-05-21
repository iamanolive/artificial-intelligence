d = {"a": 10, "c": 22, "b": 1}
print(d.items())
print(sorted(d.items()))
print(d.items())

t = sorted(d.items())
print(t)

for k, v in sorted(d.items()):
    print(k, v)

c = {"a": 10, "b": 1, "c": 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse = True)
print(tmp)