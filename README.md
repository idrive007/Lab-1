# Звіт з лабораторної роботи №1. Довгий метод.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
### Мета: Аналіз та оптимізація довгих методів.

### За основу довгого коду було взято метод "calculate_total_price", що обчислює загальну вартість всіх фруктів у магазині. 
### Він перебирає кожен фрукт у списку фруктів, викликає метод calculate_price для кожного фрукту і додає отримані ціни до загальної вартості. Після цього він повертає загальну вартість.

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


### 1. Опис проблеми
### В класі FruitStore метод calculate_total_price є довгим і містить багато умовних перевірок, що робить його складним для розуміння та може призводити до помилок при додаванні нових типів фруктів.
### Крім того, цей підхід не є розширюваним, оскільки при додаванні нового типу фрукту потрібно буде змінювати сам клас FruitStore.

### 2. Аналіз проблеми
### Проблема полягає в тому, що логіка обчислення ціни кожного типу фруктів розсіяна у методі calculate_total_price, що порушує принцип єдиної відповідальності.

### 3. Оптимізація методу
### Замість того, щоб мати умовні перевірки всередині методу calculate_total_price, створюємо окремий метод для кожного типу фруктів. 
### Також використовуємо поліморфізм для обчислення ціни кожного типу фруктів.

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
    
### Отже, використовано декілька технік рефакторінгу для покращення коду:
1. Поліморфізм: Клас Fruit визначає загальний інтерфейс для всіх типів фруктів, а підкласи, такі як Apple, Banana і Orange, реалізують конкретну логіку обчислення ціни для кожного типу фруктів.
2. Абстракція: Метод calculate_price у класі Fruit є абстрактним і викидає виключення NotImplementedError, тим самим забезпечуючи, що кожен підклас фрукта має реалізувати свою власну логіку обчислення ціни.
3. Використання заміни методу об'єктом методів: У методі calculate_total_price класу FruitStore замість умовних перевірок використовується поліморфний виклик методу calculate_price для кожного об'єкта фрукта. Це дозволяє уникнути дублювання коду та зробити його більш чистим та зрозумілим.

### 4. Результати
### Тестування оновленого методу показує, що він працює коректно, а також робить код більш розширюваним та зрозумілим. 
### Замість довгих умовних перевірок у методі calculate_total_price, застосовано поліморфізм, що дозволяє кожному типу фруктів реалізувати свій власний метод для обчислення ціни. 
