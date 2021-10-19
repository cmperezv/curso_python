#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

dicc = {}
dicc["Peticion"] = {}
dicc["Peticion"]["Comunicacion1"] = {}
dicc["Peticion"]["Comunicacion1"]["PhoneNumber"] = 666666666
dicc["Peticion"]["Comunicacion2"] = {}
dicc["Peticion"]["Comunicacion2"]["PhoneNumber"] = 677666555
dicc["Peticion"]["Comunicacion3"] = {}
dicc["Peticion"]["Comunicacion3"]["PhoneNumber"] = 655888898

print(dicc)

app_json = json.dumps(dicc)
print(app_json)
