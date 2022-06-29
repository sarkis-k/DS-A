def pivot_point_a(arr, first, last):
    # accenting order
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right


def pivot_point_d(arr, first, last):
    # descending order
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] >= pivot:
            left += 1
        while left <= right and arr[right] <= pivot:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right


def quick_sort_a(arr, first, last):
    if first < last:
        p = pivot_point_a(arr, first, last)
        quick_sort_a(arr, first, p - 1)
        quick_sort_a(arr, p + 1, last)


def quick_sort_d(arr, first, last):
    if first < last:
        p = pivot_point_d(arr, first, last)
        quick_sort_d(arr, first, p - 1)
        quick_sort_d(arr, p + 1, last)


to_sort = [3, 2, 5, 26, 46, 675, 234, 1]
start = 0
end = len(to_sort) - 1
print("before sort ", end=" ")
print(to_sort)

quick_sort_a(to_sort, start, end)
print("after sort accenting", end=" ")
print(to_sort)

quick_sort_d(to_sort, start, end)
print("after sort descending", end=" ")
print(to_sort)
