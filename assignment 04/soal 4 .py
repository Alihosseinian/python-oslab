import os
#####################################################################################################
def fibonacci(num):
    if num<= len(FibArray):
        return FibArray[num-1]
    else:
        temp_fib = fibonacci(num-1)+fibonacci(num-2)
        FibArray.append(temp_fib)
        return temp_fib
#####################################################################################################
os.system("cls")
print ("welcome")	
FibArray = [0, 1]
while True :
    while True:
        num=int(input("\n lotfan adad mored nazar ra vared konid : "))
        if num < 0 : 
            print ("lotfan adadi bozorg tar az 0 vared konid ")
        else :
            break   
    print("\n" ,fibonacci(num+1))

