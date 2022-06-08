import math

def show_menu():
    print("welcome to time calculator :)\n")
    print("1-jam \n")
    print("2-tafrigh \n")
    print("3-sanie be zaman  \n")
    print("4-zaman be sanie  \n")
    print("5-exit \n")
##########################################      GET NUMBER     ##################################################
def Get_time_Number():
    while True :
        saat = int(input('lotfan saat ra vared konid :'))
        daghighe = int(input('lotfan dagighe ra vared konid :'))
        sanie = int(input('lotfan sanie ra vared konid :'))
        if  saat >= 0 and  daghighe >= 0 and sanie >= 0:
            break
        else :
            print("time nmitavand manfi bashad \n")
    return saat , daghighe , sanie
##############################################      CLASS TIME      #############################################
class time :
    def __init__(self , h=0 , m=0 , s=0 ) :
        self.hour = h 
        self.minute=m
        self.second=s
        self.fix_time()

    def show_time (self):
        print("time : " , self.hour , ":" , self.minute , ":" , self.second , "\n")

    def fix_time(self):
        while True :
            if self.minute >= 60 :
                self.minute-=60
                self.hour+=1

            if self.second >= 60 :
                self.second-=60
                self.minute+=1    

            if self.minute<60 and self.second <60 :
                break

    def __add__(self , other):
        result = time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second
        result.fix_time()
        return result

    def __sub__(self , other):
        result = time()
        result.hour = self.hour - other.hour
        result.minute = self.minute - other.minute
        result.second = self.second - other.second
        result.fix_time()
        return result    
    
    def convert_time_to_sec (self):
        result = (int(self.hour) * 3600 + int(self.minute) * 60 + int(self.second))
        return result

    def __str__(self):
        return f"{self.hour:02d}"+':'+f"{self.minute:02d}"+':'+f"{self.second:02d}"   

    @staticmethod
    def convert_sec_to_time (x):
        result = time()
        result.second = x % 60
        x = x // 60
        result.minute = x % 60
        x = x // 60
        result.hour = x
        result.fix_time()
        return result
#######################################    MAIN    #############################################################
while True :
    show_menu()
    gozine = ''
    try:
        gozine = int(input('lotfan gozine mored nazar ra vared konid : '))
    except:
        print('ebarat vared shode motabar nist ، lotfan shomare gozine ra vared konid : ')
             
    if gozine == 1:
        print("\n time 1 \n")
        h1 , m1 , s1  = Get_time_Number()
        t1 = time(h1 , m1 , s1)
        print("\n time 2 \n")
        h2 , m2 , s2 = Get_time_Number()
        t2 = time(h2 , m2 , s2)
        print("hasel : " , t1+t2 , "\n")
    elif gozine == 2:
        print("\n time 1 \n")
        h1 , m1 , s1  = Get_time_Number()
        t1 = time(h1 , m1 , s1)
        print("\n time 2 \n")
        h2 , m2 , s2 = Get_time_Number()
        t2 = time(h2 , m2 , s2)
        print("hasel : " , t1-t2 , "\n")
    
    elif gozine == 3:
        print("\n time 1 \n")
        sec=int(input("lotfan zaman ra vared konid :"))
        t1 = time.convert_sec_to_time(sec)
        print("hasel : " , t1 , "\n")

    elif gozine == 4:
        print("\n time 1 \n")
        h1 , m1 , s1  = Get_time_Number()
        t1 = time(h1 , m1 , s1)
        print("hasel : " , t1.convert_time_to_sec() , "\n")

    elif gozine == 5:
       break   
    else : 
        print("lotfan adadi bein 1 - 5 vared konid \n ") 
    input("\nPress ENTER to continue...\n")     
print('goodbye ;) \n')