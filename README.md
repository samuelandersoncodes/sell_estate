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
