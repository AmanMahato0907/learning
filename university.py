#online order processing system base class user,name and emailid,child class -customer,customerid,cart amt,use supet,methodchaining-addto cart,adpply discont,checkout.cretae a customer object,obsereve constructor chaining output perform order operation using method chaining ,print final  cart amt 
class user:
    def __init__(self,name,emailid):
        self.name=name
        self.emailid=emailid
        print("user name id ",self.name,self.emailid)
class customer(user):
    def __init__(self,name,emailid,customerid,cart_amt):
        super().__init__(name,emailid)
        self.customerid=customerid
        self.cart_amt=cart_amt
        print("customer name id ",self.customerid,self.cart_amt)
    def add_to_cart(self,amount):
        self.cart_amt+=amount
        return self
    def apply_discount(self,discount):
        self.cart_amt-=discount
        return self
    def checkout(self):
        print(f"Final cart amount for customer {self.customerid} is {self.cart_amt}")
        return self
cust1=customer("Alice","Amanmahat@gmail.com","C001",500)
cust1.add_to_cart(200).apply_discount(50).checkout()

