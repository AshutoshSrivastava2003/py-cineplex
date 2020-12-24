# Admin File
import mysql.connector as mc

def Edit():
    mydb=mc.connect(
        host="localhost",
        user="root",
        password="Batman123",
        database="Cinema")
    Cur=mydb.cursor()
    p=input("Enter password: ")
    if p!="Project":
        print("Wrong Password")
        return 0
    
    
    while(1):
        print("To make any changes press C and to exit press E")
        
        choice=input("")
        if choice=='E':
            break
        f_times=['09:00:00','12:00:00','15:00:00','18:00:00','21:00:00']
        f_hall=[1,2,3,4,5]
        f_name=[]
        d=['UA','PG 13','R','PG 15']
        g=['Comedy','Horror','Action','Science Fiction','Documentary','Thriller']
        Cur.execute("SELECT date_format(Showtime,'%r'),Film_Name,Hall_No FROM Movie_List ORDER BY Showtime")
        L=[]
        print("Current schedule:\n")
        print("Showtime"+" "*5,"Film_Name"+" "*10,"Hall_No")
        for  i in Cur:
            print(i[0],end=" "*3)
            print(i[1],end=" "*(20-len(i[1])))
            L.append(i[1])
            print(i[2])
        
        status=1
        while status==1:
            
            time=input("Enter show time in 24 hour format: ")
            if time not in f_times:
                print("Wrong input, please enter again: ")
                continue
            status=0
        status=1
        
        while status==1:
            hall=int(input("Enter hall number: "))
            if hall not in f_hall:
                print("Wrong input, please enter again: ")
                continue
            status=0
        status=1
        
        while status==1:
            film=input("Enter film name: ")
            
            if film not in L:
                try:
                    film_genre=g[int(input("Enter genre 0-Comedy, 1-Horror, 2-Action, 3-Science Fiction, 4-Documentary and 5-Thriller: "))]
                except:
                   print("Please enter valid input ")
                   continue
                try:
                    film_rating=float(input("Enter film rating out of 5: "))
                except:
                    print("Enter valid data please.")
                    continue
                try:
                    film_age=d[int(input("Enter genre 0-UA, 1-PG 13, 2-R AND 3-PG 15: "))]
                except:
                    print("Please enter valid input: ")
                    continue
                filmdes=input("Enter a description in less than 100 characters: ")
                try:
                    Cur.execute("INSERT INTO Film_Description VALUES('{}','{}','{}','{}',{})".format(film,film_genre,film_age,filmdes,film_rating))
                except:
                    print("Data could not be registered due to invalid input")
                    continue
                mydb.commit()
            status=0
        
            
        Cur.execute("UPDATE Movie_List SET Film_Name='{}' WHERE Showtime='{}' AND Hall_No='{}'".format(film,time,hall))
        if Cur.rowcount!=1:
            Cur.execute("INSERT INTO Movie_List VALUES('{}','{}',{})".format(time,film,hall))
        
        mydb.commit()
        print("Changes Made")
        print("\nUpdated Schedule: ")
        print("Showtime"+" "*5,"Film_Name"+" "*10,"Hall_No")
        Cur.execute("SELECT date_format(Showtime,'%r'),Film_Name,Hall_No FROM Movie_List ORDER BY Showtime")
        
        for  i in Cur:
            print(i[0],end=" "*3)
            print(i[1],end=" "*(20-len(i[1])))
            print(i[2])


        
            
            
    
    return None
        
        
    
       
        
       
        

             
    
