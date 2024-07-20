import csv
class login:
    def login(self):
        k=0
        while k<1:
            self.user=input("Enter username:")
            self.pswd=input("Enter password:")
            with open("registration.csv","r",newline="") as file:
                store=csv.DictReader(file)
                for i in store:
                    if self.user==i["User"] and self.pswd==i["Pswd"]:
                        print("--->LOGIN SUCCESS<---")
                        k=1
                        break
                if self.user !=i["User"] or self.pswd !=i["Pswd"]:
                    print("Incorrect login credentials.Please enter again.")
                        
            
        
obj=login() 
obj.login()
