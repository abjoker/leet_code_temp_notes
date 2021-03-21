```
Three way partioning
```

def sort_arr(A, N):
    start = 0
    end = N
    index = 0

    while index <= end:
        if A[index] == 0:
            A[index], A[start] = A[start], A[index]
            start += 1
            index += 1
        elif A[index] == 2:
            A[index], A[end] = A[end], A[index]
            end -= 1
        else:
            index += 1

    return A
  
 print(sort_arr([2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
