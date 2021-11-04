from Module.Individual.Employee import Employee
from Module.Institution.Company import Company
from Module.Individual.Person import Person
from Module.Equipment.Car import Car
from Module.Equipment.Office import Office
from Module.Equipment.Furniture import Furnitures
from Module.Display.Graph import BaseGraph, BalanceGraph
from Module.Display.Graph import BalanceGraph
from Module.ExceptionManager.ExceptionManager import PeriodOutOfScopeError
from Module.Data.Datas import Datas

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
        return datas.list_company

        # mise à jour des dépenses de chaque entreprise
        #for company in list_company:
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

    # SIMULATION SUR 12 ITERATIONS - SYSTEM DE RATING

    def Simulation(self, list_company, month):
        for company in list_company:
            pass
        #graph1 = BalanceGraph(company.name)
        #graph2 = BalanceGraph()
        #graph3 = BalanceGraph

        for company in list_company:
            tab = []
            tab2 = []
            for i in range(month + 1):
                company.mix_workers()
                company.update_outlay()
                company.update_income()
                company.update_capital()

                # company.show_details()
                tab.append(company.capital)
                tab2.append(i)

            final = BalanceGraph()
            final.show(tab, tab2)

    def refresh_file(self, list_company):
        list_employee = []
        list_company = []
        list_person = []
        list_car = []
        list_office = []
        with open("data.json") as my_file:
            data = json.load(my_file)

            # création d'une liste de bureaux d'entreprise
            for company_office_dict in data['company_Office']:
                for value in company_office_dict.values():
                    for about in value:
                        office = Office(
                            about["Name"], about["Price"], about["Owner"], about["Rent"])
                        list_office.append(office)

            # création d'une liste de voitures de fonction
            for company_car_dict in data['company_Car']:
                for value in company_car_dict.values():
                    for about in value:
                        car = Car(about["Model"], about["Plate_Number"],
                                  about["Price"], about["charge"], about["Owner"])
                        list_car.append(car)

            # création d'une liste de personnes hors entreprise
            for person_dict in data['Person']:
                for value in person_dict.values():
                    for about in value:
                        person = Person(about["LastName"], about["FirstName"], about["Age"], about["Adress"],
                                        about["Phone"], about["Mail"])
                        list_person.append(person)

            # création d'une liste d'entreprises
            for company_dict in data['Company']:
                for value in company_dict.values():
                    for about in value:
                        company = Company(about["Name"])
                        list_company.append(company)

            # création d'une liste d'employés
            for employee_dict in data['Employee']:
                for value in employee_dict.values():
                    for about in value:
                        employee = Employee(about["LastName"], about["FirstName"], about["Age"], about["Adress"],
                                            about["Phone"], about["Mail"], about["company_id"], about["Wage"],
                                            about["company"])
                        list_employee.append(employee)

        # Ajouter les employées, les bureaux et les voitures respectivement à chaque entreprise
        for company in list_company:
            for employee in list_employee:
                if employee.company == company.name:
                    company.hire(employee)

            for office in list_office:
                if office.owner == company.name:
                    company.buy_office(office)

            for car in list_car:
                if car.owner == company.name:
                    company.buy_car(car)

            company.update_outlay()

        # mise à jour des dépenses de chaque entreprise
        for company in list_company:
            company.update_outlay()
            # company.show_details()

        return list_company

    ###########################################################
    ###| SIMULATION SUR 12 ITERATIONS - SYSTEME DE RATING |####
    ###########################################################

    def simulate(self, list_company, month):
        for company in list_company:
            tab = []
            tab2 = []
            for i in range(month+1):
                company.workers()
                company.update_outlay()
                company.update_income(random.randint(6000, 10000))
                company.update_capital()

                # company.show_details()
                tab.append(company.capital)
                tab2.append(i)

            final = BalanceGraph()
            final.show(tab, tab2)
