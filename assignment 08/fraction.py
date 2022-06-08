import math
from typing import SupportsAbs

def show_menu():
    print("welcome to Fraction calculator :)\n")
    print("1-jam \n")
    print("2-tafrigh \n")
    print("3-zarb \n")
    print("4-taghsim \n")
    print("5-sade sazi kasr \n")
    print("6-exit \n")
##########################################      GET NUMBER     ##################################################
def Get_Fraction_Number():
    sorat = int(input('lotfan sorat kasr ra vared konid :'))
    while True :
        makhraj = int(input('lotfan makhraj kasr ra vared konid :'))
        if  makhraj != 0:
            break
        else :
            print("0 dar makhraj gheir mojaze \n")
    return sorat , makhraj
########################################    CLASS FARCTION    ############################################################
class Fraction :
    def __init__(self , sorat=0 , makhraj=1) :
       self.s =  sorat
       self.m = makhraj 

    def show(self):
        print(str("Fraction : ", self.s ,  "/" ,self.m ,"\n" ))

    def __mul__(self , y):
        sorat=self.s * y.s
        makhraj=self.m * y.m
        return Fraction(sorat , makhraj)

    def __sub__(self , y) :
        if(self.m == y.m):
            sorat = self.s - y.s
            return Fraction(sorat , self.m )
        else:
            sorat = (self.s * y.m) - (y.s * self.m)
            return Fraction(sorat , self.m * y.m)

    def __add__(self , y) :
        if(self.m == y.m):
            sorat = self.s + y.s
            return Fraction(sorat , self.m )
        else:
            sorat = (self.s * y.m) + (y.s * self.m)
            return Fraction(sorat , self.m * y.m)

    def __truediv__(self , y) :
        sorat = (self.s * y.m )
        makhraj =(self.m * y.s)
        return Fraction(sorat  , makhraj)

    def simplify(self): 
        gcd = math.gcd(self.s, self.m) 
        if(gcd != 0 ) :
            self.s = self.s//gcd
            self.m = self.m//gcd 
    
    def __str__(self):
        return str(self.s) +  "/" + str(self.m)
#######################################    MAIN    #############################################################
while True :
    show_menu()
    gozine = ''
    try:
        gozine = int(input('lotfan gozine mored nazar ra vared konid : '))
    except:
        print('ebarat vared shode motabar nist ، lotfan shomare gozine ra vared konid : ')
             
    if gozine == 1:
        print("\n kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = Fraction(s1 , m1)
        print("\n kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = Fraction(s2 , m2)
        print("hasel : " , num1+num2 , "\n")

    elif gozine == 2:
        print("\n kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = Fraction(s1 , m1)
        print("\n kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = Fraction(s2 , m2)
        print("hasel : " , num1-num2 , "\n")

    elif gozine == 3:
        print("\n kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = Fraction(s1 , m1)
        print("\n kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = Fraction(s2 , m2)
        print("hasel : " , num1*num2 , "\n")

    elif gozine == 4:
        print("\n kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = Fraction(s1 , m1)
        print("\n kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = Fraction(s2 , m2)
        print("hasel : " , num1/num2 , "\n")

    elif gozine == 5:             
        s1 , m1 = Get_Fraction_Number()
        kasr_1 = Fraction(s1 , m1)
        kasr_1.simplify()
        print("result : " ,kasr_1 )     

    elif gozine == 6:
       break   
    else : 
        print("lotfan adadi bein 1 - 6 vared konid \n ")  
    input("\nPress ENTER to continue...\n")    
print('goodbye ;) \n')