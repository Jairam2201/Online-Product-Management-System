class products:
    def __init__(self):
        print("Amazon products:")
    def iphone(self):
        self.dict_1= {'name': 'iphone', 'price': 50000,'category':'mobiles','stockleft':100 }
        print("name:",end=" ")
        self.name="iphone"
        print(self.name)
        print("price:",end=" ")
        self.price=50000
        print(self.price)
        print("category:",end=" ")
        self.category="mobiles"
        print(self.category)
        print("stock left:",end=" ")
        q=self.dict_1["stockleft"]
        print(q)
    def vivo(self):
        self.dict_2 = {'name': 'vivo', 'price': 45000,'category':'mobiles','stockleft':90 }
        print("name:",end=" ")
        self.name="vivo"
        print(self.name)
        print("price:",end=" ")
        self.price=45000
        print(self.price)
        print("category:",end=" ")
        self.category="mobiles"
        print(self.category)
        print("stock left:",end=" ")
        print(self.dict_2["stockleft"])
    def puma(self):
        self.dict_3= {'name': 'puma', 'price': 4000,'category':'shoes','stockleft':190 }
        print("name:",end=" ")
        self.name="puma"
        print(self.name)
        print("price:",end=" ")
        self.price=4000
        print(self.price)
        print("category:",end=" ")
        self.category="shoes"
        print(self.category)
        print("stock left:",end=" ")
        print(self.dict_3["stockleft"])
    def hrx(self):
        self.dict_4= {'name': 'hrx', 'price': 5000,'category':'shoes','stockleft':100 }
        print("name:",end=" ")
        self.name="hrx"
        print(self.name)
        print("price:",end=" ")
        self.price=5000
        print(self.price)
        print("category:",end=" ")
        self.category="shoes"
        print(self.category)
        print("stock left:",end=" ")
        print(self.dict_4["stockleft"])
    def boat(self):
        self.dict_5 = {'name': 'boat', 'price': 1500,'category':'airpods','stockleft':150 }
        print("name:",end=" ")
        self.name="boat"
        print(self.name)
        print("price:",end=" ")
        self.price=1500
        print(self.price)
        print("category:",end=" ")
        self.category="airpods"
        print(self.category)
        print("stock left:",end=" ")
        print(self.dict_5["stockleft"])
    def oneplus(self):
        self.dict_6 = {'name': 'oneplus', 'price': 5500,'category':'airpods','stockleft':150 }
        print("name:",end=" ")
        self.name="oneplus"
        print(self.name)
        print("price:",end=" ")
        self.price=5500
        print(self.price)
        print("category:",end=" ")
        self.category="airpods"
        print(self.category)
        print("stock left:",end=" ")
        print(self.dict_6["stockleft"])
    def gun(self):
        self.dict_7 = {'name': 'gun', 'price': 5500,'category':'toys','stockleft':210 }
        print("name:",end=" ")
        self.name="gun"
        print(self.name)
        print("price:",end=" ")
        self.price=5500
        print(self.price)
        print("category:",end=" ")
        self.category="toys"
        print(self.category)
        print("stock left:",end=" ")
        print(self.dict_7["stockleft"])
    def teddy(self):
        self.dict_8 = {'name': 'teddybear', 'price': 9500,'category':'toys','stockleft':150 }
        print("name:",end=" ")
        self.name="teddybear"
        print(self.name)
        print("price:",end=" ")
        self.price=9500
        print(self.price)
        print("category:",end=" ")
        self.category="toys"
        print(self.category)
        print("stock left:",end=" ")
        print(self.dict_8["stockleft"])
    def lists(self):
        self.list=[self.dict_1,self.dict_2,self.dict_3,self.dict_4,self.dict_5,self.dict_6,self.dict_7,self.dict_8]
        self.list1=[]
        self.list2=[]
    def buy(self):
        k=True
        while(k):
            self.buy=input("Enter the name of product which u want to Buy or Add to Cart:")
            for i in self.list:
                if self.buy==i["name"]:
                    prd_price=i["price"]
                    self.qun=int(input("Enter a Quantity:"))
                    if self.qun <= i['stockleft']:
                        print("---------------Bill--------------")
                        print("Amount:",end=" ")
                        print(prd_price*self.qun)
                        print("Delivery Cost:",end=" ")
                        self.delcost=100
                        print(self.delcost)
                        total=prd_price*self.qun+self.delcost
                        print("Total Amount:",end=" ")
                        print(total)
                        print("1.Place Order\n2.Add to Cart")
                        while True:
                          a=input("Enter an option:")
                          if a=="1":
                            print("Your order has been placed.\n!!!Thank u for purchasing!!!")
                            self.list1.append(self.buy)              
                            more=input("If u want to buy one more product(YES/NO):")
                            if(more=="YES"):
                               products.buy(self)
                            else:
                               print("!!!Thank u for choosing Amazon!!!")
                            break
                          elif a=="2":
                            print("Your product has added to cart.")
                            self.list2.append(self.buy)
                            look=input("If u want to buy or add to cart one more product(YES/NO):")
                            if(look=="YES"):
                                products.buy(self)
                            else:
                                exit=input("Are u sure u want to exit(YES/NO):")
                                if(exit=="YES"):
                                    print("!!!Thank u for choosing Amazon!!!")
                                else:
                                    products.buy(self)
                            break
                          else:
                            print("Invalid option.Please enter a valid option.")
                    else:
                        print("stock unavailable")
                    k=False
                    break
            else:
                print("Product not found.Please enter a valid name")
    def display(self):
        print("Displaying  list of products present in your Orders:")
        print(self.list1)
        print("Displaying your list of products present in Add to Cart:")
        print(self.list2)

import registration
import login
obj=products()
obj.iphone()
obj.vivo()
obj.puma()
obj.hrx()
obj.boat()
obj.oneplus()
obj.gun()
obj.teddy()
obj.lists()
obj.buy()
obj.display()
