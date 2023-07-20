Advance Market Status

Languages: Python

Topics: OOP, Continuous program, Error handling, Interactive, MySQL, MariaDB, REST API, Optional, Regex, Python virtual environment 

Websites links: “https://www.tgju.org”, “https://www.shakhesban.com”, “https://arzdigital.com/coins”

In this program there’s two main purposes:
1-Web scraping and showing useful market data read from different websites around the world.
2-User choice capability to select which data output and how much of it, will be saved into the database.

This program includes 5 python modules.
3 following modules will do the main part which is receiving important relevant data from web and implementing it before they send it to database module.

“local.py”: will receive web data mainly from https://www.tgju.org website.
This website content concentrates mostly on Iran local market status, such as gold, silver, gold coins and etc.
Program divides mentioned data to 4 main parts:
"1: Gold and Silver price."
"2: International Ounces price."
"3: Gold Coins price."
"4: International Currencies price."

“bourse.py”: will receive web data mainly from https://www.shakhesban.com website.
This website content concentrates mostly on Tehran Stock Exchange market status, which has three main parts: Bourse, Fara-Bourse and Stock Exchange Indicators (indexes).
Bourse and Fara-Bourse are divided into smaller subsets to represent more valuable data from the extended and large stock exchange market.
These are common subsets for both Bourse and Fara-Bourse options:
"1.Without Ordering:"
"2.Ordering by Market Value:"
"3.Ordering by Final Price:"
"4.Ordering by Final Trade:"
"5.Ordering by Trade Volume:"
"6.Ordering by Trade Value:"

“crypto.py”: will receive web data mainly from https://arzdigital.com/coins website.
This website content concentrates mostly on Crypto Currency market status which is divided manually to 4 parts by program: 
"1: First 50 top crypto currencies."
"2: First 100 crypto currencies."
"3: First 500 crypto currencies."
"4: First 1000 crypto currencies."

“database.py” module will create a connection to a MySQL database (MariaDB) and insert selected data by user, to related databases and tables.
Classes methods in this module will receive all shown outputs to user, but only selected outputs data, will be saved to database by user choice.

“main.py” module is where user interacts with program by choosing desired options to receive important momentary related market data and decides which output should be send to database.
This module also includes quit option at any time or going back through menus. The Program should be ran from "main.py".

All modules and code structures in mentioned program contain error handling parts to avoid program crashes or stops as much as possible; but “main.py” and "database.py" contains the most parts of error management from codes beginning to end.
Finally, this mini project was written in virtual environment directory, so libraries or packages are only installed locally in mentioned environment and not globally. 

Note: Codes documentation and descriptions are more obvious in comments among the codes on each file.
Note: This mini project was fully handled by git from beginning to end.



