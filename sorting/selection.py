def selection_sort_a(arr):
    # accenting order
    for i in range(len(arr)):
        min_val = min(arr[i:])
        min_ind = arr.index(min_val)
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


def selection_sort_d(arr):
    # descending order
    for i in range(len(arr)):
        max_val = max(arr[i:])
        max_ind = arr.index(max_val)
        arr[i], arr[max_ind] = arr[max_ind], arr[i]


to_sort = [3, 2, 5, 26, 46, 675, 234, 1]
print("before sort ", end=" ")
print(to_sort)

selection_sort_a(to_sort)
print("after sort accenting", end=" ")
print(to_sort)

selection_sort_d(to_sort)
print("after sort descending", end=" ")
print(to_sort)
