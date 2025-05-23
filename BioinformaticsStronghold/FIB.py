n, k = map(int, input().split())
a, b = 1, 1
for _ in range(2, n):
    a, b = b, b + k * a
print(b)