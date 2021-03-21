def obtain_pivot(A, start, end):
    # if just one element
    if start == end:
        return A[start]

    while start <= end:
        mid = (start + end) // 2

        if start == end:
            return A[start]
        elif start + 1 == end:
            return max(A[start], A[end])
        elif A[mid-1] <= A[mid] >= A[mid+1]:
            return A[mid]
        elif A[mid-1] <= A[mid] <= A[mid+1]:
            start = mid + 1
        else:
            end = mid - 1


def get_peak(A):
    start = 0
    end = len(A) - 1
    peak = obtain_pivot(A, start, end)
    return peak


print(get_peak([1,1,1]))     
print(get_peak([1, 2, 3]))   
print(get_peak([1,2,3,5,3,2,1]))
print(get_peak([2,5,3,2,1]))
