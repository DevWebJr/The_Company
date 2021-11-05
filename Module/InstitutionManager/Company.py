from Module.FurnitureManager.Car import Car
from Module.InstitutionManager.Institution import Institution
from Module.PeopleManager.Employee import Employee
from Module.FurnitureManager.Office import Office
import random


class Company(Institution):
    """
    Cette classe héritée de la classe Institution permet l'instanciation de Company.
    """
    def __init__(self, name, address, outlay):
        super().__init__(name, address)
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
    """return details about all employees"""
    def show_employees(self):
        for employee in self.list_of_employees:
            employee.show_employee_details()
            
    """return details about all offices"""
    def show_offices(self):
        for office in self.list_of_offices:
            office.show_office_details()

    """return details about all cars"""
    def show_cars(self):
        for car in self.list_of_cars:
            car.show_car_details()

    """calculation of all taxes"""
    def update_outlay(self):
        value = 0
        for employee in self.list_of_employees:
            value -= employee.wage
        for office in self.list_of_offices:
            value -= office.rent
        for car in self.list_of_cars:
            value -= car.rent

    """update income when necessary"""
    def update_income(self, income):
        self.income = income
        
    """update capital after all taxes"""
    def update_capital(self):
        self.capital = int(self.capital) + int(self.income) + int(self.outlay)

    """hire an employee"""
    def hire(self, employee: Employee):
        self.list_of_employees.append(employee)
    
    """fire an employee"""
    def fire(self, target: Employee):
        for employee in self.list_of_employees:
            if target == employee:
                self.list_of_employees.remove(employee)      
    
    """return list of all availables cars"""
    def get_list_of_availables_cars(self):
        availables_cars = []
        if self.list_of_cars != None:
            for car in self.list_of_cars:
                if car.has_owner() == False:
                    availables_cars.append(car)
        else:
            print("Plus aucune voiture disponible.")
        return availables_cars

    """return a car using a random choice in list"""
    def choose_car_in_list(self):
        availables_cars = self.get_list_of_availables_cars()
        numero = random.randrange(1, len(availables_cars))
        car = availables_cars[numero]
        return car    
    
    """attribute one car to one employee"""
    def assign_a_car(self,car:Car, employee: Employee):
        if car.has_owner() == False:
            car.has_owner() == True
            car.owner = employee
            self.get_list_of_availables_cars().remove(car) 
            
    """simulation of scores and their issues"""
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
    def buy_office(self, office: Office):
        self.list_of_offices.append(office)
        self.capital -= office.rent

    #sell
    def sell_office(self, sold_office: Office):
        for office in self.list_of_offices:
            if office == sold_office:
                self.list_of_offices.remove(office)
                self.capital += office.rent/0.90

    ##cars##
    #buy
    def buy_car(self, car: Car):
        self.list_of_cars.append(car)
        self.capital -= car.rent

    #sell
    def sell_car(self, sold_car: Car):
        for car in self.list_of_cars:
            if sold_car == car:
                self.list_of_cars.remove(car)
                self.capital += car.rent/0.90
