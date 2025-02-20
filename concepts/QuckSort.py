def quicksort(arr , low , high):
    if(low<high):
        pind = partition(arr , low , high)
        quicksort(arr , low , pind-1)
        quicksort(arr , pind+1 , high)

def partition(arr , low , high):
    pivot = arr[low]
    i = low 
    j = high
    while(i<j):
        while(arr[i]<=pivot and i<=high):
            i+=1
        while(arr[j]>pivot and j>=low):
            j-=1
        if(i<j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    arr[low] , arr[j] = arr[j] , arr[low]
    return j



arr = [3,1,2,4,1,5,2,6,4]
low = 0
high = len(arr)-1
quicksort(arr , low , high)
print(arr)