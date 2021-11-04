from Module.Individual.Person import Person
from Module.ExceptionManager.ExceptionManager import AccessRightError


class Employee(Person):
    """
    Classe héritée de la Classe Person, permettant d'instancier des employées.
    """
    def __init__(self, last_name, first_name, gender, wage, score, company, company_id):
        Person.__init__(last_name, first_name, gender)
        self._wage = wage
        self._score = score
        self._company = company
        self._company_id = company_id

    """Getters & Setters"""
    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, value):
        self._wage = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value

    """Methods"""
    def modify_wage(self, amount, boss):
        if isinstance(boss, Boss):
            boss.upgrade_wage(amount, self)
        else:
            raise AccessRightError("Only a boss can be so generous.")

    def modify_score(self, points, boss):
        if isinstance(boss, Boss):
            boss.upgrade_score(points, self)
        else:
            raise AccessRightError("Only a boss can be so generous.")

    def join_a_company(self, company, company_id):
        self.company = company      
        self.company_id = company_id  
        
    def quit_a_company(self):
        self.company = None
        
    def job_is_done(self):
        self.score += 5        

    def job_is_not_done(self):
        self.score -= 5
    
    def check_score(self):
        if self.score > 100:
            satisfaction = True
            print("Bien")
        elif self.score < 40:
            satisfaction = False
            print("Pas Bien")
            self.quit()
        else:
            satisfaction = True
            print("Rien")
        return satisfaction
    
    def show_employee_details(self):
        print(f"\nDétails Salarié :"
            f"\nSalaire mensuel : {self.wage} €"
            f"\nSatisfaction du PDG : {self.score}\n")


class Boss(Employee):
    """
    Classe héritée de la Classe Employee, permettant d'instancier des Boss.
    """
    def __init__(self, last_name, first_name, gender, wage, score, company, company_id):
        super().__init__(last_name, first_name, gender, wage, score, company, company_id)

    """Methods"""
    def upgrade_wage(self, bonus, employee):
        employee.wage = employee.wage + bonus

    def upgrade_score(self, bonus, employee):
        employee.score = employee.score + bonus
