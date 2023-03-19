def merge_sort_and_count_inversions(arr):
    if len(arr) == 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort_and_count_inversions(arr[:mid])
    right, inv_right = merge_sort_and_count_inversions(arr[mid:])
    merged, inv_split = merge_and_count_split_inversions(left, right)
    return merged, inv_left + inv_right + inv_split

def merge_and_count_split_inversions(left, right):
    i, j = 0, 0
    merged = []
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, count

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    _, inversions = merge_sort_and_count_inversions(arr)
    print(inversions)
