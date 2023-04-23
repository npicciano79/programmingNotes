#notes on creating, reading and writing to CSV files


#sample creating CSV code
#include import 

import CSV  


header=[' index ',' category ',' name ',' street ',' city ',' zip ',' phone ',' fax ',' website ',' about ',' contact ']
with open('businessCSV.csv','w',newline='')as f:
    writer=csv.writer(f,delimiter=',',escapechar=' ',quoting=csv.QUOTE_NONE)
    writer.writerow(header)
    #writer.writerow(space)
    for bus in business_data:
        writer.writerow(bus) 



#reading from CSV
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))



#creating temporary CSV, removing header
with open('businessCSV.csv','r') as f:
    with open('temp_businessCSV.csv','w') as fl:
        next(f) #skip header line
        for line in f:
            fl.write(line)
  
