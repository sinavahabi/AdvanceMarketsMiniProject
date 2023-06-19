"""
    Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
    Commands:
        pip install mysql-connector-python
"""

# Importing classes from other modules.
import re
from local import Local
from crypto import Crypto
from bourse import Bourse
import mysql.connector
import jdatetime
from ColorsClass.colors import bcolors
# After importing other essential packages that we need, our program is ready to begin.


# Using class inheritance to have access in necessary usable objects.
class LocalDB(Local):

    def data_database(self):
        # Defining some conditional and essential variables.
        valid, condition, symbols, prices, dates = True, True, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            # After creating cursor program is ready to execute queries with SQL syntax.
            cursor = connection.cursor()
            # Creating database called "local".
            cursor.execute("CREATE DATABASE local")
        # Using "try except" statement helps us here to avoid program crashes after first time program is ran and database is already created.
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="local"
            )

            # Creating table called "data" after we made new connection to an existing database called "local".
            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE data (name VARCHAR(50), price VARCHAR(30), date VARCHAR(20))")
        # Using "try except" statement helps us here to avoid program crashes after first time program is run and database is already created.
        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []

        # Make sure our "date_list" indexes count is equal to others.
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        # Asking for user choice between shown outputs and giving some guidelines.
        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        # Using Regex to make sure nothing is entered except "numbers" and "," by user.
        user_input = re.sub(r'[^,\d]', "", user_selection)

        try:
            # Assign user choices as a list of integer numbers separated by comma to a variable.
            selected_opt = [int(idx.strip()) - 1 for idx in user_input.split(',')]
            # Considering user pressing "Enter" button on keyboard and avoiding program crashes.
        except ValueError as invalidInput:
            valid = False

        # If user done mentioned condition "valid" variable will be set to False and data won't be inserted to database.
        if valid:
            for index in selected_opt:
                try:
                    # If user enters irrelevant numbers to outputs indexes (number or numbers bigger than last index number shown beside outputs), following variable values will remain as their default value assigned at top method level which is 0.
                    symbols = self.symbol_list[index]
                    prices = self.price_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

                # And if their value remained default (0), by following condition, if all the variable values below where equal to 0 (False); then condition value will set to False and nothing will be inserted to database as well.
                if symbols or prices or dates:
                    query = "INSERT INTO data(name, price, date) VALUES (%s, %s, %s)"
                    new_cursor.execute(query, (symbols, prices, dates))
                else:
                    condition = False

            if condition:
                new_connection.commit()
                new_cursor.close()
                new_connection.close()
                print(bcolors.HEADER + bcolors.BOLD + "Your valid selected data has been inserted to database successfully" + bcolors.ENDC)
            else:
                print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC + "\n" + bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)

    def currencies_database(self):
        # Defining some conditional and essential co-conditional variables.
        valid, condition, symbols, prices, dates = True, True, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            # After creating cursor program is ready to execute queries with SQL syntax.
            cursor = connection.cursor()
            # Creating database called "local".
            cursor.execute("CREATE DATABASE local")
        # Using "try except" statement helps us here to avoid program crashes after first time program is ran and database is already created.
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="local"
            )

            # Creating table called "currency" after we made new connection to an existing database called "local".
            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE currency (name VARCHAR(50), price VARCHAR(30), date VARCHAR(20))")
        # Using "try except" statement helps us here to avoid program crashes after first time program is run and table is already created.
        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []

        # Make sure our "data_list" indexes count is equal to others.
        for i in range(0, len(self.currency_symbol_list)):
            date_list.append(current_date[:16])

        # Asking for user choice between shown outputs and giving some guidelines.
        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        # Using Regex to make sure nothing is entered except "numbers" and "," by user.
        user_input = re.sub(r'[^,\d]', "", user_selection)

        try:
            # Assign user choices as a list of integer numbers separated by comma to a variable.
            selected_opt = [int(idx.strip()) - 1 for idx in user_input.split(',')]
            # Considering user pressing "Enter" button on keyboard and avoiding program crashes.
        except ValueError as invalidInput:
            valid = False

        # If user has done mentioned condition "valid" variable will be set to False and data won't be inserted to database.
        if valid:
            for index in selected_opt:
                try:
                    # If user enters irrelevant numbers to outputs indexes (number or numbers bigger than last index number shown beside outputs), following variable values will remain as their default value assigned at top method level which is 0.
                    symbols = self.currency_symbol_list[index]
                    prices = self.currency_price_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

                # And if their value remained default (0), by following condition, if all the variable values below where equal to 0 (False); then condition value will set to False and nothing will be inserted to database as well.
                if symbols or prices or dates:
                    query = "INSERT INTO currency(name, price, date) VALUES (%s, %s, %s)"
                    new_cursor.execute(query, (symbols, prices, dates))
                else:
                    condition = False

            if condition:
                new_connection.commit()
                new_cursor.close()
                new_connection.close()
                print(
                    bcolors.HEADER + bcolors.BOLD + "Your valid selected data has been inserted to database successfully" + bcolors.ENDC)
            else:
                print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC + "\n" + bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)


# Using class inheritance to have access in necessary usable objects.
class CryptoDB(Crypto):
    def database(self):
        # Defining some conditional and essential co-conditional variables.
        valid, condition, symbols, dollar_prices, rial_prices, marketcaps, volumes, dates = True, True, 0, 0, 0, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            # After creating cursor program is ready to execute queries with SQL syntax.
            cursor = connection.cursor()
            # Creating database called "crypto".
            cursor.execute("CREATE DATABASE crypto")
        # Using "try except" statement helps us here to avoid program crashes after first time program is ran and database is already created.
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="crypto"
            )

            # Creating table called "crypto_currency" after we made new connection to an existing database called "crypto".
            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE crypto_currency (name VARCHAR(30), dollar_price VARCHAR(20), rial_price VARCHAR(30), marketcap VARCHAR(30), volume VARCHAR(30), date VARCHAR(20))")
        # Using "try except" statement helps us here to avoid program crashes after first time program is run and table is already created.
        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []

        # Make sure our "date_list" indexes count is equal to others.
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        # Asking for user choice between shown outputs and giving some guidelines.
        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        # Using Regex to make sure nothing is entered except "numbers" and "," by user.
        user_input = re.sub(r'[^,\d]', "", user_selection)

        try:
            # Assign user choices as a list of integer numbers separated by comma to a variable.
            selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]
            # Considering user pressing "Enter" button on keyboard and avoiding program crashes.
        except ValueError as invalidInput:
            valid = False

        # If user has done mentioned condition "valid" variable will be set to False and data won't be inserted to database.
        if valid:
            for index in selected_opt:
                try:
                    # If user enters irrelevant numbers to outputs indexes (number or numbers bigger than last index number shown beside outputs), following variable values will remain as their default value assigned at top method level which is 0.
                    symbols = self.symbol_list[index]
                    dollar_prices = self.dollar_price_list[index]
                    rial_prices = self.rial_price_list[index]
                    marketcaps = self.marketcap_list[index]
                    volumes = self.trade_volume_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

                # And if their value remained default (0), by following condition, if all the variable values below where equal to 0 (False); then condition value will set to False and nothing will be inserted to database as well.
                if symbols or dollar_prices or rial_prices or marketcaps or volumes or dates:
                    query = "INSERT INTO crypto_currency(name, dollar_price, rial_price, marketcap, volume, date) VALUES (%s, %s, %s, %s, %s, %s)"
                    new_cursor.execute(query, (symbols, dollar_prices, rial_prices, marketcaps, volumes, dates))
                else:
                    condition = False

            if condition:
                new_connection.commit()
                new_cursor.close()
                new_connection.close()
                print(
                    bcolors.HEADER + bcolors.BOLD + "Your valid selected data has been inserted to database successfully" + bcolors.ENDC)
            else:
                print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC + "\n" + bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)


# Using class inheritance to have access in necessary usable objects.
class BourseDB(Bourse):
    def database_bourse(self):
        # Defining some conditional and essential co-conditional variables.
        valid, condition, symbols, final_prices, trade_prices, trade_values, volumes, marketcaps, dates = True, True, 0, 0, 0, 0, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            # After creating cursor program is ready to execute queries with SQL syntax.
            cursor = connection.cursor()
            # Creating database called "stock_exchange".
            cursor.execute("CREATE DATABASE stock_exchange")
        # Using "try except" statement helps us here to avoid program crashes after first time program is ran and database is already created.
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="stock_exchange"
            )

            # Creating table called "bourse_farabourse" after we made new connection to an existing database called "stock_exchange".
            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE bourse_farabourse (symbol VARCHAR(30), final_price VARCHAR(20), trade_price VARCHAR(20), trade_value VARCHAR(30), volume VARCHAR(30),  marketcap VARCHAR(30), date VARCHAR(20))")
        # Using "try except" statement helps us here to avoid program crashes after first time program is run and table is already created.
        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []

        # Make sure our "data_list" indexes count is equal to others.
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        # Asking for user choice between shown outputs and giving some guidelines.
        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        # Using Regex to make sure nothing is entered except "numbers" and "," by user.
        user_input = re.sub(r'[^,\d]', "", user_selection)

        try:
            # Assign user choices as a list of integer numbers separated by comma to a variable.
            selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]
            # Considering user pressing "Enter" button on keyboard and avoiding program crashes.
        except ValueError as invalidInput:
            valid = False

        # If user has done mentioned condition "valid" variable will be set to False and data won't be inserted to database.
        if valid:
            for index in selected_opt:
                try:
                    # If user enters irrelevant numbers to outputs indexes (number or numbers bigger than last index number shown beside outputs), following variable values will remain as their default value assigned at top method level which is 0.
                    symbols = self.symbol_list[index]
                    final_prices = self.final_price_list[index]
                    trade_prices = self.trade_price_list[index]
                    trade_values = self.trade_value_list[index]
                    volumes = self.trade_volume_list[index]
                    marketcaps = self.marketcap_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

                # And if their value remained default (0), by following condition, if all the variable values below where equal to 0 (False); then condition value will set to False and nothing will be inserted to database as well.
                if symbols or final_prices or trade_prices or trade_values or volumes or marketcaps or dates:
                    query = "INSERT INTO bourse_farabourse(symbol, final_price, trade_price, trade_value, volume, marketcap, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    new_cursor.execute(query, (symbols, final_prices, trade_prices, trade_values, volumes, marketcaps, dates))
                else:
                    condition = False

            if condition:
                new_connection.commit()
                new_cursor.close()
                new_connection.close()
                print(
                    bcolors.HEADER + bcolors.BOLD + "Your valid selected data has been inserted to database successfully" + bcolors.ENDC)
            else:
                print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC + "\n" + bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)

    def database_index(self):
        # Defining some conditional and essential co-conditional variables.
        valid, condition, symbols, amounts, dates = True, True, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            # After creating cursor program is ready to execute queries with SQL syntax.
            cursor = connection.cursor()
            # Creating database called "stock_exchange".
            cursor.execute("CREATE DATABASE stock_exchange")
        # Using "try except" statement helps us here to avoid program crashes after first time program is ran and database is already created.
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="stock_exchange"
            )

            # Creating table called "indicator" after we made new connection to an existing database called "stock_exchange".
            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE indicator (symbol VARCHAR(40), amount VARCHAR(20), date VARCHAR(20))")
        # Using "try except" statement helps us here to avoid program crashes after first time program is run and table is already created.
        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []

        # Make sure our "data_list" indexes count is equal to others.
        for i in range(0, len(self.index_symbol_list)):
            date_list.append(current_date[:16])

        # Asking for user choice between shown outputs and giving some guidelines.
        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        # Using Regex to make sure nothing is entered except "numbers" and "," by user.
        user_input = re.sub(r'[^,\d]', "", user_selection)

        try:
            # Assign user choices as a list of integer numbers separated by comma to a variable.
            selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]
            # Considering user pressing "Enter" button on keyboard and avoiding program crashes.
        except ValueError as invalidInput:
            valid = False

        # If user has done mentioned condition "valid" variable will be set to False and data won't be inserted to database.
        if valid:
            for index in selected_opt:
                try:
                    # If user enters irrelevant numbers to outputs indexes (number or numbers bigger than last index number shown beside outputs), following variable values will remain as their default value assigned at top method level which is 0.
                    symbols = self.index_symbol_list[index]
                    amounts = self.index_amount_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

                # And if their value remained default (0), by following condition, if all the variable values below where equal to 0 (False); then condition value will set to False and nothing will be inserted to database as well.
                if symbols or amounts or dates:
                    query = "INSERT INTO indicator(symbol, amount, date) VALUES (%s, %s, %s)"
                    new_cursor.execute(query, (symbols, amounts, dates))
                else:
                    condition = False

            if condition:
                new_connection.commit()
                new_cursor.close()
                new_connection.close()
                print(
                    bcolors.HEADER + bcolors.BOLD + "Your valid selected data has been inserted to database successfully" + bcolors.ENDC)
            else:
                print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC + "\n" + bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)
