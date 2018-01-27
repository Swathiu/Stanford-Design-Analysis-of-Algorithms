def MergeSort(arr,low,high):  #low =0
    
    if low < high :    
        mid = int((low + (high - 1))/2)
        print ("MergeSort - Low - %d, Mid - %d, High = %d" %(low,mid,high))
        MergeSort (arr,int(low),int(mid))
        MergeSort (arr,int(mid+1),int(high))

        Merge(arr,int(low),int(mid),int(high))

def Merge(arr,low,mid,high):
    print ("Merge - Low - %d, Mid - %d, High = %d" %(low,mid,high))
    print ("Array - ", arr)
    n1 = mid - low + 1
    n2 = high - mid

    LeftArr = []
    RightArr = []
    
    LeftArr = [None] * (n1)
    RightArr = [None] * (n2)

    for i in range(0,n1):
        LeftArr[i] = arr[int(low) + i]

    for j in range(0,n2):
        RightArr[j] = arr[int(mid) + j + 1]

    i=0
    j=0
    k=low

    while i < n1 and j < n2:
        if LeftArr[i] <= RightArr[j]:
            arr[k] = LeftArr[i]
            i += 1
        else:
            arr[k] = RightArr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = LeftArr[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = RightArr[j]
        k += 1
        j += 1


arr = [34,56,23,12,9,7]
size = len(arr)
MergeSort(arr,0,size-1)
for i in range (0,size):
    print ("%d" %arr[i])
