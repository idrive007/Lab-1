#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Fruit:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def calculate_price(self):
        raise NotImplementedError("Підкласи повинні реалізовувати метод calculate_price")


class Apple(Fruit):
    def calculate_price(self):
        return self.quantity * 2


class Banana(Fruit):
    def calculate_price(self):
        return self.quantity * 1.5


class Orange(Fruit):
    def calculate_price(self):
        return self.quantity * 3


class FruitStore:
    def __init__(self, fruits):
        self.fruits = fruits

    def calculate_total_price(self):
        total_price = 0
        for fruit in self.fruits:
            total_price += fruit.calculate_price()
        return total_price


fruits = [Apple("apple", 2), Banana("banana", 3), Orange("orange", 1)]
store = FruitStore(fruits)
print(store.calculate_total_price())



# In[ ]:




