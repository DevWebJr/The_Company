from Module.PeopleManager.Person import Person
from Module.PeopleManager.Employee import Employee
from Module.InstitutionManager.Company import Company
from Module.FurnitureManager.Car import Car
from Module.FurnitureManager.Office import Office
from Module.DataManager.CompanyData import CompanyData
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
        datas = CompanyData()
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

    def start(self, list_of_companies, month):
        
        for company in list_of_companies:
            first_tab = []
            second_tab = []
            for i in range(month + 1):
                company.simulate_score()
                company.update_outlay()
                company.update_income(company.income)
                company.update_capital()

                # company.show_details()
                first_tab.append(company.capital)
                second_tab.append(i)

            title = f"{company.name.upper()}"
            x_label = f"Étude réalisée sur une période de {int(month)} mois"
            y_label = "Capital"
            figsize = (10, 8)
            graph = Graph(title, x_label, y_label, figsize)
            name = company.name
            graph.show(first_tab, second_tab, name)

    def import_datas_from_json(self, list_of_companies):
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
                            about["Price"], about["Rent"], about["Available"], about["Owner"], about["Address"])
                        list_of_offices.append(office)

            # création d'une liste de voitures de fonction
            for company_cars_dict in datas['Car']:
                for value in company_cars_dict.values():
                    for about in value:
                        car = Car(about["Price"], about["Rent"], about["Available"], about["Owner"])
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