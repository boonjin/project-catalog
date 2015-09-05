Tournament Results
==================

Author: Goh Boon Jin

Purpose: This application provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.


### Introduction
This project showcases a app catalog with predefined categories. Users logged in may add new apps within each category.
The application also has JSON endpoints.

The 3 main files are
* `database_setup.py` - contains the database schema for the project
* `project.py` - python module for the project server
* `presetApps.py` - initialize predefined categories and apps
    
### Requirements
* Vagrant and Virtual Box
* [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)

### Execution
* Run Vagrant VM, 
    * `vagrant up`
    * `vagrant ssh`
* Go to folder
    * `cd ../../catalog`
* Create preset Categories and Apps
    * `python presetApps.py`
* Run server
    * `python project.py`
* Access application by visiting 'http://127.0.0.1:5000` locally
