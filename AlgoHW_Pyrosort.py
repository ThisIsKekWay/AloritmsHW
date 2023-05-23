import random

def heapMaker (lst, size, rootCoord):
    mxm = rootCoord
    leftChild = 2 * rootCoord + 1
    rightChild = 2 * rootCoord + 2

    if leftChild < size and lst[leftChild] > lst[mxm]:
        mxm = leftChild

    if rightChild < size and lst[rightChild] > lst[mxm]:
        mxm = rightChild

    if mxm != rootCoord:
        lst[rootCoord], lst[mxm] = lst[mxm], lst[rootCoord]

        heapMaker(lst, size, mxm)


def sort (lst):
    for i in range(len(lst) - 1, -1, -1):
        heapMaker(lst, len(lst), i)

    for i in range(len(lst) - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]

        heapMaker(lst, i, 0)


lst = [random.randint(0, 51) for _ in range(20)]
print(lst)
sort(lst)
print(lst)