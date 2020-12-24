#Installation_Setup
import csv
import mysql.connector as m
hos=input("Enter mysql host name: ")
use=input("Enter mysql user name: ")
pas=input("Enter mysql password: ")
try:
    
    mydb=m.connect(
        host=hos,
        user=use,
        password=pas,
        )
except:
    print("Wrong details, please try again.")
Cur=mydb.cursor()
Cur.execute("CREATE DATABASE if not exists Cinema")
Cur.execute("USE Cinema")
Cur.execute("CREATE TABLE IF NOT EXISTS Movie_List(Showtime time, Film_Name varchar(20), Hall_No integer)")
Cur.execute("CREATE TABLE IF NOT EXISTS Film_Description(Movie varchar(20),Genre varchar(20), Age_Res varchar(20),Description varchar(100), Rating decimal(2,1))")
Cur.execute("CREATE TABLE IF NOT EXISTS Sale_Log(Customer_Name varchar(20),Age integer,Q_ID integer, Number_of_tickets integer,Show_Name varchar(20),Show_Time time,Amt_Paid decimal(7,2))")
st='INSERT INTO Movie_List VALUES("{}","{}",{})'
m1="MR BEAN"
m2="Walk In The Dark"
m3="Story of Tolstoy"
m4="Physics Class"
m5="Alien From Mars"
m6="My Naughty Brother"
m7='Fog'
m8='Dr. Strange 2'
t1='09:00:00'
t2='12:00:00'
t3='15:00:00'
t4='18:00:00'
t5='21:00:00'
Cur.execute(st.format(t1,m1,1))
Cur.execute(st.format(t4,m1,1))

Cur.execute(st.format(t2,m2,2))
Cur.execute(st.format(t3,m2,3))
Cur.execute(st.format(t5,m2,1))

Cur.execute(st.format(t2,m3,3))
Cur.execute(st.format(t4,m3,5))

Cur.execute(st.format(t2,m4,4))
Cur.execute(st.format(t5,m4,3))

Cur.execute(st.format(t2,m5,5))
Cur.execute(st.format(t4,m5,3))

Cur.execute(st.format(t1,m6,2))

Cur.execute(st.format(t3,m7,5))
Cur.execute(st.format(t5,m7,5))
Cur.execute(st.format(t1,m7,3))

Cur.execute(st.format(t5,m8,4))


st="INSERT INTO Film_Description VALUES('{}','{}','{}','{}',{})"
a1="R"
a2="PG 13"
a3="PG 15"
a4="UA"
g1="Horror"
g2="Science Fiction"
g3="Comedy"
g4="Documentary"
g5="Action"
Cur.execute(st.format(m7,g1,a1,"Haunted house owner returns to take revenge.",4.0))
Cur.execute(st.format(m5,g2,a2,"Alien Po comes from Mars in a Ufo in search of Uranium on Earth",4.0))
Cur.execute(st.format(m2,g1,a1,"Haley goes to his new school but gets trapped over there at night",4.5))
Cur.execute(st.format(m6,g3,a4,"JO describes an incident when her brother ruined her day",4.5))
Cur.execute(st.format(m3,g4,a4,"A vivid account of Leo Tolstoy early works and his greatest achievements.",4.5))
Cur.execute(st.format(m1,g5,a4,"Mr. Bean despite of his disability turns into a great spy and saves his nation.",3))
Cur.execute(st.format(m4,g2,a3,"A Physics teacher explores the realms of quantum computing and gets trapped in a time loop.",5))
Cur.execute(st.format(m8,g2,a2,"Dr. Strange gets teleported into another dimenson where he finds an old foe.",4.7))

mydb.commit()
fobj=open("Sales_Directory.csv","w")
l=["Customer Name","Age","Qatar ID","Number of tickets","Show Name","Showtime","Amount Paid"]
csvw=csv.writer(fobj)
csvw.writerow(l)
fobj.close()


fobj=open("Python_SQLConnectIon.csv","w")
l=["host","user","password"]
csvw=csv.writer(fobj)
csvw.writerow(l)
l=[hos,use,pas]
csvw.writerow(l)
fobj.close()

print("SETUP on device is done, proceed to MAIN page.")
