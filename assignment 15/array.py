from math import *
#####################################################
def motagharen(araye):
    for i in range(len(araye)):
        if araye[i] != araye[-i-1]:
            return False
    return True
#####################################################
araye = []
n = int(input("lotfan tedad adad khod ra vared konid : "))

for i in range(0, n):
    x = int(input("lotfan adad mored nazar ra vared konid :"))
    araye.append(x)

if (motagharen(araye)):
    print ("motagharen ast \n ")
else:
    print ("motagharen nist \n")