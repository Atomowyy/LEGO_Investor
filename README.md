# LEGO_Investor
## _Easy to use application, which help you to inspect your LEGO sets prices_


##  IMPORTANT!
This code require some specified additions to work fine. 
Make sure to follow every step from _CONFIGURATION_ section!

## Features
I'll add this someday


##  CONFIGURATION
#### 1. Web Browser
Script require Chrome web browser, make sure to install it 
#### 2. .env file
Script reads DB informations from .env file, you have to create text file named .env in main.py directory
There is a example file included to repository. 
```
# .env
host={database server IP, localhost for xampp}
database={database name}
port={port that MYSQL is running on. Ignore this for DB hosted on your machine}
user={priviliged user}
password={priviliged user password}
```
#### 3. MYSQL Database
There will be sql file in this repository within few days.
#### 4. Python libraries
Install folowing libraries in terminal:
* tabulate
* selenium
* mysql-connector-python
* python-dotenv

If this wont work, right click on underscored lanes at first lanes of code, and select "install" or "import"
