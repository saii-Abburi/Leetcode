def sqrt(num , prec):
    st = 0
    end = num
    incr = 0.1
    while st<=end:
        mid = (st+end)//2
        if mid*mid== num:
            return mid
        elif mid*mid>num:
            end = mid-1
        else:
            st = mid+1
    root = end
    for i in range(prec):
        while root*root<=num:
            root+=incr
        root-=incr
        incr = incr/10
    return root

num = 46
root  =sqrt(num , 3)
print(round(root , 2))
