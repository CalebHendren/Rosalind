def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n, m = map(int, input().split())
A = list(map(int, input().split()))
keys = list(map(int, input().split()))

result = []
for key in keys:
    index = binary_search(A, key)
    result.append(str(index))

print(" ".join(result))