# load up the model for VSNData
from importVsns.models import VSNData


#------------------------------------
#Use 'csv' module to read csv file

print "\nStarting Import from CSV to VSNData db...\n"

import csv

#open up csv file (assume: fixed path for this exercise, not cmd line file input) and load into array
#Note: no error checking on the csv/input array at this point (assuming csv file is "perfect" for exercise)

with open('./importVsns/vsn_data_noheader.csv', 'rb') as csvfile:
    VsnInputArray = csv.reader(csvfile, delimiter=',')
    
    # loop over lines of array, one at time and save into db
    for row in VsnInputArray:
        a=str(row[0])
        a1=a[0:6]
        a2=a[6:12]
        mod_a1=a1.replace("*","[A-Z*]")
        mod_a2=a2.replace("*","[0-9*]")
        mod_a = mod_a1 + mod_a2
        dbEntry = VSNData(Indexed_SNP=mod_a, SerialNumberPattern=str(row[0]), VehicleTrimId=int(row[1]), Year=int(row[2]), Make=str(row[3]), Model=str(row[4]), TrimName=str(row[5]))
        dbEntry.save()

print "\nImport from CSV to VSNData db is complete...\n"





