import os
PRODUCTS=[]
############################################################    SHOW MENU    ########################################################
def show_menu():
    print("welcome to shop :)\n")
    print("1-add :\n")
    print("2-edit :\n")
    print("3-delet :\n")
    print("4-show list :\n")
    print("5-search :\n")
    print("6-buy :\n")
    print("7-save and exit:\n")
######################################################################################################################################
def index_finder_name(esm):
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name']==esm:
            return i
    return -1
##########################################################    LOAD DATA FILE   ########################################################
def load_data_from_file():
    print("Loading ....\n\n")
    f=open('database.csv' , 'r')
    for khat in f :
        info=khat[:-1].split(',')
        new_dictionary = {'code':info[0] , 'name':info[1] , 'price':info[2] , 'count':info[3]  }
        PRODUCTS.append(new_dictionary)
    for i in range(len(PRODUCTS)):    
        print( PRODUCTS[i],'\n')
    print("Database loaded . app is ready to use \n\n")
##########################################################   ADD    ##################################################################  
def Add():
    found=False
    esm=input("lotfan esm mahsol khod ra vared konid : ")
    index = index_finder_name(esm)
    if index != -1:
        print("in kala ba ID CODE  :",   PRODUCTS[index]['code']   , "ba gheimat :",PRODUCTS[index]['price']   , " va tedad :", PRODUCTS[index]['count'] , "mojod ast")
        tedad=int(input("\nche tedad mikhahid ezafe konid : ")) 
        PRODUCTS[index]['count']=str(int(PRODUCTS[index]['count'])+tedad)
        print("tedad mored nazar ezafe shod \n")
    else :
        print("mahsol mored nazar jozv kala ha nist va bayad tarif konid an ra ")
        code=input("lotfan code mahsol khod ra vared konid ")
        while True :
            flag=False
            for product in PRODUCTS :
                if product['code']==code :
                    print("code vared shode ghablan estefde shode ast lotfan code jadidi vared konid :")
                    code=input("lotfan code mahsol khod ra vared konid ")
                    flag=True
                    break
            if not flag:
                break
        gheimat=input("lotfan gheimat mahsol khod ra vared konid : ")
        tedad=input("lotfan tedad mahsol khod ra vared konid  :")
        new_dictionary = {'code':code , 'name':esm , 'price':gheimat , 'count':tedad  }
        PRODUCTS.append(new_dictionary) 
        print("mahsol mored nazar vared kala ha shod ")
############################################################   EDIT    ##############################################################
def Edit():
    esm=input("lotfan esm mahsol khod ra vared konid : ")
    flag=False
    for product in PRODUCTS :
        if product['name']==esm :
            flag=True 
            print("kodam ghesmat mahsol ra mikhahid taghir dahid : ")
            print("1-code ")
            print("2-name ")
            print("3-price ")
            print("4-count ")
            gozine=int(input("lotfan gozine mored nazar ra vared konid : "))
            if gozine==1 :
                _flag=True
                while True :
                    if  _flag:
                        code=int(input("lotfan code jadid mored nazar ra vared konid : "))
                    _flag=False
                    for _product in PRODUCTS :
                        if int(_product['code'])==code :
                            print("code vared shode ghablan barai mahsoli digar estefde shode ast lotfan code jadidi vared konid :")
                            _flag=True
                    if not _flag:
                        break
                product['code'] = str(code)
                print("code mahsol taghir kard \n") 
            elif gozine == 2 :
                esm=input("lotfan name jadid  mored nazar ra vared konid :")
                product['name'] = esm
                print("name mahsol taghir kard \n")
                break
            elif gozine == 3 :
                gheimat=int(input("lotfan gheimat jadid  mored nazar ra vared konid :"))
                product['price'] = gheimat
                print("gheimat mahsol taghir kard \n")
                break
            elif gozine == 4 :
                tedad=int(input("lotfan tedad jadid  mored nazar ra vared konid : "))
                product['count'] = tedad
                print("tedad mahsol taghir kard \n")
                break
    
    if not flag :
        print("kalaie mored nazar mojod nist\n ")             
#########################################################    DELET   #################################################################
def Delet():
    esm=input("lotfan esm mahsol khod ra vared konid : ")
    for i in range(len(PRODUCTS)-1) :
        if PRODUCTS[i]['name']==esm:
           PRODUCTS.pop(i)  
           print("mahsol mored nazar hazf shod \n ")
#########################################################    SHOW LIST     ###########################################################
def Show_list():
    for product in PRODUCTS :
        print( "CODE : " ,product['code'],'\t\t' ,"NAME : ", product['name'],'\t\t' ,"GHEIMAT : ", product['price'],'\t\t' ,"TEDAD :", product['count'],'\t\t' ,)
#########################################################  SERACH  ###################################################################
def Search():
    esm=input("lotfan esm mahsol khod ra vared konid : ")
    for product in PRODUCTS :
        if product['name']==esm:
            print("in kala ba ID CODE  :",product['code'] ,"name :",product['code'] ,"ba gheimat :",product['price'] ," va tedad :",product['count'] , "mojod ast")
            return
    print("kalaie mored nazar mojod nist")
    return
####################################################### BUY  #########################################################################
def Buy():
    bill=0
    sabad_kharid=[]
    while True :
        print("1-ezafe kardan be sabad kharid")
        print("2-etmam kharid + chap factor")
        gozine=int(input("lotfan gozine mored nazar ra vared konid : "))
        if gozine==1 :
            esm=input("lotfan esm mahsol khod ra vared konid  : ")
            found = False
            for product in PRODUCTS :
                if product['name']==esm:
                    print("in kala mojod ast  ID CODE  :",   product['code']   , "ba gheimat :",product['price']   , " va tedad :", product['count'] , "mojod ast")
                    found = True
                    while True :
                        tedad=int(input("che tedad mikhahid : "))
                        while True :
                            if tedad >= 0 :
                                break
                            tedad=int(input("ein adamizad yek adad + vared konid : "))
                        if tedad > int(product['count']) :
                            print("in mizan az kala mojod nemibashad ")
                            print("tedad mojod az kalaie mored nazar : ",product['count'])
                            break
                        else :
                            product['count']=str(tedad)
                            ins=dict(product)
                            bill+=tedad*int(product['price'])
                            sabad_kharid.append(ins)
                            product['count']=str(int(product['count'])-tedad)
                            break
            if not found :
                    print("kalaie mored nazar mojod nist")
        if gozine==2 : 
            print("sabad kharid shoma : \n ")
            for product in sabad_kharid:
                print(product)  
            print("total sum :",bill)          
            break
###########################################   main   ###########################################################################
load_data_from_file()
while True :
    show_menu()
    choise=int(input("lotfan amaliat mored nazar ra entekhab konid :"))
    if choise == 1 :
        Add()
    elif choise == 2 :
        Edit()
    elif choise == 3 :
        Delet()
    elif choise == 4 :
        Show_list()
    elif choise == 5 :
        Search()
    elif choise == 6 :
        Buy() 
    elif choise == 7 : 
       f=open('my_file.txt' , 'w')   
       for product in PRODUCTS:
            f.write(product['code']+','+product['name']+','+product['price']+','+product['count']+'\n')       
       break
os.system("cls")    
print("etelaat dar file zakhire shod \n")    
print("goodbye :)\n\n")