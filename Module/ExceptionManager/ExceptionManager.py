class AccessRightError(Exception):
    """
    Classe héritée de la Classe Exception, permettant de gérer une erreur de droit d'accès à la fonction modify_wage().
    """
    pass


class PeriodOutOfScopeError(Exception):
    """
    Classe héritée de la Classe Exception, permettant de gérer la durée maximale liée à la fonction choose_a_period().
    """
    pass
