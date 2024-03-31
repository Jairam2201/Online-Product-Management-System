def reg():
    import csv
    f=open("reg1.csv","a",newline="")
    a=csv.writer(f)
    studentid=input("Enter an ID:")
    user=input("Enter a useranme:")
    pswd=input("Enter a password:")
    phno=input("PHNO:")
    a.writerow([studentid,user,pswd,phno])
reg()
