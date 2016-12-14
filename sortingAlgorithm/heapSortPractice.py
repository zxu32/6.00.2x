# heapsort
import random as rand


def maxHeapify(aList, i, heapSize):
    left = i * 2 + 1  # index of left node
    right = left + 1  # index of right node
    if left <= heapSize-1 and aList[left] > aList[i]:
        largest = left  # index of largest value
    else:
        largest = i
    if right <= heapSize-1 and aList[right] > aList[largest]:
        largest = right
    if i != largest:
        aList[i], aList[largest] = aList[largest], aList[i]
        # swap the values of the heap
        # index of largest stays the same
        maxHeapify(aList, largest, heapSize)


def buildMaxHeap(aList, heapSize):
    for i in range(heapSize//2-1, -1, -1):  # range(start, end, step)
        maxHeapify(aList, i, heapSize)


def heapSort(aList, heapSize):
    buildMaxHeap(aList, heapSize)
    for i in range(len(aList)-1, 0, -1):
        # print(i)
        (aList[0], aList[i]) = (aList[i], aList[0])
        heapSize -= 1
        maxHeapify(aList, 0, heapSize)

if __name__ == "__main__":
    l1 = [rand.randint(0, 1000) for i in range(0, 100)]
    print(l1)
    heapSort(l1, len(l1))
    print(l1)
