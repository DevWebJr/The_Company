class Furniture():
    def __init__(self, price, rent):
        self._price = price
        self._rent = rent

    ###Getters & Setters###
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, price):
        self._rent = price
