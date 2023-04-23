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
    
def main():
    """
    This runs the entire program functions
    """
    display_homepage()
    display_main_menu()

main()






