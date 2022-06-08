import os
#####################################################################################################
def show_multilply_table(satr , soton):
    for i in range(1, satr + 1):
        for j in range(1, soton + 1):
            print(i * j , end='\t')
        print()

####################################################################################################
os.system("cls")
print("\n welcome\n")
while True :
    while True:
        satr=int(input(" lotfan tedad satr hai jadval ra vared konid : "))
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
    show_multilply_table (satr , soton)