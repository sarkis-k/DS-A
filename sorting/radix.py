def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr):
    max_elem = max(arr)
    place = 1
    while max_elem // place > 0:
        counting_sort(arr, place)
        place *= 10


to_sort = [3, 2, 5, 26, 46, 675, 234, 1]
print("before sort ", end=" ")
print(to_sort)

radix_sort(to_sort)
print("after sort accenting", end=" ")
print(to_sort)
