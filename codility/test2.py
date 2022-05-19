from copy import deepcopy

def isAesthetic(tree):
    type = -1
    n = len(tree)
    if tree[0] < tree[1]:
        type = 0
    elif tree[0] > tree[1]:
        type = 1
    if type == -1:
        return False
    if type == 0:
        if n == 3:
            if tree[1] <= tree[2]:
                return False
        for i in range(2, n - 1,2):
            if tree[i - 1] > tree[i] and tree[i] < tree[i+1]:
                continue
            else:
                return False
    elif type == 1:
        if n == 3:
            if tree[1] >= tree[2]:
                return False
        for i in range(2, n-1, 2):
            if tree[i - 1] < tree[i] and tree[i] > tree[i + 1]:
                continue
            else:
                return False
    return True



def solution(A):
    # write your code in Python 3.6
    if isAesthetic(A):
        return 0
    n = len(A)
    result = 0
    for i in range(n):
        deleted_A = deepcopy(A)
        deleted_A.pop(i)
        aesthetic = isAesthetic(deleted_A)
        if aesthetic:
            result += 1
    if result == 0:
        return -1
    return result

ans = solution([3,4,5,3,7])
print(ans)