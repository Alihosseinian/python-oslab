##########################################################################################
############################################# modle 1 (tabe amade ) ######################
##########################################################################################
from datetime import timedelta

sec = int (input("lotfn modat zaman ra be sanie vared konid : "))
print('Time in Seconds:', sec)

td = timedelta(seconds=sec)
print('Time in hh:mm:ss:', td)
##########################################################################################
############################################# modle 2 ####################################
##########################################################################################
import math
sec_2 = int (input("(modle 2 )lotfn modat zaman ra be sanie vared konid :"))
saat = sec_2 / 3600 
daghighe = (sec_2 % 3600) / 60 
sanie = (sec_2 % 3600) / 60 
print (math.floor(saat) , ":" , math.floor(daghighe) , ":" , math.floor(sanie) ,)