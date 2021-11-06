class Person():
    """
    This Class implements Person Objects.
    """

    def __init__(self, last_name:str ="", first_name:str ="", gender: bool = True):
        self._last_name = last_name
        self._first_name = first_name
        self._gender = gender

    """Getters & Setters"""
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    """Methods"""
    def get_gender_str(self):
        if self.gender == True:
            gender_str = f"Homme"
        else:
            gender_str = f"Femme"
        return gender_str

    def show_details(self):
        gender_str = "Homme" if self.gender else "Femme"
        details = f"{self.last_name} {self.first_name} ({gender_str})"
        return details
