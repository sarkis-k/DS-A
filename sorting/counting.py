def counting_sort_a(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[arr[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(0, size):
        arr[i] = output[i]


arr1 = [4, 2, 2, 8, 3, 3, 1]
print("before sort ", end=" ")
print(arr1)

counting_sort_a(arr1)
print("after sort accenting", end=" ")
print(arr1)

