#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Fruit:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class FruitStore:
    def __init__(self, fruits):
        self.fruits = fruits

    def calculate_total_price(self):
        total_price = 0
        for fruit in self.fruits:
            if fruit.name == "apple":
                total_price += fruit.quantity * 2
            elif fruit.name == "banana":
                total_price += fruit.quantity * 1.5
            elif fruit.name == "orange":
                total_price += fruit.quantity * 3
            
        return total_price

fruits = [Fruit("apple", 2), Fruit("banana", 3), Fruit("orange", 1)]
store = FruitStore(fruits)
print(store.calculate_total_price())


# In[ ]:




