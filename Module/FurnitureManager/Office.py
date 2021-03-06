from Module.FurnitureManager.Furniture import Furniture


class Office(Furniture):
    def __init__(self, price, rent, available, address):
        super().__init__(price, rent, available)
        self._address = address

    ###Getters & Setters###
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    ###Methods###
    def show_office_details(self):
        details = f"\nDétails Bureau :\n{self.price}\n({self.rent}/mensuel)\nPropriétaire : {self.owner}\n({self.has_owner()})\n{self.address}"
        return details
