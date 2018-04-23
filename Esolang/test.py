from twice_linear import dbl_linear

def snail(array):
    rarray = []
    h = len(array)
    w = len(array[0])
    counter = h * w
    flag = 0
    add = 1
    up_h = h-1
    up_w = w-1
    down_h = 1
    down_w = 0
    i = 0
    j = 0
    while counter!=0:
        if flag==0:
            while j<=up_w:
                rarray.append(array[i][j])
                j+=add
                counter-=1
            j-=add
            i+=add
            while i<=up_h:
                rarray.append(array[i][j])
                i+=add
                counter-=1
            i-=add
            add = -1
            j+=add
            up_h-=1
            up_w-=1
        if flag==1:
            while j>=down_w:
                rarray.append(array[i][j])
                j+=add
                counter-=1
            j-=add
            i+=add
            while i>=down_h:
                rarray.append(array[i][j])
                i+=add
                counter-=1
            i-=add
            add = 1
            j+=add
            down_h+=1
            down_w+=1
        flag+=1
        flag%=2
    return rarray

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))

print(__name__)
dbl_linear(3)