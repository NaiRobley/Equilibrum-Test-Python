def solution(A):
    sum1 = 0
    sum2 = sum(A)
    for i in range(len(A)):
        sum2 -= A[i]
        if sum1 == sum2:
            return i
        sum1 += A[i]
    return -1
