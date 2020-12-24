#DATA DESTROYER
import os
import csv
os.remove("Sales_Directory.csv")
fobj=open("Python_SQLConnectIon.csv","r")
csvr=csv.reader(fobj)
next(csvr)
for row in csvr:
    hos=row[0]
    use=row[1]
    pas=row[2]
fobj.close()
os.remove("Python_SQLConnectIon.csv")
import mysql.connector as m


    
mydb=m.connect(
    host=hos,
    user=use,
    password=pas,
    )
Cur=mydb.cursor()
Cur.execute("DROP DATABASE Cinema")
mydb.commit()
mydb.close()
print("Data eliminated")
