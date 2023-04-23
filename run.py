# imported libraries
import os
from dotenv import load_dotenv
from pyfiglet import Figlet
from colorama import Style, Fore
from pymongo import MongoClient
from pymongo.errors import OperationFailure

# Loads the .env file's hidden content 
load_dotenv()

# Facilitates access to mongodb data
cluster = os.environ.get("DB_CLUSTER")
client = MongoClient(cluster)
db = client.sam

def display_homepage():
    """
    This function displays the homepage of the application
    """
    fig_font = Figlet(font='block', width= 100)
    print(Fore.CYAN + (fig_font.renderText('Buy / Sell Estate\n')))
    print('------------------------ Ⓒ 2023 --------------------------\n' + Style.RESET_ALL)

def display_main_menu():
    """
    This function displays the terminal's main menu of options
    """
    os.system('clear')
    print("MAIN MENU")
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("1. Properties")
    print("2. Clients")
    print("-=-=-=-=-=-=-=-=-=-=-")
    while True:
        try:
            option = int(input("Please enter an Option: \n"))
        except ValueError:
            print("Please enter a numeric value and try again")
            continue

def properties_menu():
    """
    This function displays the properties menu options. 
    It takes the user input and calls subsequent functions. 
    If an input is invalid, it shows error and ask for input again.
    """
    os.system('clear')
    print("Properties Menu")
    print("---------------")
    print("1. List All")
    print("2. Update")
    print("3. Add New")
    print("4. Delete")
    print("0. Main Menu")
    print("---------------")

    while True:
        option = input("Enter an option: \n")
        if option == "1":
            list_all_properties()
            break
        elif option == "0":
            display_main_menu()
            break
        else:
            print(" You chose an invalid option")

    # returns back to the properties menu after exploration of other functions
    properties_menu()

def list_all_properties():
    """
    This function fetchs the list of all the
    available property details from mongodb's collection
    """
    try:
        result = db.properties.find({})
    except OperationFailure:
        print("sorry, an error occured")
    results_list = list(result)
    if len(results_list) == 0:
        print("No result found")
    else:
        for result in results_list:
            display_properties(result)
    input("\nPress a key to continue\n")

def display_properties(properties):
    """
    This function displays details of the properties'
    collection dictionary from mongodb in a refined format.
    """
    property = properties["property"]
    property_type = properties["property_type"]
    house_number = properties["house_number"]
    location = properties["location"]
    price_bought = properties["price_bought"]
    repair_cost = properties["repair_cost"]
    tax_paid = properties["tax_paid"]
    status = properties["status"]
        
    print()
    print(f"property: {property}")
    print(f"property_type: {property_type}")
    print(f"house_number: {house_number} - location: {location}")
    print(f"price_bought: {price_bought} - status: {status}")
    print(f"repair_cost: {repair_cost} & tax_paid: {tax_paid}")
    
def main():
    """
    This runs the entire program functions
    """
    display_homepage()
    display_main_menu()

main()






