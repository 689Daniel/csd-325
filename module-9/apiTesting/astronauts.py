#Daniel Preller, 23 July 2025, Assignment 9.2
#Program to show the astronauts currently in space using an API

import requests, json

response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)
#Connection test


def json_print(json_object):# Prints a formatted JSON string
    text = json.dumps(json_object, sort_keys=True, indent=4)
    print(text)

json_print(response.json())# Prints results