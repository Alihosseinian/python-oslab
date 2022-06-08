
side_1 = int(input ('please enter the First side value :'))
side_2 = int(input ('please enter the second side value :'))
side_3 = int(input ('please enter the third side value :'))

if side_1 < (side_2 + side_3) and side_2 < (side_1 + side_3) and side_3 < (side_1 + side_2):
    print(' yes you can make a triangle with these values') 

else :
    print(' no you can not make a triangle with these values') 
