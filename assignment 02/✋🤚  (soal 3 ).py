import random

print ("** welcome**")
count_user = 0
count_comp_1 = 0 
count_comp_2 =0
while True :
    print ("1- ro ")
    print ("2- posht")
    user = (int(input ("lotfn gozine mored nazar ra vared konid :")))
    while True :
        if user != 1 and user != 2  :
            print ("lotfan yki az adad 1 - 2 ra  entekhab konid 😒")
            user = (int(input ("lotfn gozine mored nazar ra vared konid :")))
        else :
            break
    comp_1 = random.randint(1,2)
    comp_2 = random.randint(1,2)
    if (comp_1 == comp_2 and user == comp_1 and user == comp_2) :
        print ("in round barande nadasht ")

    elif (comp_1 == comp_2 and user != comp_1 and user != comp_2) :
         print ("barande in round : user ")
         count_user += 1

    elif (comp_1 != comp_2 and user != comp_1 and user == comp_2) :
        print ("barande in round : computer 1 ")
        count_comp_1 += 1

    elif (comp_1 != comp_2 and user == comp_1 and user!= comp_2) :
        print ("barande in round : computer 2 ")
        count_comp_2 += 1
        
    if (count_user == 1 or count_comp_1 == 1 or count_comp_2 ==1) :
        break