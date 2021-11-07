class Institution():
    """
    Cette classe permet l'instanciation d'institutions.
    """
    def __init__(self, name, address):
        self._id = id
        self._name = name
        self._address = address

    """Getters & Setters"""
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    """Methods"""
