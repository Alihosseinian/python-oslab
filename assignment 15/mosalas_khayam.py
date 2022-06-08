def Pascal(n): 
    array=[]
    for line in range(1, n + 1): 
        x = 1 
        temp = []
        for i in range(1, line + 1): 
            temp.append(x)
            x = int(x * (line - i) / i) 
        array.append(temp)
    for i in range(n):
        for j in range(len(array[i])):
            print  ( array[i][j] , end="\t" )
        print()

n = int(input("lotfan adad khod ra vared konid : ")) 
Pascal(n)
