class Furniture():
    def __init__(self, price, rent, available:bool = True):
        self._id = id
        self._price = price
        self._rent = rent
        self._available = available
        self._owner = None

    ###Getters & Setters###
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    ###Methods###
    def is_available(self):
        if self.available:
            print("Disponible")
        else:
            self.price = None
            print("Non Disponible")

    def has_owner(self):
        if self.owner == None:
            return False
        else:
            return True