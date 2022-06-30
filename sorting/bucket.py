def bucket_sort(arr):
    buckets = []

    for i in range(len(arr)):
        buckets.append([])
    for x in arr:
        b_index = int(x / 10)                 # input number issue
        buckets[b_index].append(x)
    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr


to_sort = [3, 2, 5, 26, 46, 75, 34, 1]
print("before sort ", end=" ")
print(to_sort)

bucket_sort(to_sort)
print("after sort accenting", end=" ")
print(to_sort)
