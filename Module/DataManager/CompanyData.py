from Module.InstitutionManager.Company import Company
from Module.FurnitureManager.Office import Office
from Module.FurnitureManager.Car import Car
from Module.PeopleManager.Person import Person
from Module.PeopleManager.Employee import Employee
import json

class CompanyData():
    def __init__(self):
        self._list_of_people = []
        self._list_of_employees = []
        self._list_of_companies = []
        self._list_of_cars = []
        self._list_of_offices = []

    """Getters & Setters"""
    @property
    def list_of_people(self):
        return self._list_of_people

    @list_of_people.setter
    def list_of_people(self, value):
        self._list_of_people = value

    @property
    def list_of_employees(self):
        return self._list_of_employees

    @list_of_employees.setter
    def list_of_employees(self, value):
        self._list_of_employees = value

    @property
    def list_of_companies(self):
        return self._list_of_companies

    @list_of_companies.setter
    def list_of_companies(self, value):
        self._list_of_companies = value

    @property
    def list_of_cars(self):
        return self._list_of_cars

    @list_of_cars.setter
    def list_of_cars(self, value):
        self._list_of_cars = value

    @property
    def list_of_offices(self):
        return self._list_of_offices

    @list_of_offices.setter
    def list_of_offices(self, value):
        self._list_of_offices = value

    """Methods"""
    def initialisation(self):
        # self.get_people()
        self.get_employees()
        self.get_companies()
        self.get_cars()
        self.get_offices()
        self.load()

    # def get_people(self):
    #     with open("all_datas.json") as my_file:
    #         datas = json.load(my_file)
    #         # création d'une liste de personnes hors entreprise
    #         for person_dict in datas['Person']:
    #             for value in person_dict.values():
    #                 for about in value:
    #                     person = Person(about["LastName"], about["FirstName"], about["Gender"])
    #                     self.list_of_people.append(person)

    def get_employees(self):
        with open("all_datas.json") as my_file:
            datas = json.load(my_file)
            # création d'une liste d'employés
            for employee_dict in datas['Employee']:
                for value in employee_dict.values():
                    for about in value:
                        employee = Employee(about["last_name"], about["first_name"], about["gender"], about["wage"], about["company"], about["company_id"])
                        self.list_of_employees.append(employee)
                        
    def get_companies(self):
        with open("all_datas.json") as my_file:
            datas = json.load(my_file)
            # création d'une liste d'entreprises
            for firm_dict in datas['Company']:
                for value in firm_dict.values():
                    for about in value:
                        company = Company(
                            about['name'], about['address'], about['outlay'])
                        self.list_of_companies.append(company)
                        
    def get_cars(self):
        with open("all_datas.json") as my_file:
            datas = json.load(my_file)
            # création d'une liste de voitures de fonction
            for firm_car_dict in datas['Car']:
                for value in firm_car_dict.values():
                    for about in value:
                        car = Car(about["price"], about["rent"], about["available"], about["owner"])
                        self.list_of_cars.append(car)

    def get_offices(self):
        with open("all_datas.json") as my_file:
            datas = json.load(my_file)
            # création d'une liste de bureaux d'entreprise
            for firm_office_dict in datas['Office']:
                for value in firm_office_dict.values():
                    for about in value:
                        office = Office(
                            about["price"], about["rent"], about["available"], about["owner"], about["address"])
                        self.list_of_offices.append(office)

    def export_datas_to_json(self):
        with open("datas.json", 'w', encoding='utf-8') as my_file:
            datas = json.load(my_file)
            datas.dump(self)

    def load(self):
        # Ajouter les employées, les bureaux et les voitures respectivement à chaque entreprise
        for company in self.list_of_companies:
            for employee in self.list_of_employees:
                if employee.company == company.name:
                    company.hire(employee)

            for office in self.list_of_offices:
                if office.owner == company.name:
                    company.buy_office(office)

            for car in self.list_of_cars:
                if car.owner == company.name:
                    company.buy_car(car)
