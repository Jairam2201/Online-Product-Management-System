def reg():
    import csv
    f=open("reg1.csv","a",newline="")
    a=csv.writer(f)
    studentid=input("enter a id:")
    user=input("enter  useranme:")
    pswd=input("enter a password:")
    phno=input("phno:")
    a.writerow([studentid,user,pswd,phno])
reg()
