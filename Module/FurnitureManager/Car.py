from Module.FurnitureManager.Furniture import Furniture


class Car(Furniture):
    def __init__(self, price, rent, available):
        super().__init__(price, rent, available)
        self._car_company = None

    ###Getters & Setters###
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, value):
        self._rent = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def car_company(self):
        return self._car_company

    @car_company.setter
    def car_company(self, value):
        self._car_company = value

    ###Methods###
    def sold_to_a_company(self, company):
        self._car_company = company.name
        company.list_of_cars.append(self)

    def show_car_details(self):
        details = f"\nDétails Véhicule :\n{self.price}\n({self.rent}/mensuel)\nPropriétaire : {self.owner}\n({self.has_owner()})"
        return details
