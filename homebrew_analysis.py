import requests
import json
from json import JSONDecodeError


while True:
    print("Welcome to JSON reader. You can check how many times a certain package has been installed using Homebrew. You will receive a results from last 30, 90 and 365 days")
    package_name = input("Enter a package name: ")

    try:
        #getting a json data from the package 
        r = requests.get(f'https://formulae.brew.sh/api/formula/{package_name}.json')

        #converting it into a python dictionary
        r_data = r.json()

        

        #getting data from last 30, 90 and 365 days
        r_days = r_data['analytics']['install']

        _30d = r_days['30d'][f"{package_name}"]
        _90d = r_days['90d'][f"{package_name}"]
        _365d = r_days['365d'][f"{package_name}"]

        print(f"The {package_name} has been installed: \n {_30d} times in the last 30 days, \n {_90d} times in the last 90 days, \n {_365d} times in the last 365 days, ")

        #Creating a new python dictionary that contains all the generated data:

        homebrew_installation = {
                "Installation": [
                {"30d": f"{_30d}"},
                {"90d": f"{_90d}"},
                {"365d": f"{_365d}"},

                ]
        }

        #Converted homebrew_installation dictionary to json format
        installation_string = json.dumps(homebrew_installation)

        print(installation_string)

    except JSONDecodeError:
        print("Package not found, please try again.")
       
