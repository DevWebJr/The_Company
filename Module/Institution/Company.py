from Module.Institution.Institution import Institution
from Module.Individual.Employee import Employee
import random


class Company(Institution):
    """
    Cette classe héritée de la classe Institution permet l'instanciation de Company.
    """
    def __init__(self, name, address, outlay):
        Institution.__init__(name, address)
        self._outlay = outlay
        self._income = 0
        self._capital = 0
        self._list_of_employees = []
        self._list_of_cars = []
        self._list_of_offices = []

    """Getters & Setters"""
    @property
    def outlay(self):
        return self._outlay

    @outlay.setter
    def outlay(self, value):
        self._outlay = value

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, value):
        self._income = value

    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, value):
        self._capital = value

    @property
    def list_of_employees(self):
        return self._list_of_employees

    @list_of_employees.setter
    def list_of_employees(self, value):
        self._list_of_employees = value

    @property
    def list_of_offices(self):
        return self._list_of_offices

    @list_of_offices.setter
    def list_of_offices(self, value):
        self._list_of_offices = value

    @property
    def list_of_cars(self):
        return self._list_of_cars

    @list_of_cars.setter
    def list_of_cars(self, value):
        self._list_of_cars = value

    """Methods"""
    ###about the company###
    ##all of lists##
    def show_employees(self):
        for employee in self.list_of_employees:
            employee.show_details()

    def show_offices(self):
        for office in self.list_of_offices:
            office.show_details()

    def show_cars(self):
        for car in self.list_of_cars:
            car.show_details()

    ##outlay##
    def update_outlay(self):
        value = 0
        for employee in self.list_of_employees:
            value -= employee.wage
        for office in self.list_of_offices:
            value -= office.cost
        for car in self.list_of_cars:
            value -= car.cost

    ##income##
    def update_income(self, income):
        self.income = income
        
    ##capital##
    def update_capital(self):
        self.capital = self.capital + self.income + self.outlay

    ##employees##
    def hire(self, employee):
        self.list_of_employees.append(employee)
    
    def fire(self, target):
        for employee in self.list_of_employees:
            if target == employee:
                self.list_of_employees.remove(employee)       
    
    def simulate_score(self):
        for employee in self._list_of_employees:
            mood = random.randint(0, 3)
            if mood >= 1:
                employee.job_is_done()
            if mood == 0:
                employee.job_is_not_done()
            if not employee.check_score():
                self.fire(employee)
                
    ##offices##
    #buy
    def buy_office(self, office):
        self.list_of_offices.append(office)
        self.capital -= office.rent

    #sell
    def sell_office(self, sold_office):
        for office in self.list_of_offices:
            if office == sold_office:
                self.list_of_offices.remove(office)
                self.capital += office.rent/0.90

    ##cars##
    #buy
    def buy_car(self, car):
        self.list_of_cars.append(car)
        self.capital -= car.rent

    #sell
    def sell_car(self, sold_car):
        for car in self.list_of_cars:
            if sold_car == car:
                self.list_of_cars.remove(car)
                self.capital += car.rent/0.90
