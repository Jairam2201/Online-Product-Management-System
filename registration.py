import csv
def reg():
    f=open("registration.csv","a",newline="")
    a=csv.writer(f)
    print("!!!WELCOME TO AMAZON!!!")
    studentid=input("Enter an ID:")
    i=True
    while i:
        user=input("Enter a useranme:")
        with open("registration.csv","r",newline="") as file:
                    store=csv.DictReader(file)
                    for i in store:
                        if user==i["User"]:
                            print("Username already exists.")
                            i=True
                            break
                        else:
                            i=False
    pswd=input("Enter a password:")
    phno=input("PHNO:")
    a.writerow([studentid,user,pswd,phno])
    print("--->Successfully Registered<---")
reg()
