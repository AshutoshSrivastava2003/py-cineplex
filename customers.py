import csv

def cust():
    fobj=open("Python_SQLConnectIon.csv","r")
    csvr=csv.reader(fobj)
    next(csvr)
    for row in csvr:
        hos=row[0]
        use=row[1]
        pas=row[2]
    fobj.close()
    Name=input('Enter your Name: ')
    Age=int(input('Enter your Age: '))
    Q_ID=int(input('Enter your Qatar Id: '))

    import mysql.connector as MC
    mydb=MC.connect(
        host=hos,
        user=use,
        password=pas,
        database="Cinema"
        )

    mycursor=mydb.cursor()
    mycursor.execute("SELECT date_format(Showtime,'%T'),Film_Name,Hall_No FROM Movie_List ORDER BY Showtime")
    myrecords=mycursor.fetchall()
    a=1
    print("Here are the show timings \n")
    print("S.No.","Showtime"+" "*5,"Film_Name"+" "*10,"Hall_No")
    for i in myrecords:
        print(a,end=" "*(5-a//10))
        print(i[0],end=" "*3)
        print(i[1],end=" "*(25-len(i[1])))
        
        print(i[2])
        a+=1
    
    Movie=int(input('\nselect the movie number: '))-1 #value of a
    
    Number_of_Tickets=int(input('number of tickets: '))
    Show_Name=myrecords[Movie][1]
    Show_Time=myrecords[Movie][0]
    Amount=Number_of_Tickets*30
    
    mycursor.execute("select * from Film_Description WHERE Movie='{}'".format(Show_Name))
    record=[]
    for i in mycursor:
        for j in i:
            record.append(j)
        
    
    
    AR=record[2]
    dage={'R':18,'PG 13':13,'UA':7,'PG 15':15}
    for i in dage:
        if AR==i:
            AR=dage[i]
            break
    
    if Age<AR:#check age
        print('Sorry you are too young to watch this film.')
        return None
        
   
    print('Good choice!')
    print('Movie details:')
    print('\nMovie name is',record[0])
    print('\nGenre is',record[1])
    print('\nAge restriction is',record[2])
    print('\nDescription :\n',record[3])
    print('\nRating is ',record[4])
    print("Do you wish to confirm your booking? Y/N ")
    c=input("")
    if c=="N":
        quit
    else:
        print("Your reservation is done.")
        Res_code=Name[0]+str(Q_ID%10)+str(Age*2)
        print("This is your reservaton code which you can present along with your QID at the entry point.\n",Res_code)
    
    customer=[Name,Age,Q_ID,Number_of_Tickets,Show_Name,Show_Time,Amount]

    mycursor.execute("insert into Sale_Log VALUES('{}','{}','{}','{}','{}','{}','{}')".format(Name,Age,Q_ID,Number_of_Tickets,Show_Name,Show_Time,Amount))
    mydb.commit()
    fobj=open("Sales_Directory.csv","a")
    
    mycursor.execute("SELECT Customer_Name, Age, Q_ID,Number_of_tickets,Show_Name,date_format(Show_Time,'%r'),Amt_Paid FROM Sale_Log")
    data=mycursor.fetchall()
    csvw=csv.writer(fobj)
    
    csvw.writerows(data)
    fobj.close()

    
    



