# the Newtons Sqrt method states that the sqrt of a num is found by using the formula 
#  root = (x+(n/x))/2
# By following the 3 steps:
#  Assign the x = n
#  if the error = |root - x| < 1 or precision value root is found 
#  assgin x = root
#  time complexity = O(log(n)f(n))

def sqrt(num):
    x = num
    root = 0
    while True:
        root = 0.5*(x+(num/x))
        if abs(root-x)<0.1:
            return root
        x = root


num = 40
print(sqrt(num))
