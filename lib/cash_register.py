#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self,prod_name, prod_cost, quantity = 1):
            self.cart = prod_cost * quantity
            self.total += self.cart
            for x in range(quantity):
                self.items.append(prod_name)
      
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = int((self.discount/100) * self.total)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:}.")
        else:
            print("There is no discount to apply.")
        
    def void_last_transaction(self):
            self.total -= self.cart
            return self.total 
    
        


    
    

