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
        dbEntry = VSNData(SerialNumberPattern=row[0], VehicleTrimId=row[1], Year=row[2], Make=row[3], Model=row[4], TrimName=row[5])
        dbEntry.save()

print "\nImport from CSV to VSNData db is complete...\n"





