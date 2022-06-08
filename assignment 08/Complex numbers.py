def show_menu():
    print("welcome to Complex numbers calculator :)\n")
    print("1-jam \n")
    print("2-tafrigh \n")
    print("3-zarb \n")
    print("4-taghsim \n")
    print("5-exit \n")
##########################################      GET NUMBER     ##################################################
def Get_complex_Number():
    real = int(input('lotfan ghesmat real adad  ra vared konid :'))
    image = int(input('lotfan ghesmat imagee adad ra vared konid :'))
    return real , image
############################################     CLASS COMPLEX      ##########################################
class Complex_numbers :
    def __init__ (self, re=0, im=0):
        self.real = re
        self.img = im

    def __add__(self, other):
        result=Complex_numbers()
        result.real = self.real + other.real
        result.img = self.img + other.img
        return result

    def __sub__(self, other):
        result=Complex_numbers()
        result.real = self.real - other.real
        result.img = self.img - other.img
        return result

    def __mul__(self, other):
        result=Complex_numbers()
        result.real = self.real * other.real - self.img * other.img
        result.img = self.img * other.real + self.real * other.real
        return result

    def __truediv__(self, other):
        divisor = (other.real**2 + other.img**2)
        return Complex_numbers((self.real * other.real - self.img * other.img)/divisor , (self.img * other.real + self.real * other.img)/divisor)

    def show(self):
        print(str( self.real ,  self.img , "j" ,"\n" ))
    
    def __str__(self):
        if self.img >=0 :
            return str(self.real) + " + " + str(self.img) + "j"
        else :
            return str(self.real) + " - " +  str(abs(self.img)) + "j"
#######################################    MAIN    #############################################################
while True :
    show_menu()
    gozine = ''
    try:
        gozine = int(input('lotfan gozine mored nazar ra vared konid : '))
    except:
        print('ebarat vared shode motabar nist ، lotfan shomare gozine ra vared konid : ')
             
    if gozine == 1:
        print("\n Complex_numbers 1 \n")
        r1 , i1  = Get_complex_Number()
        num1 = Complex_numbers(r1 , i1)
        print("\n Complex_numbers 2 \n")
        r2 , i2 = Get_complex_Number()
        num2 = Complex_numbers(r2 , i2)
        print("hasel : " , num1+num2 , "\n")

    elif gozine == 2:
        print("\n Complex_numbers 1 \n")
        r1 , i1 = Get_complex_Number()
        num1 = Complex_numbers(r1 , i1)
        print("\n Complex_numbers 2 \n")
        r1 , i1 = Get_complex_Number()
        num2 = Complex_numbers(r1 , i1)
        print("hasel : " , num1-num2 , "\n")
    
    elif gozine == 3:
        print("\n Complex_numbers 1 \n")
        r1 , i1 = Get_complex_Number()
        num1 = Complex_numbers(r1 , i1)
        print("\n Complex_numbers 2 \n")
        r1 , i1 = Get_complex_Number()
        num2 = Complex_numbers(r1 , i1)
        print("hasel : " , num1*num2 , "\n")

    elif gozine == 4:
        print("\n Complex_numbers 1 \n")
        r1 , i1 = Get_complex_Number()
        num1 = Complex_numbers(r1 , i1)
        print("\n Complex_numbers 2 \n")
        r1 , i1 = Get_complex_Number()
        num2 = Complex_numbers(r1 , i1)
        print("hasel : " , num1/num2 , "\n")

    elif gozine == 5:
       break   
    else : 
        print("lotfan adadi bein 1 - 5 vared konid \n ")
    input("\nPress ENTER to continue...\n")    
print('goodbye ;) \n')