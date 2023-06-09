# Sell Estate

![Application's GIF](docs/sellestate.gif)

## Table Of Content

- [Introduction](#Introduction)
    - [Application link](#Application-link)
    - [Site Goals](#Site-Goals)
    - [Target Audience](#Target-Audience)
    - [User stories](#User-Stories)
    - [Features Planned](#Features-Planned)
- [Structure](#Structure)
    - [Features](#Features)
    - [Features left to Implement](#Features-Left-to-Implement)
- [Logical Flow](#Logical-Flow)
- [Database Design](#Database-Design)
- [Technologies](#Technologies)
- [Testing](#Testing)
    - [Functional Testing](#Functional-Testing)
    - [Pep8 Validation](#Pep8-Validation)
    - [Bugs and Fixes](#Bugs-and-Fixes)
- [Deployment](#Deployment)
    - [Version Control](#Version-Control)
    - [MongoDB Setup](#MongoDB-Setup)
    - [Heroku Deployment](#Heroku-Deployment)
- [Credits](#Credits)
  - [Content](#Content)

## Introduction

As a prospective real estate business person, I am inspired to create this pilot project to help beginner and small estate business persons keep track of their records. This project will help in adding new properties and clients acquired. It will also allow for updating the status and profit they make on property sales. There is also room for updating client's associated property with the help of setting a property reference.                                      

### View the deployed application [here](https://sell-estate.herokuapp.com/)

### Site Goals

* To provide a simple application for the site owner to keep track of their properties and clients.

### Target Audience

* Small estate businesses that want to keep track of their properties and clients.

### User Stories

* As a User, I would like to be able to easily find the various menus. In order for me to be able to view properties and clients details. I would also love to update, add, edit and or remove details.
* As a User, I would like to be able to manage my properties so that I can easily keep track of property details and be able to udpate, edit, add and or delete when neccessary. I would also love to easily find my property by their house number.
* As a User, I would like to be able to manage my clients' details so that I can add, delete, update and find clients easily by thier name when necessary.
* As a User, I would like to be able to return to the main menu without having to restart the application and also exit just by a tap.

### Features Planned

* Simple and easy to use application with clear navigation.
* Simple database storage for:
    * Add, list, update and delete functionality for properties.
    * Add, list, update and delete functionality for clients.
* Return to main menu option through sub menus.
* Exit easily by pressing 0 and enter.

## Structure

### Features

USER STORY

`
As a User, I would love to be able to easily find and understand the main menu so that I can at first know where exactly to get clients or properties information. In order for me to subsequently update, add or remove its details.
`

IMPLEMENTATION
* Main Menu
    * When the application starts, the sell estate logo witha copyright line underneath is displayed on the top of the main menu to introduce the user aesthetically to sell estate.
    * The main menu beneath the logo displays with the following options:
        * 1 - Properties
        * 2 - Clients
    * The user must input the correct corresponding number displayed on the menu. Else, they will be prompted to enter a numeric value while they are given another chance to re-enter a digit.
    * This feature will allow the user to easily access the sub menus to each category in order to perform the needed operations.

![Main Menu](docs/sellestate_main_menu.jpg)

USER STORY

`
As a User, I would like to be able to manage my properties so that I can easily keep track of the properties I have available and view, update, add  and delete when neccessary.
`

IMPLEMENTATION
* Properties Menu
    * When the user selects properties from the main menu, the following menu options are displayed:
        * 1 - List All - This option displays all properties currently stored in mongoDB.
        * 2 - Update - This option will open the properties Update Menu, implementation described below.
        * 3 - Add new - This option will first ask the user to verify the prospective property by the house number. If the house number is not already recorded, User is allowed to enter the details of the new property and save it to the mongo database once all details are correctly input. Conversely, if the house number already exists, user is notified that he or she already has that property saved.
        * 4 - Delete - This option will allow the user to delete a property from MongoDB after verifying and confirming deletion.
        * 5 - Main Menu - This option will return the user to the main menu.
        * 0 - Exit - This option ends the program with a closing confirmation message.
    * The user must input a correct number corresponding to each menu or they will be alerted on an incorrect choice and the menu will be presented again.
    * This feature will allow the user to easily view, add, update and delete properties to and from mongoDB efficiently.

Properties Menu

![Properties Menu](docs/properties_menu.jpg)

List All
![List all](docs/list_all.jpg)                                                                                                           

* Property Update Menu
    * When the property update menu is selected, the following menu options display:
        * 1 - Update status - This will allow user to find a particular property by house number in order to update its status whether sold or still available. 
        * 2 - Update profit - This will allow user to find a particular property by house number in order to update its profit. 
        * 3 - Back to properties menu - This will allow the user to go back to the properties menu.
        * 4 - Main Menu - This option will return the user to the main menu.
        * 0 - Exit - This option ends the application with a closing confirmation message.

Property Update Menu
![Property Update Menu](docs/update_property.jpg)

Update status
![Update status](docs/update_status.jpg)

Update profit
![Update profit](docs/update_profit.jpg)                                                                                                 

Add new                                                                                                                                   
![Add new](docs/add_new.jpg)
                                                                                                                                          
Delete                                                                                                                                   
![Delete](docs/delete.jpg)

USER STORY

`
As a User, I would love to have an intact list of all my clients and the properties they are attached to. In order for me to view their details, update the properties linked to them and also add to the list and or delete when neccessary.

IMPLEMENTATION
* Clients Menu
    * When the user selects clients from the main menu, the following menu options are displayed:
        * 1 - List All - This option displays all clients currently stored in mongoDB.
        * 2 - Update - This option will open the clients Update Menu, implementation described below.
        * 3 - Add new - This option will first ask the user to verify the client by name. If the name is not already recorded, User is allowed to enter the details of the new client and save it to the mongo database once all details are correctly input. In contrast, if the name already exists, user is notified that he or she already has that particular client saved.
        * 4 - Delete - This option will allow the user to delete a client from MongoDB after verifying and confirming deletion.
        * 5 - Main Menu - This option will return the user to the main menu.
        * 0 - Exit - This option ends the program with a closing confirmation message.
    * The user must input a correct number corresponding to each menu or they will be alerted on an incorrect choice and the menu will be presented again.
    * This feature will allow the user to easily view, add, update and delete clients to and from mongoDB efficiently.

Clients Menu
![Clients Menu](docs/clients_menu.jpg)

List All
![List all](docs/clients_list_all.jpg)

* Clients Update Menu
    * When the client update menu is selected, the following menu options display:
        * 1 - Update Property ref - This will allow user to find a particular client by name in order to update his or her associated property reference. 
        * 2 - Back to Clients Menu - This will allow the user to go back to the clients menu.
        * 3 - Main Menu - This option will return the user to the main menu.
        * 0 - Exit - This option ends the application with a closing confirmation message.

Clients Update Menu
![Clients Update Menu](docs/clients_update_menu.jpg)
                                                                                                                                          
Update property ref
![Update property ref](docs/property_ref.jpg)

Add new                                                                                                                                   
![Add new](docs/clients_add_new.jpg)
                                                                                                                                          
Delete                                                                                    
![Delete](docs/clients_delete.jpg)

USER STORY

`
As a User, I would like to be able to return to the main menu and exit the application without having to restart the application.
`

IMPLEMENTATION
* All sub menus have an option to return to the main menu and even other umbrella submenus as well. These are typically right above the exit option.
* This will allow the user to return to the main menu if they selected the wrong option or are done with the current menu.
* An exit option to end the application is also on all the sub menus for easy closing of the application.

This is evident on all the menu screenshots above.

**Error Handling**

Error handling was implemented throughout the application with the use of try/except statements to handle exceptions raised for things like None type values, Database connection errors Key and Value errors.

### Features Left to Implement

As a future enhancement, I would like to add some basic functionality to automatically calculate sales and profit instead of the manual input. I would also like to implement updates in accordance with the input date so that users will easily tell when exactly they made a particular input.
__
## Logical Flow

### Flowchart

To aid the development process of building the application, I used [Lucid Chart](https://www.lucidchart.com/) to 
visualise the organisational flow and functionality. This also helped me organise and demonstrate input validation to 
ensure that key data being sent to the mongo database is completely valid.

![Sellestate Flowchart](docs/sellesate_flowchart.jpg)

**Main Menu**

![Main Menu](docs/lucid_main_menu.jpg)

**Properties Menu**

![Properties Menu](docs/lucid_properties_menu.jpg)

**Clients Menu**

![Clients Menu](docs/lucid_clients.jpg)

**Property Update Menu**

![Property Update Menu](docs/lucid_property_update.jpg)

**Client Update Menu**

![Client Update Menu](docs/lucid_clients_update.jpg)


## Database Design

MongoDB is used to store the properties and clients with two collections namely; properties and clients.

**Collection 1 - properties**

This collection is used to store property details. As seen below, inserted objects to the properties collection has these fields:

![Properties Collection](docs/mongo_properties.jpg)

**Collection 2 - clients**

This collection is used to store client details.  Objects inserted to this collection has the following fields:

![Clients Collection](docs/mongo_clients.jpg)

## Technologies

* Python - Python was the main language used to build the application.
    * Python packages used:
        * pymongo - Used to connect to the MongoDB atlas to the application.
        * pyfiglet - Used to access the mini font for the application's homepage title. 
        * colorama - Used for the aesthetic design of the application's homepage title and its copyright line.
        * dotenv - Used to store and hide the mongo database cluster.
        * os - Used in line with a cls/clear command to clear the command line interface.
        * sys - Used to access the exit function at the bottom of all submenus. 
* MongoDB - This was used as data storage in order to store the properties and clients information.
* ScreenPal - This was used to screen record the Gif right at the top of the readme.

## Testing

### Functional Testing

Below are the  execution of positive functional tests:

![Main Menu Test](docs/test_main_menu.JPG)

![Properties Menu Test](docs/test_properties_menu.JPG)

![Clients Menu Test](docs/test_clients_menu.JPG)

![Properties Update Menu Test](docs/test_properties_update.JPG)

![Clients Update Menu Test](docs/test_clients_update.JPG)

Negative input validation testing was also conducted on all menu options to ensure correct input. All options behaved as expected, alerting the user of invalid input and then asking for input again.

### Pep8 Validation

The entire python code was passed through https://pep8ci.herokuapp.com/ validator and all warnings or errors were fixed. Code then validated successfully.

![Pep8](docs/pylinter_validation.jpg)

### Bugs and Fixes

At the start of the project, google spreadsheet was used to store data. Data input was not flexible enough. A switch to mongoDB provided the room for all types of data fields and types to be stored flexibly.
Initially, data could not be fed to the mongo database but the cluster connection was established and that was fixed. 
Hiding the cluster in an env.py file also did not work so an alternative of dotenv was imported and used.

Along the line, properties with the same house number were able to be added. A fix was implemented to ensure that duplicate properties with the same house number could not be added.

Also, empty data could be submitted to the database while adding new property and client. It was also the case in all data updates. A function; validate_data was created and implemented to fix this bug. Thus after the fix, whenever an empty field is entered, user is prompted with the validation text "This field is required" and asked to make the input again.

Making a query to the database was problematic with regards to case sensitivity. This was fixed by making the query's case correspond to the input case. Hence, queries of all sorts of cases are successful now.

 ## Deployment

 ### Version Control
The site was created using the Gitpod workspace and pushed to github to the remote repository ‘sell_estate’.

The following git commands were used throughout the development to push code to the remote repository:

```git add .``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

```git commit --amend -m "Amended git commit message"``` - This command was used to correct mistakenly/misspelt pushed commit messages.

```git push -f"``` - This command was used to force push an amended commit message.

### Heroku Deployment

* Install the requirements listed in requirements.txt using the terminal command "pip3 freeze --local > requirements.txt".

* Log-in to [Heroku](https://www.heroku.com) or create an account.

* Choose an app name and region, then click "Create app".

* Go to "Settings" and navigate to Config Vars. 
   
* Click the button labelled "Reveal Config Vars" and enter the "key" as port, the "value" as 8000 and click the "add" button.

* In order for the deployed application to have  permissions to access the mongo database, add your cluster variable from the .env file as the "key" and the URI connection string as the "value".

* Scroll down to the buildpacks section of the settings page and click the button labeled "Add Buildpack", choose "Python," and click "Save Changes".

* Repeat the step above to add "Node.js". It must be in this order with Python visibly above Node.js for the application to work.

* Navigate back to the "Deploy" page and select "Github" as the deployment method.

* Connect to your Github account and find your project's repository.

* Scroll down to Manual Deploy on Heroku, select "main" branch and click "Deploy Branch".

* Choose between enable automatic deploys or manual deploys. 

* The app will now be deployed to heroku.

### MongoDB Setup

* Navigate to [MongoDB](https://www.mongodb.com/) and create an account.
* Verify account by clicking the verification link emailed to you on the email you signed up with.
* Log in with newly created account.
* On the top right under projects, click the drop down and select new project.
* Name the project and click next, filling in subsequent inputs as desired.
* If prompted, whitelist IP by inputting (0.0.0.0/0) to allow access from anywhere.
* Once the project is created, from the left menu, select Database Access and create a new user with Read and Write access. It's best practice not to use special characters in the password as these will need to be escaped.
* Once a user has been created, you can click the 'Databases' under deployment and then click connect.
* Select the Connect your application option and this will provide you with a Mongo URI connection string that can be used in Heroku or an env file locally.

## Credits 

* [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template)
  * I appreciate Code institute's support and their gitpod template.

* [W3C](https://www.w3schools.com/python/)
  * I frequently referred to W3school tutorials throughout this project.  

* [Youtube Credentials storage Tutorial](https://www.youtube.com/watch?v=DVVYHlGYIHY)
    * I learnt how to use the dotenv to keep my mongoDB credentials from the youtube video above.

* [Youtube MongoDB Tutorial](https://www.youtube.com/watch?v=qWYx5neOh2s)
    * This youtube tutorial was used as a crash course on mongodb for all database functionality used within the project.
<br><br>

* Persons
    * A big appreciation to my mentor Gareth Mcgirr who guided and pushed me to use mongoDB.
    
    * I thank Olena Olkhovyk for inspiring and encouraging me on throughout the project.

### Content 

All the content with the exception of those listed in the Media and credits sections of this document were originaly made by Samuel Anderson.

### Media
  
* The ScreenPal desktop application was used to snap the GIF at the top of the readme.
* Pixlr X was used was used to edit most of the images in the readme section for clarity, aesthetics and readability.