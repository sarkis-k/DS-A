def insertion_sort_a(arr):
    # accenting order
    for i in range(len(arr)):
        cur_elem = arr[i]
        pos = i
        while cur_elem < arr[i - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = cur_elem


def insertion_sort_d(arr):
    # descending order
    for i in range(len(arr)):
        cur_elem = arr[i]
        pos = i
        while cur_elem > arr[i - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = cur_elem


to_sort = [3, 2, 5, 26, 46, 675, 234, 1]
print("before sort ", end=" ")
print(to_sort)

insertion_sort_a(to_sort)
print("after sort accenting", end=" ")
print(to_sort)

insertion_sort_d(to_sort)
print("after sort descending", end=" ")
print(to_sort)
