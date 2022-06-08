import os
#####################################################################################################
def multiplication_table(satr , soton):

    for i in range(satr):
        for j in range(soton):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('#', end=' ')
                else:
                    print('*', end=' ')
            else:
                if j % 2 == 0:
                    print('*', end=' ')
                else:
                    print('#', end=' ')
        print()
#####################################################################################################
os.system("cls")
print ("welcome")
while True :
    while True:
        satr=int(input("\n lotfan tedad satr hai jadval ra vared konid : "))
        if satr <= 0 : 
            print ("lotfan adadi bozorg tar az 0 vared konid ")
        else :
            break   
    while True :            
        soton=int(input(" \n lotfan tedad soton hai jadval ra vared konid : "))
        if soton <= 0 : 
            print ("lotfan adadi bozorg tar az 0 vared konid ")
        else :
            break 
    multiplication_table(satr , soton)