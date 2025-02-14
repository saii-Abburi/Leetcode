def mergesort(arr , low , high):
    if (low>=high):
        return
    mid = (low+high)//2
    mergesort(arr , low , mid)
    mergesort(arr , mid+1 , high)
    merge(arr , low , mid , high)

def merge(a , low , mid , high):
    ans = []
    l = low
    r = mid+1
    while l<=mid and r<=high:
        if(a[l]<a[r]):
            ans.append(a[l])
            l+=1
        else:
            ans.append(a[r])
            r+=1
    while (l<=mid):
        ans.append(a[l])
        l+=1
    while(r<=high):
        ans.append(a[r])
        r+=1
    for i in range(low , high+1):
        arr[i] = ans[i-low]


arr = [3,1,2,4,1,5,2,6,4]
low = 0
high = len(arr)-1
mergesort(arr , low , high)
print(arr)