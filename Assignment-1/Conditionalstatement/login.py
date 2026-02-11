correctusername="admin"
correctpassword=1234

username=input("Enter your username: ")
password=int(input("enter your password:"))

if(username==correctusername and password==correctpassword):
    print("Logged in...")
else:
    print("Invalid crediential")    