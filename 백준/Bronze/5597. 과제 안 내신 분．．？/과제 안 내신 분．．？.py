num = [i for i in range(1,31)]

for j in range(28):
  data = int(input())
  num.remove(data)
print(min(num))
print(max(num))