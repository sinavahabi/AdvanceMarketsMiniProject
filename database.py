import re
from local import Local
from crypto import Crypto
from bourse import Bourse
import mysql.connector
import jdatetime
from ColorsClass.colors import bcolors


class LocalDB(Local):

    def data_database(self):
        valid, condition, symbols, prices, dates = True, True, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE local")

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

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE data (name VARCHAR(50), price VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        try:
            selected_opt = [int(idx.strip()) - 1 for idx in user_input.split(',')]
        except ValueError as invalidInput:
            valid = False

        if valid:
            for index in selected_opt:
                try:
                    symbols = self.symbol_list[index]
                    prices = self.price_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

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
        valid, condition, symbols, prices, dates = True, True, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE mytest")

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

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE currency (name VARCHAR(50), price VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.currency_symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        try:
            selected_opt = [int(idx.strip()) - 1 for idx in user_input.split(',')]
        except ValueError as invalidInput:
            valid = False

        if valid:
            for index in selected_opt:
                try:
                    symbols = self.currency_symbol_list[index]
                    prices = self.currency_price_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

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


class CryptoDB(Crypto):
    def database(self):
        valid, condition, symbols, dollar_prices, rial_prices, marketcaps, volumes, dates = True, True, 0, 0, 0, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE crypto")
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

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE crypto_currency (name VARCHAR(30), dollar_price VARCHAR(20), rial_price VARCHAR(30), marketcap VARCHAR(30), volume VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        try:
            selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]
        except ValueError as invalidInput:
            valid = False

        if valid:
            for index in selected_opt:
                try:
                    symbols = self.symbol_list[index]
                    dollar_prices = self.dollar_price_list[index]
                    rial_prices = self.rial_price_list[index]
                    marketcaps = self.marketcap_list[index]
                    volumes = self.trade_volume_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

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


class BourseDB(Bourse):
    def database_bourse(self):
        valid, condition, symbols, final_prices, trade_prices, trade_values, volumes, marketcaps, dates = True, True, 0, 0, 0, 0, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE stock_exchange")
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

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE bourse_farabourse (symbol VARCHAR(30), final_price VARCHAR(20), trade_price VARCHAR(20), trade_value VARCHAR(30), volume VARCHAR(30),  marketcap VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        try:
            selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]
        except ValueError as invalidInput:
            valid = False

        if valid:
            for index in selected_opt:
                try:
                    symbols = self.symbol_list[index]
                    final_prices = self.final_price_list[index]
                    trade_prices = self.trade_price_list[index]
                    trade_values = self.trade_value_list[index]
                    volumes = self.trade_volume_list[index]
                    marketcaps = self.marketcap_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

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
        valid, condition, symbols, amounts, dates = True, True, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE stock_exchange")
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

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE indicator (symbol VARCHAR(40), amount VARCHAR(20), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.index_symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input(
            "You can choose index numbers from above outputs which you desire to save into database.\n" +
            bcolors.OKGREEN + bcolors.BOLD + "A valid example would be something like this: \"1,2,13,7,97,8\"" +
            bcolors.ENDC + "\nEnter your choices here: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        try:
            selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]
        except ValueError as invalidInput:
            valid = False

        if valid:
            for index in selected_opt:
                try:
                    symbols = self.index_symbol_list[index]
                    amounts = self.index_amount_list[index]
                    dates = date_list[index]
                except IndexError as Error:
                    print(bcolors.FAIL + "This index number is not available between given outputs." + bcolors.ENDC)

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
