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

clients = { 
"client_one" : {"Name" : "Donald Biden", "Tel" : "1578989034", "Associated property / id" : "FH 34_Hanover", 
"Status" : "Fully-paid"},
"client_two" : {"Name" : "Hilary Macron", "Tel" : "1751212348", "Associated property / id" : "R24 /c_Munich", 
"Status" : "Half-payment"},
"client_three" : {"Name" : "Micheal Jackson", "Tel" : "09175163487", "Associated property / id" : "A13_Cologne", 
"Status" : "Viewing appointment@ 29/05/23"}
}

properties = db.properties

result = properties.insert_one(clients)

print(client.list_database_names())

print(db.list_collection_names())

def display_homepage():
    """
    This function displays the homepage of the application
    """
    fig_font = Figlet(font='block', width= 100)
    print(Fore.CYAN + (fig_font.renderText('Buy / Sell Estate\n')))
    print('------------------------ Ⓒ 2023 --------------------------\n' + Style.RESET_ALL)

display_homepage()

