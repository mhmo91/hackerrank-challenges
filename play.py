# i'm an empty file that Mo uses to play!


def solution(A):
    hashMap = {}
    for num in A:
        if num not in hashMap.keys():
            hashMap[num] = True
    return len(hashMap)


print(solution([2, 1, 1, 2, 3, 1]))
