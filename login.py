class login:
    def login(self):
        k=0
        while k<1:
            self.user=input("enter username:")
            self.pswd=input("enter password:")
            import csv
            with open("reg1.csv","r",newline="") as file:
                store=csv.DictReader(file)
                for i in store:
                    if self.user==i["user"] and self.pswd==i["pswd"]:
                        print("login successfully")
                        k=1
                        break
                if self.user!=i["user"] or self.pswd!=i["pswd"]:
                    print("incorrect login credentials")
                        
            
        
obj=login() 
obj.login()
