no_of_inversions = 0

def ArrayInvert(arr,low,high):  #low =0
    
    if low < high :    
        mid = int((low + (high - 1))/2)
        ArrayInvert (arr,int(low),int(mid))
        ArrayInvert (arr,int(mid+1),int(high))

        Merge(arr,int(low),int(mid),int(high))

def Merge(arr,low,mid,high):
    global no_of_inversions
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

    len_LeftArr = len(LeftArr)
    i=0
    j=0
    k=low

    while i < n1 and j < n2:
        if LeftArr[i] <= RightArr[j]:
            arr[k] = LeftArr[i]
            i += 1
        else:
            arr[k] = RightArr[j]
            no_of_inversions = no_of_inversions + len_LeftArr - i
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


arr = [1,3,5,2,4,6]
size = len(arr)
ArrayInvert(arr,0,size-1)
for i in range (0,size):
    print ("%d" %arr[i])
print ("No. of Split Inversions is - ",no_of_inversions)
