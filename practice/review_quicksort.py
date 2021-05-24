def my_quick_sort(S, a, b):
    if a >= b: return

    pivot = S[b]
    left = a
    right = b -1

    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and S[right] > pivot:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
    S[b],S[left] = S[left], S[b]

    my_quick_sort(S, a, left -1 )
    my_quick_sort(S, left + 1, b)


temp = [5, 2, 1, 3, 6, 9]

my_quick_sort(temp, 0, len(temp) - 1)
print(temp)
    