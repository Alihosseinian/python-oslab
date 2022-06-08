import random
result=[]
boys = ["ali" , "reza" , "yasin" , "benyamin" , "mehrdad" , "sajjad" , "aidin" , "shahin"]
girls = ["sara" , "zari" , "neda" , "homa" , "eli" , "goli" , "mari" , "mina"]
####################################################### selected boy and girl  #########################################################################
def Marriage():
    kam=min(len(boys) , len(girls))
    for i in range(kam):
        new_dic={'boy':'' ,'girl':''}
        index_boy=random.randint(0,len(boys)-1)
        new_dic['boy']=boys[index_boy]
        boys.pop(index_boy)
        index_girl=random.randint(0,len(girls)-1)
        new_dic['girl']=girls[index_girl]
        girls.pop(index_girl)    
        result.append(new_dic)
    
####################################################### show result   #########################################################################
def show_result():
    for i in range(len(result)) :
        print( "zoj " + str(i+1) + ": (" +  result[i]['boy'] + "," + result[i]['girl']  + ")\n" )
####################################################### main  #########################################################################
while True :
    Marriage()
    if len(boys)==0 or len(girls)==0 :
        print("\n")
        show_result()
        break
print("goodbye :)\n\n")
