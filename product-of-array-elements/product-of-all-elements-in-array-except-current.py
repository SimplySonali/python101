def pdtArray(arr):
    bigpdt = 1
    arrb=[]
    zexist = 0
    for i in range(len(arr)):
        if arr[i] == 0 :
            zexist = 1
            pass
        bigpdt = bigpdt * arr[i]
    print (bigpdt)
    for j in range(len(arr)):
        if zexist == 1 and arr[j] != 0 :
            num = 0
        elif arr[j] == 0:
            num = "Infinite"
        else:
           num = bigpdt//arr[j]
        print (num)
        arrb.append(num)
    return arrb

if __name__ == "__main__" :
    arr = [2,4,6,3]
    print (pdtArray(arr))
