import csv

class Item:

    pay_rate=0.8 #Class Atrribute
    all = []

    def __init__(self, name: str,price: float,quantity=0):

        #Run Validations to recieved arguments
        assert price >= 0 , f"Price {price} not GTE 0"
        assert quantity >= 0 , f"Quantity {quantity} not GTE 0"

        #Assign to self object
        self.name=name
        self.quantity=quantity
        self.price=price

        Item.all.append(self)
    
    def calculate_total_price(self):
        self.tp= self.quantity*self.price
        return self.tp
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate #Item.pay_rate
        return self.price
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader= csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name= item.get('name'),
                price= float(item.get('price')),
                quantity= int(item.get('quantity'))
            )


    
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
    
Item.instantiate_from_csv()
print(Item.all)


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)
    

# item1= Item("Phone",5000,50)
# item2= Item("Laptop",150000)
# # item3= Item(1,2,"jk")
# # item4= Item("Box",-1,-2)
# item5= Item("Tablet",50000,4)


# item2.has_keypad = False
# item5.pay_rate= 0.5

# print(item2.has_keypad)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item5.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)
# print(item2.__dict__)
# print(item5.__dict__)
# print(item1.apply_discount())
# print(item5.apply_discount())