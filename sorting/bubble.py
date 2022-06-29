def bubble_sort_a(arr):
    # accenting order
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_d(arr):
    # descending order
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


to_sort = [3, 2, 5, 26, 46, 675, 234, 1]
print("before sort ", end=" ")
print(to_sort)

bubble_sort_a(to_sort)
print("after sort accenting", end=" ")
print(to_sort)

bubble_sort_d(to_sort)
print("after sort descending", end=" ")
print(to_sort)
