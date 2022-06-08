################################  chek factoriel #############################

adad = int(input("lotfan adad mored nazar ra vared konid "))
tedad = 1
faoriel = 1
while (faoriel < adad) :
    tedad += 1
    faoriel *= tedad
if adad == faoriel:
    print('Yes')
else:
    print('No')