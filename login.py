class login:
    def login(self):
        k=0
        while k<1:
            self.user=input("Enter username:")
            self.pswd=input("Enter password:")
            import csv
            with open("reg1.csv","r",newline="") as file:
                store=csv.DictReader(file)
                for i in store:
                    if self.user==i["user"] and self.pswd==i["pswd"]:
                        print("--->LOGIN SUCCESS<---")
                        k=1
                        break
                if self.user!=i["user"] or self.pswd!=i["pswd"]:
                    print("Incorrect login credentials.Please enter again.")
                        
            
        
obj=login() 
obj.login()