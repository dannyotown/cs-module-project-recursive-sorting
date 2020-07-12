# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    arrC = []
    # Your code here
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            arrC.append(arrB[0])
            arrB.pop(0)
        else:
            arrC.append(arrA[0])
            arrA.pop(0)
    while len(arrA) > 0:
        arrC.append(arrA[0])
        arrA.pop(0)
    while len(arrB) > 0:
        arrC.append(arrB[0])
        arrB.pop(0)
    return arrC


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        M = len(arr)//2
        L = arr[:M]
        R = arr[M:]
        return merge(merge_sort(L), merge_sort(R))
    else:
        return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
print(merge_sort([2, 4, 3, 7, 6, 8, 10, 5]))


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
