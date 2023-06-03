# imported libraries
import os
import sys
from pyfiglet import Figlet
from colorama import Style, Fore
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from dotenv import load_dotenv

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
    fig_font = Figlet(font='mini', width=200)
    print(Fore.CYAN + (fig_font.renderText('Sell Estate\n')))
    print('-=-=-= Ⓒ 2023 -=-=-=-\n' + Style.RESET_ALL)


def display_main_menu():
    """
    This function displays the terminal's main menu of options
    """
    os.system('clear')
    display_homepage()
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

        if option == 1:
            properties_menu()
            break
        elif option == 2:
            clients_menu()
            break
        else:
            print("You chose an invalid option")


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
    print("5. Main Menu")
    print("0. Exit")
    print("---------------")

    while True:
        option = input("Enter an option: \n")
        if option == "1":
            list_all_properties()
            break
        elif option == "2":
            properties_edit_menu()
            break
        elif option == "3":
            new_estate = add_new_property()
            if new_estate is not None:
                save_property_details(new_estate)
            break
        elif option == "4":
            remove_property()
            break
        elif option == "5":
            display_main_menu()
            break
        elif option == "0":
            sys.exit("Your program ended successfully!")
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
    property_number = properties["property_number"]
    property_type = properties["property_type"]
    house_number = properties["house_number"]
    location = properties["location"]
    price_bought = properties["price_bought"]
    repair_cost = properties["repair_cost"]
    tax_paid = properties["tax_paid"]
    status = properties["status"]
    profit = properties["profit"]
    print()
    print(f"property_number: {property_number}")
    print(f"property_type: {property_type}")
    print(f"house_number: {house_number} - location: {location}")
    print(f"repair_cost: {repair_cost} & tax_paid: {tax_paid}")
    print(f"price_bought: {price_bought}")
    print(f"status: {status} - profit: {profit}")


def properties_edit_menu():
    """
    This function provides property update menu
    and calls other functions to edit it.
    If an input is invalid, it shows error
    and makes another input request.
    """
    os.system('clear')
    print("Update Property")
    print("---------------")
    print("1. Update status")
    print("2. Update profit")
    print("3. Back to Properties Menu")
    print("4. Main Menu")
    print("0. Exit")
    print("---------------")

    option = input("Enter an option: \n")
    if option == "1":
        properties_update_status()
        properties_edit_menu()
    elif option == "2":
        update_properties_profit()
        properties_edit_menu()
    elif option == "3":
        properties_menu()
    elif option == "4":
        display_main_menu()
    elif option == "0":
        sys.exit("Your program ended successfully!")
    else:
        print("You entered an invalid option, please try again")
        input("\nPress a key to continue\n")
        properties_edit_menu()


def properties_update_status(housenumber=None):
    """
    This function updates the selling status of the property
    with a default of None if the house_number is not passed
    as an arguement.
    User searches by house number for the update.
    """
    if housenumber is None:
        housenumber = (input("Enter house_no: \n")).upper()
    result = find_property_by_house_number(housenumber)
    if result is not None:
        display_properties(result)

        try:
            new_status = validate_data(input("\nPlease enter the new status\n"))
            db.properties.update_one(
                {"house_number": housenumber}, {"$set": {
                    "status": new_status,
                    }}
                )
            print(f"your new status is {new_status}")
            print("successfully updated!")
        except OperationFailure:
            print("Sorry! status could not update, please try again later")
        input("\nPress a key to continue...\n")
    else:
        print("\nProperty not found")
        input("\nPress a key to continue...\n")


def update_properties_profit(housenumber=None):
    """
    This function updates the profit of the property
    with a default of None if the house_number is not passed
    as an arguement.
    User searches by house number for the profit update.
    """
    if housenumber is None:
        housenumber = (input("Enter house_no: \n")).upper()
    result = find_property_by_house_number(housenumber)
    if result is not None:
        display_properties(result)

        try:
            updated_profit = validate_data(input("\nPlease enter the current profit\n"))
            db.properties.update_one(
                {"house_number": housenumber}, {"$set": {
                    "profit": updated_profit,
                    }}
                )
            print(f"your updated profit is: {updated_profit}")
            print("successfully updated!")
        except OperationFailure:
            print("Sorry! profit could not update, please try again later")
        input("\nPress a key to continue...\n")
    else:
        print("\nProperty not found")
        input("\nPress a key to continue...\n")


def find_property_by_house_number(house_number):
    """
    This function finds a property in mongodb by the
    corresponding house number.
    """
    try:
        result = db.properties.find_one({"house_number": house_number})
        return result
    except OperationFailure:
        print("Sorry, this house number does not match any property")
        return None


def validate_data(data):
    """
    This function validates submitted data.
    It makes sure empty data cannot be submitted.
    """
    if len(data) == 0:
        result = ''
        while len(result) == 0:
            print('This field is required')
            result = input(data)
        return result
    return data


def add_new_property():
    """
    This function prepares a new property in a dictionary form.
    which will be saved subsequently to mongodb by another function.
    User is first asked for house number, if house number already exists,
    user is obliged to enter a new one.
    """
    housenumber = (input(
        "To avoid duplication verify house_number:\n")).upper()
    result = find_property_by_house_number(housenumber)
    if result is not None:
        print("You have already recorded this property\n")
        display_properties(result)
        input("\nPress a key to continue\n")
        return None

    property_number = validate_data(
        input("Please enter property_no: \n").lower())
    housenumber = validate_data(
        input("Please enter house_no: \n").upper())
    property_type = validate_data(
        input("Please enter property_type: \n").lower())
    location = validate_data(
        input("Please enter property location: \n").capitalize())
    price_bought = validate_data(input("Please enter price_bought: \n"))
    repair_cost = validate_data(input("Please enter repair_cost: \n"))
    tax_paid = validate_data(input("Please enter tax_paid: \n"))
    status = validate_data(input("Please enter status: \n").lower())
    profit = validate_data(input("Please enter profit: \n").lower())

    property_details = {
        "property_number": property_number,
        "property_type": property_type,
        "house_number": housenumber,
        "location": location,
        "price_bought": price_bought,
        "repair_cost": repair_cost,
        "tax_paid": tax_paid,
        "status": status,
        "profit": profit,
        }
    return property_details


def save_property_details(properties):
    """
    This function saves the updates provided in the
    add_new_property function into mongodb.
    """
    try:
        db.properties.insert_one(properties)
        print("Update successful!")
        input("\nPress a key to continue\n")
        return True
    except OperationFailure:
        print("Sorry there was an error, update failed!")
        input("\nPress a key to continue\n")
        return False


def remove_property():
    """
    This function finds a property by house number,
    confirms if user is sure of removing the specific property.
    Then deletes it upon confirmation.
    """
    house_number = (input("Enter a house number\n")).upper()
    result = find_property_by_house_number(house_number)
    if result is not None:
        display_properties(result)
        confirm_removal = input("\n\nPlease confirm removal? (y/n) : \n")
        if confirm_removal == 'y':
            db.properties.delete_one({"house_number": house_number})
            print("\nProperty removed!")
        else:
            print("\nProperty removal failed")
    else:
        print(f"\nNo results found for {house_number}")
    input("\nPress a key to continue\n")


def clients_menu():
    """
    This function displays the clients menu options.
    It takes the user input and calls subsequent functions.
    If an input is invalid, it shows error and ask for the input again.
    """
    os.system('clear')
    print("Clients Menu")
    print("---------------")
    print("1. List All")
    print("2. Update")
    print("3. Add New")
    print("4. Delete")
    print("5. Main Menu")
    print("0. Exit")
    print("---------------")

    while True:
        option = input("Enter an option: \n")
        if option == "1":
            list_all_clients()
            break
        elif option == "2":
            clients_edit_menu()
            break
        elif option == "3":
            new_client = add_new_client()
            if new_client is not None:
                save_client_details(new_client)
            break
        elif option == "4":
            remove_client()
            break
        elif option == "5":
            display_main_menu()
            break
        elif option == "0":
            sys.exit("Your program ended successfully!")
        else:
            print(" You chose an invalid option")

    # returns back to the clients menu after exploring other functions
    clients_menu()


def list_all_clients():
    """
    This function fetchs the list of all the
    available client details from mongodb's clients collection
    """
    try:
        result = db.clients.find({})
    except OperationFailure:
        print("sorry, an error occured")
    results_list = list(result)
    if len(results_list) == 0:
        print("No result found")
    else:
        for result in results_list:
            display_clients(result)
    input("\nPress a key to continue\n")


def display_clients(clients):
    """
    This function displays details of the clients'
    collection dictionary from mongodb in a refined format.
    """
    name = clients["name"]
    email = clients["email"]
    tel = clients["tel"]
    associated_property_ref = clients["associated_property_ref"]
    print()
    print(f"name: {name}")
    print(f"email: {email}")
    print(f"tel: {tel}")
    print(f"associated_property_ref: {associated_property_ref}")


def clients_edit_menu():
    """
    This function provides clients update menu
    and calls other functions to edit it.
    If an input is invalid, it shows error and makes another input request.
    """
    os.system('clear')
    print("Update Client")
    print("---------------")
    print("1. Update property ref")
    print("2. Back to Clients Menu")
    print("3. Main Menu")
    print("0. Exit")
    print("---------------")

    option = input("Enter an option: \n")
    if option == "1":
        update_property_ref()
        clients_edit_menu()
    elif option == "2":
        clients_menu()
    elif option == "3":
        display_main_menu()
    elif option == "0":
        sys.exit("Your program ended successfully!")
    else:
        print("You entered an invalid option, please try again")
        input("\nPress a key to continue\n")
        clients_edit_menu()


def find_client_by_name(name):
    """
    This function finds client in mongodb by their name.
    """
    try:
        result = db.clients.find_one({"name": name})
        return result
    except OperationFailure:
        print("Sorry, you dont have this name in your list")
        return None


def update_property_ref(client_name=None):
    """
    This function updates the associated property ref of the client
    with a default of None if the name is not passed
    as an arguement.
    User searches for client by name for the update.
    """
    if client_name is None:
        client_name = input("Please enter clients' name: \n")
    result = find_client_by_name(client_name)
    if result is not None:
        display_clients(result)

        try:
            new_ref = validate_data(input("\nPlease enter the new property ref: \n"))
            db.clients.update_one(
                {"name": client_name}, {"$set": {
                    "associated_property_ref": new_ref,
                    }}
                )
            print(f"your new property ref is: {new_ref}")
            print("successfully updated!")
        except OperationFailure:
            print("Sorry! property ref could not update, please try again")
        input("\nPress a key to continue...\n")
    else:
        print("\nProperty not found")
        input("\nPress a key to continue...\n")


def add_new_client():
    """
    This function prepares the entry of a new client in a dictionary form.
    which will be saved subsequently to mongodb by another function.
    User is first asked for client's name, if the name already exists,
    user is obliged to enter a new one.
    """
    client_name = input("To avoid duplication verify name: \n")
    result = find_client_by_name(client_name)
    if result is not None:
        print("You have already recorded this client\n")
        display_clients(result)
        input("\nPress a key to continue\n")
        return None

    client_name = validate_data(
        input("Good to go! Please re-enter name: \n").capitalize())
    email_address = validate_data(input("Please enter an email: \n").lower())
    telephone_number = int(validate_data(
        input("Please enter telelephone number: \n")))
    associated_property_ref = validate_data(
        input("Enter the associated_property_ref: \n"))

    client_details = {
        "name": client_name,
        "email": email_address,
        "tel": telephone_number,
        "associated_property_ref": associated_property_ref,
    }
    return client_details


def save_client_details(clients):
    """
    This function saves the updates provided in the
    add_new_client function's inputs into mongodb.
    """
    try:
        db.clients.insert_one(clients)
        print("Update successful!")
        input("\nPress a key to continue\n")
        return True
    except OperationFailure:
        print("Sorry there was an error, update failed!")
        input("\nPress a key to continue\n")
        return False


def remove_client():
    """
    This function finds a client by name,
    confirms if user is sure of removing the specific client.
    Then deletes it upon confirmation.
    """
    name = input("Enter a name\n")
    result = find_client_by_name(name)
    if result is not None:
        display_clients(result)
        confirm_removal = input("\n\nPlease confirm removal? (y/n) : \n")
        if confirm_removal == 'y':
            db.clients.delete_one({"name": name})
            print("\nClient removed!")
        else:
            print("\nClient removal failed")
    else:
        print(f"\nNo results found for {name}")
    input("\nPress a key to continue\n")


def main():
    """
    This runs the entire program functions
    """

    display_main_menu()


main()
