# from re import split
# from Module.FunctionManager.Function import Function
# from Module.PeopleManager.Employee import Employee
# from Module.PeopleManager.Person import Person


# people = [{"last_name": "Fury", "first_name": "Nick", "gender": True,
#            "wage": 3500.65, "company": "Hammond, Williams and Weberans Sons", "company_id": 1},
#           {"last_name": "Banner", "first_name": "Bruce", "gender": True,
#                          "wage": 2520.75, "company": "Hammond, Williams and Weberans Sons", "company_id": 1},
#           {"last_name": "Stark", "first_name": "Tony", "gender": True,
#                          "wage": 3020.35, "company": "Rodriguez Inc - Ltd", "company_id": 2},
#           {"last_name": "Parker", "first_name": "Peter", "gender": True,
#                          "wage": 2620.32, "company": "Rodriguez Inc - Ltd", "company_id": 2},
#           {"last_name": "Rogers", "first_name": "Steve", "gender": True,
#                          "wage": 2700.17, "company": "Barrett Incand", "company_id": 3},
#           {"last_name": "Strange", "first_name": "Stephen", "gender": True,
#                          "wage": 3206.15, "company": "Barrett Incand", "company_id": 3},
#           {"last_name": "Danvers", "first_name": "Carol", "gender": False,
#                          "wage": 3110.11, "company": "Olson ans Sons Group", "company_id": 4},
#           {"last_name": "Lauferson", "first_name": "Loki", "gender": True,
#                          "wage": 2800.25, "company": "Olson ans Sons Group", "company_id": 4},
#           {"last_name": "Ordinson", "first_name": "Thor", "gender": True,
#                          "wage": 3117.42, "company": "Stephens-Reyes - PLC", "company_id": 5},
#           {"last_name": "Kent", "first_name": "Clark", "gender": True,
#                          "wage": 3337.47, "company": "Stephens-Reyes - PLC", "company_id": 5},
#           {"last_name": "Wayne", "first_name": "Bruce", "gender": True,
#                          "wage": 4228.42, "company": "Cordova - Inc", "company_id": 6},
#           {"last_name": "Allen", "first_name": "Barry", "gender": True,
#                          "wage": 2728.76, "company": "Cordova - Inc", "company_id": 6},
#           {"last_name": "Prince", "first_name": "Diana", "gender": False,
#                          "wage": 2873.26, "company": "Hammond, Williams and Weberans Sons", "company_id": 1},
#           {"last_name": "Curry", "first_name": "Arthur", "gender": True,
#                          "wage": 2548.78, "company": "Rodriguez Inc - Ltd", "company_id": 2},
#           {"last_name": "Stone", "first_name": "Victor", "gender": True,
#                          "wage": 2769.34, "company": "Barrett Incand", "company_id": 3}
#           ]

# for i in range(10):
#     print(f"choix {i+1} : {Function.choose_in_list(people)}\n")
#     i+=1

import numpy as np
import matplotlib.pyplot as plt

"""un tableau x comprenant 10 points allant de 0 à 2"""
x = np.linspace(0, 2, 10)
"""un tableau y qui est le carré de x"""
y = x**2

plt.figure(figsize=(12,8))
plt.plot(x, y, c="yellow", lw="3", label="quadratique")
plt.plot(x, x**3, c="blue", lw="3", label="cubique")
plt.title("figure 1")
plt.xlabel("axe x")
plt.ylabel("axe y")
plt.legend()
plt.show()      
# plt.savefig("figure_1.png")

