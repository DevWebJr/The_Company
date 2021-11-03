####################
###jeu de données###
####################

# plusieurs employés:
employee_01 = {"id": 1, "last_name": "Fury", "first_name": "Nick", "gender": True,
               "wage": 3500.65, "firm": "Hammond, Williams and Weberans Sons", "firm_id": 1, "role": True, "service_vehicle": True}
employee_02 = {"id": 2, "last_name": "Banner", "first_name": "Bruce", "gender": True,
               "wage": 2520.75, "firm": "Hammond, Williams and Weberans Sons", "firm_id": 1, "role": False, "service_vehicle": False}
employee_03 = {"id": 3, "last_name": "Stark", "first_name": "Tony", "gender": True,
               "wage": 3020.35, "firm": "Rodriguez Inc - Ltd", "firm_id":2, "role": False, "service_vehicle": False}
employee_04 = {"id": 4, "last_name": "Parker", "first_name": "Peter", "gender": True,
               "wage": 2620.32, "firm": "Rodriguez Inc - Ltd", "firm_id":2, "role": False, "service_vehicle": False}
employee_05 = {"id": 5, "last_name": "Rogers", "first_name": "Steve", "gender": True,
               "wage": 2700.17, "firm": "Barrett Incand", "firm_id": 3, "role": False, "service_vehicle": False}
employee_06 = {"id": 6, "last_name": "Strange", "first_name": "Stephen", "gender": True,
               "wage": 3206.15, "firm": "Barrett Incand", "firm_id": 3, "role": False, "service_vehicle": False}
employee_07 = {"id": 7, "last_name": "Danvers", "first_name": "Carol", "gender": False,
               "wage": 3110.11, "firm": "Olson ans Sons Group", "firm_id": 4, "role": False, "service_vehicle": False}
employee_08 = {"id": 8, "last_name": "Lauferson", "first_name": "Loki", "gender": True,
               "wage": 2800.25, "firm": "Olson ans Sons Group", "firm_id": 4, "role": False, "service_vehicle": False}
employee_09 = {"id": 9, "last_name": "Ordinson", "first_name": "Thor", "gender": True,
               "wage": 3117.42, "firm": "Stephens-Reyes - PLC", "firm_id": 5, "role": False, "service_vehicle": False}
employee_10 = {"id": 10, "last_name": "Kent", "first_name": "Clark", "gender": True,
               "wage": 3337.47, "firm": "Stephens-Reyes - PLC", "firm_id": 5, "role": False, "service_vehicle": False}
employee_11 = {"id": 11, "last_name": "Wayne", "first_name": "Bruce", "gender": True,
               "wage": 4228.42, "firm": "Cordova - Inc", "firm_id": 6, "role": True, "service_vehicle": True}
employee_12 = {"id": 12, "last_name": "Allen", "first_name": "Barry", "gender": True,
               "wage": 2728.76, "firm": "Cordova - Inc", "firm_id":6, "role": False, "service_vehicle": False}
employee_13 = {"id": 13, "last_name": "Prince", "first_name": "Diana", "gender": False,
               "wage": 2873.26, "firm": "Hammond, Williams and Weberans Sons", "firm_id": 1, "role": False, "service_vehicle": False}
employee_14 = {"id": 14, "last_name": "Curry", "first_name": "Arthur", "gender": True,
               "wage": 2548.78, "firm": "Rodriguez Inc - Ltd", "firm_id": 2, "role": False, "service_vehicle": False}
employee_15 = {"id": 15, "last_name": "Stone", "first_name": "Victor", "gender": True,
               "wage": 2769.34, "firm": "Barrett Incand", "firm_id": 3, "role": False, "service_vehicle": False}


# plusieurs firmes avec des employés:
# avengers = {"employees": [employee_01, employee_02, employee_03, employee_04,
#                           employee_05, employee_06, employee_07, employee_08, employee_09]}
# justice_league = {"employees": [
#     employee_10, employee_11, employee_12, employee_13, employee_14, employee_15]}

# plusieurs voitures
car_01 = {"id": 1,"cost": 4500,"owner": False,"availability": False,"color": "green", "occupied": False}
car_02 = {"id": 2,"cost": 3250,"owner": False,"availability": False,"color": "red", "occupied": False}
car_03 = {"id": 3,"cost": 7690,"owner": False,"availability": False,"color": "yellow", "occupied": False}
car_04 = {"id": 4,"cost": 4609,"owner": False,"availability": False,"color": "white", "occupied": False}
car_05 = {"id": 5,"cost": 3284,"owner": False,"availability": False,"color": "black", "occupied": False}

# plusieurs bureaux
office_01 = {"id": 1,"cost": 22690,"owner": False,"availability": False,"address": "48 Kerry Way - Gardena - 90248 | California"}
office_02 = {"id": 2,"cost": 33045,"owner": False,"availability": False,"address": "684 Grasselli Street - West Lebanon - 03784 | New Hampshire"}
office_03 = {"id": 3,"cost": 52896,"owner": False,"availability": False,"address": "3460 Highland View Drive - Elk Grove - 95624 | California"}
office_04 = {"id": 4,"cost": 34514,"owner": False,"availability": False,"address": "3767 Ocala Street - Orlando - 32803 | Florida"}
office_05 = {"id": 5,"cost": 34514,"owner": False,"availability": False,"address": "1526 Calico Drive - Wenatchee - 98801 | Washington"}
office_06 = {"id": 6,"cost": 55046,"owner": False,"availability": False,"address": "4652 Pennsylvania Avenue - Lyndhurst - 07071 | New Jersey"}
office_07 = {"id": 7,"cost": 33045,"owner": False,"availability": False,"address": "3369 Prospect Street - Perkins - 63774 | Missouri"}
office_08 = {"id": 8,"cost": 52896,"owner": False,"availability": False,"address": "558 Caldwell Road - Buffalo - 14216 | New York"}
office_09 = {"id": 9,"cost": 34514,"owner": False,"availability": False,"address": "1306 Doe Meadow Drive - Beltsville - 20705 | Maryland"}
office_10 = {"id": 10,"cost": 55046,"owner": False,"availability": False,"address": "2522 Still Pastures Drive - Charlotte - 28202 | South Carolina"}

# plusieurs firmes
firm_01 = {"id": 1, "name": "Hammond, Williams and Weberans Sons","address": "492 Stone Court - Gardena - 90248 | California", "outlay": 0}
firm_02 = {"id": 2, "name": "Rodriguez Inc - Ltd","address": "70163 Jacobs Rapids - West Lebanon - 03784 | New Hampshire", "outlay": 0}
firm_03 = {"id": 3, "name":"Barrett Incand", "address":"56913 Mooney Port - Elk Grove - 95624 | California", "outlay":0}
firm_04 = {"id": 4, "name":"Olson ans Sons Group", "address":"41124 Mitchell Park - Orlando - 32803 | Florida", "outlay":0}
firm_05 = {"id": 5, "name":"Stephens-Reyes - PLC", "address":"5653 Farley Fall - Wenatchee - 98801 | Washington", "outlay":0}
firm_06 = {"id": 6, "name":"Cordova - Inc", "address":"344 Gordon View - Lyndhurst - 07071 | New Jersey", "outlay":0}