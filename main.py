#Main Code

#Importing Libraries
import mysql.connector as MC
import Admin
import customers1



print("Hello, welcome to Virtual CinePlex")
status='ON'
while(status!='E'):
    
    print("\nEnter 1 for Admin and 2 for customer and E to exit:\n ")
    ch=input("")
    
    if ch=='1':
        res=Admin.Edit()
    elif ch=='2':
        res=customers1.cust()
    elif ch=='E':
        status='E'
    else:
        print("Wrong input, please enter y to try again or enter E to exit")
        status=input()
        
print("Thank you for visiting Virtual CinePlex")
    




