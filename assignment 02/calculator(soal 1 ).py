import math 
import os
while True :

    print ("** wellcome to calculator**")
    print ("1- add")
    print ("2- sub")
    print ("3- mul")
    print ("4- div")
    print ("5- sin")
    print ("6- cos")
    print ("7- tan")
    print ("8- cot")
    print ("9- log")
    print ("10- exit")
    gozine = int (input ("lotfan adad gozine mored nazar khod ra entekhab konid : "))

    if gozine == 1 :
        adad_aval = int(input ("lotfan adad aval ra vared konid : "))
        adad_dovom = int(input ("lotfan adad dovom ra vared konid : "))
        hasel = adad_aval + adad_dovom
        print (hasel)
#######################################################################################################
    elif gozine == 2 :
        adad_aval = int(input ("lotfan adad aval ra vared konid : "))
        adad_dovom = int(input ("lotfan adad dovom ra vared konid : "))
        hasel = adad_aval - adad_dovom
        print (hasel)
#######################################################################################################
    elif gozine == 3 :
        adad_aval = int(input ("lotfan adad aval ra vared konid : "))
        adad_dovom = int(input ("lotfan adad dovom ra vared konid : "))
        hasel = adad_aval * adad_dovom
        print (hasel)
#######################################################################################################
    elif gozine == 4 :
        adad_aval = int(input ("lotfan adad aval ra vared konid : "))
        adad_dovom = int(input ("lotfan adad dovom ra vared konid : "))
        if adad_dovom == 0 :
            print ("taghsim bar 0 tarif nashodas ")
        else :
            hasel = adad_aval / adad_dovom
            print (hasel)
#######################################################################################################
    elif gozine == 5 :
      adad_aval = int(input ("lotfan adad mored nazar ra vared konid : "))
      math.radians=adad_aval/360 *2 *math.pi
      hasel = math.sin(math.radians)
      print ("sin " , adad_aval , "daraje : "  , hasel )
#######################################################################################################
    elif gozine == 6 :
      adad_aval = int(input ("lotfan adad mored nazar ra vared konid : "))
      math.radians=adad_aval/360 *2 *math.pi
      hasel = math.cos(math.radians)
      print ("cos" , adad_aval , "daraje:" , hasel )
#######################################################################################################
    elif gozine == 7 :
      adad_aval = int(input ("lotfan adad mored nazar ra vared konid : "))
      math.radians=adad_aval/360 *2 *math.pi
      hasel = math.tan(math.radians)
      print ("tan " , adad_aval , "daraje :" , hasel )
#######################################################################################################
    elif gozine == 8 :
      adad_aval = int(input ("lotfan adad mored nazar ra vared konid : "))
      math.radians=adad_aval/360 *2 *math.pi
      hasel = math.atan(math.radians)
      print ("cot " , adad_aval , "daraje :" , hasel )  
#######################################################################################################
    elif gozine == 9 :
      adad_aval = int(input ("lotfan adad mored nazar ra vared konid : "))
      hasel_10 = math.log10(adad_aval)
      hasel_2 = math.log2(adad_aval)
      print ("log dar mabna 10 : " ,  hasel_10 )   
      print ("log dar mabna 2 : " ,  hasel_2 )  
########################################################################################################
    elif gozine == 10 :
        print ( "bye bye  💙")
        break
    else :
        print ("natije mored nazar yaft nashod ")

##clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
##clearConsole()
## ostad mn in tike ro bara system cls omdm emtehan konm safham kolan pak mishod dg comment krdmsh bbkhshid 😂😂