################################  armstrong number #############################

adad= int(input("lotfan adad khod ra vared monid : "))
tavan = len(str(adad))
sum = 0
temp = adad
while temp > 0:
   digit = temp % 10
   sum += digit ** tavan
   temp //= 10

if adad == sum:
   print(adad,"is an Armstrong ")
else:
   print(adad,"is not an Armstrong ")