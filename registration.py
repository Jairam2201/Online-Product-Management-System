import csv
def reg():
    f=open("reg1.csv","a",newline="")
    a=csv.writer(f)
    print("!!!WELCOME TO AMAZON!!!")
    studentid=input("Enter an ID:")
    user=input("Enter a useranme:")
    pswd=input("Enter a password:")
    phno=input("PHNO:")
    a.writerow([studentid,user,pswd,phno])
    print("--->Successfully Registered<---")
reg()