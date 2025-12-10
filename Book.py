class Book:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price
        
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, cost):
        if cost < 0:
            raise ValueError("Cost must be above 0")
        self.__price = cost
        
    def info(self):
        return f"Title: {self.__title} | Price: {self.price}"