import random
import time


def insertionSort(array):
    n = len(array)
    if n <= 1:
        return
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def countSort(array):
    n = len(array)
    highest = array[0]
    for i in range(1, n):
        if highest < array[i]:
            highest = array[i]
    fr = [0 for x in range(highest + 1)]
    for i in range(0, n):
        fr[array[i]] += 1
    k = 0
    for i in range(len(fr)):
        for j in range(fr[i]):
            array[k] = i
            k += 1


def radixSort(arr):
    radix = 10
    buckets = [[] for i in range(radix)]
    max_length = False
    placement = 1
    while not max_length:
        max_length = True
        for i in arr:
            tmp = i // placement
            buckets[tmp % radix].append(i)
            if max_length and tmp > 0:
                max_length = False
        i = 0
        for bucket in buckets:
            for num in bucket:
                arr[i] = num
                i += 1
            bucket.clear()
        placement *= radix


def merge(arr1, arr2):
    arr3 = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    if i >= len(arr1):
        for k in range(j, len(arr2)):
            arr3.append(arr2[k])
    else:
        for k in range(i, len(arr1)):
            arr3.append(arr1[k])
    arr1.clear()
    for m in range(0, len(arr3)):
        arr1.append(arr3[m])


def mergeSort(arr):
    if len(arr) <= 1:
        return
    left = []
    right = []

    mid = len(arr) // 2
    for i in range(0, mid):
        left.append(arr[i])
    for i in range(mid, len(arr)):
        right.append(arr[i])

    mergeSort(left)
    mergeSort(right)
    merge(left, right)

    arr.clear()
    for i in range(0, len(left)):
        arr.append(left[i])


def shellSort(arr):
    interval = len(arr) // 2
    while interval > 0:
        for i in range(interval, len(arr)):
            aux = arr[i]
            j = i
            while j >= interval and arr[j - interval] > aux:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = aux
        interval = interval // 2


def is_Sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux


def counting_sort_16(v, base):
    aux = [0] * len(v)
    c = [0] * 65536
    for j in range(len(v)):
        c[(v[j] >> 16*base) & 65535] += 1
    for k in range(1, len(c)):
        c[k] += c[k - 1]
    for i in range(len(v) - 1, -1, -1):
        aux[c[(v[i] >> 16*base) & 65535] - 1] = v[i]
    c[(v[i] >> 16 * base) & 65535] -= 1
    for i in range(len(aux)):
        v[i] = aux[i]


def counting_sort_2_8(v, base):
    aux = [0] * len(v)
    c = [0] * 256
    for j in range(len(v)):
        c[(v[j] >> 8 * base) & 255] += 1
    for k in range(1, len(c)):
        c[k] += c[k-1]
    for i in range(len(v)-1, -1, -1):
        aux[c[(v[i] >> 8 * base) & 255] - 1] = v[i]
        c[(v[i] >> 8 * base) & 255] -= 1
    for i in range(len(aux)):
        v[i] = aux[i]


def radixSort_8(array):
    for i in range(0, 4):
        base = i
        counting_sort_2_8(array, base)


def radixSort_16(array):
    for i in range(0, 2):
        base = i
        counting_sort_16(array, base)


def nearly_sorted_numbers(N, Max):
    arrayTest = [random.randint(1, Max) for _ in range(N)]
    arrayTest.sort()
    for i in range(0, 20):
        arrayTest[random.randint(0, N - 1)], arrayTest[random.randint(0, N - 1)] = arrayTest[random.randint(0, N - 1)], arrayTest[random.randint(0, N - 1)]
    return arrayTest


sorts = ["insertionSort", "countSort", "radixSort", "mergeSort", "shellSort", "bubbleSort", "radixSort_8",
         "radixSort_16"]
N = 10**3
Max = 10**8
print("N = ", N, " Max = ", Max, ":")

arrayTest = [random.randint(1, Max) for _ in range(N)]
arrayTest.sort(reverse=True)
for sort in sorts:
    arrayAux = arrayTest.copy()
    sortFunction = globals()[sort]
    start = time.time()
    sortFunction(arrayAux)
    end = time.time()
    if is_Sorted(arrayAux):
        print("Sortare corecta", end - start, "seconds", sort)
    else:
        print("Sortare gresita ", sort)
start = time.time()
arrayTest.sort()
end = time.time()
if is_Sorted(arrayTest):
    print("Sortare corecta", end - start, "seconds", "Default Python Sort")
else:
    print("Sortare gresita", "Default Python Sort")




