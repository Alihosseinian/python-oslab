##################################### SHOW MENU ##################################################
def show_menu():
    print("welcome to calculator :)\n")
    print("1-jam :\n")
    print("2-tafrigh :\n")
    print("3-zarb :\n")
    print("4-taghsim :\n")
    print("5-exit:\n")
#####################################  CLASS (OOP) #######################################################
class Kasr :
    def __init__(self , s , m ) :
       self.sorat=s
       self.makhraj=m
    ##################################### jam 2 kasr #####################################################  
        
    def __add__(self , kasr ):
        if(self.makhraj == kasr.makhraj):
            Fraction = self.sorat + kasr.sorat
            return Kasr(Fraction , self.makhraj )
        else:
            Fraction = (self.sorat * kasr.makhraj) + (kasr.sorat * self.makhraj)
            return Kasr(Fraction , self.makhraj * kasr.makhraj)
   
    ##################################### tafrigh 2 kasr ################################################## 

    def __sub__(self , kasr ):
        if(self.makhraj == kasr.makhraj):
            Fraction = self.sorat - kasr.sorat
            return Kasr(Fraction , self.makhraj )
        else:
            Fraction = (self.sorat * kasr.makhraj) - (kasr.sorat * self.makhraj)
            return Kasr(Fraction , self.makhraj * kasr.makhraj)

    ##################################### zarb 2 kasr #####################################################

    def __mul__(self , kasr):
        Fraction_sorat = (self.sorat * kasr.sorat)
        Fraction_makhraj =(self.makhraj * kasr.makhraj)
        return Kasr(Fraction_sorat , Fraction_makhraj)

    ##################################### taghsim 2 kasr ##################################################

    def __truediv__(self ,kasr):
        Fraction_sorat = (self.sorat * kasr.makhraj)
        Fraction_makhraj =(self.makhraj * kasr.sorat)
        return Kasr(Fraction_sorat , Fraction_makhraj)

    #######################################################################################################

    def __str__(self):
        return  str(self.sorat)+ '/' + str(self.makhraj)

##################################### load_data ############################################################

def load_data():

    kasr1_sorat = int(input('lotfan soart kasr ra vared konid :'))

    while True :
        kasr1_makhraj = int(input('lotfan makhraj kasr ra vared konid :'))
        if kasr1_makhraj != 0:
            break
        else :
            print("kasr ba makhraj 0 tarif nashodas lotfan adadi gheir 0 vared konid \n")

    return kasr1_sorat , kasr1_makhraj   
##################################### MAIN ############################################################ 
while True :
    s,m=load_data()
    F1=Kasr(s,m)
    s,m=load_data()
    F2=Kasr(s,m)    
    show_menu()
    choise=int(input("lotfan amaliat mored nazar ra entekhab konid :"))
    if choise == 1 :
        print("hasel : " , F1+F2)
    elif choise == 2 :
        print("hasel : " , F1-F2)
    elif choise == 3 :
        print("hasel : " , F1*F2)
    elif choise == 4 :
       print("hasel : " , F1/F2)
    elif choise == 7 : 
        break 
print("goodbye :)\n\n")
         
