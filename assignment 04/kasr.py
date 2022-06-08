import os
import math


def show_menu():
    print("welcome to calculator :)\n")
    print("1-jam \n")
    print("2-tafrigh \n")
    print("3-zarb \n")
    print("4-taghsim \n")
    print("5-sade sazi kasr \n")
    print("6-exit \n")
###########################################################################################################
def Get_Fraction_Number():
    sorat = int(input('lotfan sorat kasr ra vared konid :'))
    while True :
        makhraj = int(input('lotfan makhraj kasr ra vared konid :'))
        if  makhraj != 0:
            break
        else :
            print("0 dar makhraj gheir mojaze \n")
    return sorat , makhraj
###########################################################################################################
class fraction :
    def __init__(self , sorat=0 , makhraj=1) :
       self.s =  sorat
       self.m = makhraj 
###########################################################################################################
    def show(self):
        print(str("hasel : ", self.s ,  "/" ,self.m ,"\n" ))
###########################################################################################################
    def __mul__(self , y):
        sorat=self.s * y.s
        makhraj=self.m * y.m
        return fraction(sorat , makhraj)
###########################################################################################################
    def __sub__(self , y) :
        if(self.m == y.m):
            Fraction = self.s - y.m
            return fraction(Fraction , self.m )
        else:
            Fraction = (self.s * y.m) - (y.s * self.m)
            return fraction(Fraction , self.m * y.m)
###########################################################################################################
    def __add__(self , y) :
        if(self.m == y.m):
            Fraction = self.s + y.s
            return fraction(Fraction , self.m )
        else:
            Fraction = (self.s * y.m) + (y.s * self.m)
            return fraction(Fraction , self.m * y.m)
###########################################################################################################
    def __div__(self , y) :
        sorat = (self.s * y.m )
        makhraj =(self.m * y.s)
        return fraction(sorat  , makhraj)
###########################################################################################################
    def simplified(self,y):  
        if(math.gcd(y.s, y.m)!= 1 ) :
            return fraction(y.s/math.gcd(y.s, y.m)  , y.m/math.gcd(y.s, y.m) )
        else :
            return fraction(y.s, y.m) 
###########################################################################################################
show_menu()
while(True):
    show_menu()
    gozine = ''
    try:
        gozine = int(input('lotfan gozine mored nazar ra vared konid : '))
    except:
        print('gozine vared shode motabar nist ، lotfan gozine ii digar vared konid : ')
             
    if gozine == 1:
        print("kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = fraction(s1 , m1)
        print("kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = fraction(s2 , m2)
        print("hasel : " , num1+num2 , "\n")

    elif gozine == 2:
        print("kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = fraction(s1 , m1)
        print("kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = fraction(s2 , m2)
        print("hasel : " , num1-num2 , "\n")

    elif gozine == 3:
        print("kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = fraction(s1 , m1)
        print("kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = fraction(s2 , m2)
        print("hasel : " , num1*num2 , "\n")

    elif gozine == 4:
        print("kasr 1 \n")
        s1 , m1 = Get_Fraction_Number()
        num1 = fraction(s1 , m1)
        print("kasr 2 \n")
        s2 , m2 = Get_Fraction_Number()
        num2 = fraction(s2 , m2)
        print("hasel : " , num1/num2 , "\n")

    elif gozine == 5:             
        s1 , m1 = Get_Fraction_Number()
        kasr_1 = fraction(s1 , m1)
        print("result : " , kasr_1.simplify(kasr_1))     

    elif gozine == 6:
       break     
print('goodbye ;) \n')