import random

class Function():
    def __init__(self):
        self._id = id
    
    """Getters & Setters"""
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    """return an object from a list using a random choice"""
    def choose_in_list(the_list):
        the_target = random.randrange(1, len(the_list))
        the_choice = the_list[the_target]
        return the_choice
