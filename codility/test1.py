def Sort(arr1, arr2):
    n = len(arr1)
    for i in range(n):
        for j in range(0, n- i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
            elif arr1[j] == arr1[j + 1]:
                if arr2[j] > arr2[j + 1]:
                    arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]

def solution(D, C, P):
    # write your code in Python 3.6
    Sort(D, C)
    n = len(D)
    powSum = 0
    for i in range(n):
        powSum += C[i]
        if powSum > P:
            c = i
    if powSum <= P:
        c = n
    return c

ans = solution([11,18,1], [9,18,8], 7)
print(ans)