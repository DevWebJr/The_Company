from Module.Individual.Person import Person
from Module.Individual.Employee import Employee
from Module.Institution.Company import Company
from Module.Equipment.Car import Car
from Module.Equipment.Office import Office
from Module.Data.Datas import Datas
from Module.Display.Graph import Graph
from Module.ExceptionManager.ExceptionManager import PeriodOutOfScopeError

import json
import random


class Simulation():
    def __init__(self):
        self._id = int

    ###Getters & Setters###
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def load_data_company(self):
        datas = Datas()
        datas.initialisation()
        return datas.list_of_companies

        # mise à jour des dépenses de chaque entreprise
        #for company in list_of_companies:
        #   company.update_outlay()
        # company.show_details()

    def choose_duration(self):
        duration = input("Nombre de périodes pour la simulation : ")
        try:
            duration_int = int(duration)
        except:
            duration_int = int(self.choose_duration())

        if duration_int < 0 or duration_int > 120:
            raise PeriodOutOfScopeError("Nombre incorrect")
        else:
            return duration_int

    def Simulation(self, list_of_companies, month):
        
        for company in list_of_companies:
            first_tab = []
            second_tab = []
            for i in range(month + 1):
                company.simulate_score()
                company.update_outlay()
                company.update_income()
                company.update_capital()

                # company.show_details()
                first_tab.append(company.capital)
                second_tab.append(i)

            graph = Graph()
            graph.show(first_tab, second_tab)

    def refresh_file(self, list_of_companies):
        list_of_people = []
        list_of_employees = []
        list_of_companies = []
        list_of_cars = []
        list_of_offices = []
        with open("datas.json") as file:
            datas = json.load(file)

            # création d'une liste de bureaux d'entreprise
            for company_offices_dict in datas['Office']:
                for value in company_offices_dict.values():
                    for about in value:
                        office = Office(
                            about["Price"], about["Rent"], about["Owner"], about["Occuppied"], about["Address"])
                        list_of_offices.append(office)

            # création d'une liste de voitures de fonction
            for company_cars_dict in datas['Car']:
                for value in company_cars_dict.values():
                    for about in value:
                        car = Car(about["Price"], about["Rent"],
                                  about["Owner"], about["Occupied"])
                        list_of_cars.append(car)

            # création d'une liste de personnes hors entreprise
            for people_dict in datas['Person']:
                for value in people_dict.values():
                    for about in value:
                        person = Person(about["LastName"], about["FirstName"], 
                                        about["Gender"])
                        list_of_people.append(person)

            # création d'une liste d'entreprises
            for companies_dict in datas['Company']:
                for value in companies_dict.values():
                    for about in value:
                        company = Company(
                            about["Name"], about["Address"], about["Outlay"])
                        list_of_companies.append(company)

            # création d'une liste d'employés
            for employees_dict in datas['Employee']:
                for value in employees_dict.values():
                    for about in value:
                        employee = Employee(about["LastName"], about["FirstName"], 
                                            about["Gender"], about["Wage"], 
                                            about["company"], about["company_id"])
                        list_of_employees.append(employee)

        # Ajouter les employées, les bureaux et les voitures respectivement à chaque entreprise
        for company in list_of_companies:
            for employee in list_of_employees:
                if employee.company == company.name:
                    company.hire(employee)

            for office in list_of_offices:
                if office.owner == company.name:
                    company.buy_office(office)

            for car in list_of_cars:
                if car.owner == company.name:
                    company.buy_car(car)

            company.update_outlay()

        # mise à jour des dépenses de chaque entreprise
        for company in list_of_companies:
            company.update_outlay()
            # company.show_details()

        return list_of_companies

    ######################
    ####| SIMULATION |####
    ######################

    def simulate(self, list_of_companies, month):
        for company in list_of_companies:
            first_tab = []
            second_tab = []
            for i in range(month+1):
                company.workers()
                company.update_outlay()
                company.update_income(random.randint(6000, 10000))
                company.update_capital()

                # company.show_details()
                first_tab.append(company.capital)
                second_tab.append(i)

            graph = Graph()
            graph.show(first_tab, second_tab)
