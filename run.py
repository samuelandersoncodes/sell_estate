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