import re
from local import Local
from crypto import Crypto
from bourse import Bourse
import mysql.connector
import jdatetime
from ColorsClass.colors import bcolors


class LocalDB(Local):

    def data_database(self):
        condition, symbols, prices, dates = True, 0, 0, 0
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
                database="mytest"
            )

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE testTable (name VARCHAR(50), price VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input("Enter index numbers from above outputs which you desire to save into database: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]

        for index in selected_opt:
            try:
                symbols = self.symbol_list[index]
                prices = self.price_list[index]
                dates = date_list[index]
            except IndexError as Error:
                print(bcolors.FAIL + "This index number is not in available between given outputs." + bcolors.ENDC)

            if symbols or prices or dates:
                query = "INSERT INTO testTable(name, price, date) VALUES (%s, %s, %s)"
                new_cursor.execute(query, (symbols, prices, dates))
            else:
                condition = False

        if condition:
            new_connection.commit()
            new_cursor.close()
            new_connection.close()
            print(bcolors.HEADER + bcolors.BOLD + "Your selected data has been inserted to database successfully" + bcolors.ENDC)
        else:
            print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)

    def currencies_database(self):
        condition, symbols, prices, dates = True, 0, 0, 0
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
                database="mytest"
            )

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE testTable2 (name VARCHAR(50), price VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.currency_symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input("Enter index numbers from above outputs which you desire to save into database: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]

        for index in selected_opt:
            try:
                symbols = self.symbol_list[index]
                prices = self.price_list[index]
                dates = date_list[index]
            except IndexError as Error:
                print(bcolors.FAIL + "This index number is not in available between given outputs." + bcolors.ENDC)

            if symbols or prices or dates:
                query = "INSERT INTO testTable2(name, price, date) VALUES (%s, %s, %s)"
                new_cursor.execute(query, (symbols, prices, dates))
            else:
                condition = False

        if condition:
            new_connection.commit()
            new_cursor.close()
            new_connection.close()
            print(
                bcolors.HEADER + bcolors.BOLD + "Your selected data has been inserted to database successfully" + bcolors.ENDC)
        else:
            print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)


class CryptoDB(Crypto):
    def database(self):
        condition, symbols, dollar_prices, rial_prices, marketcaps, volumes, dates = True, 0, 0, 0, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE mytest2")
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="mytest2"
            )

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE testTable (name VARCHAR(30), dollar_price VARCHAR(20), rial_price VARCHAR(30), marketcap VARCHAR(30), volume VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input("Enter index numbers from above outputs which you desire to save into database: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        selected_opt = [int(idx.strip()) -1 for idx in user_input.split(',')]

        for index in selected_opt:
            try:
                symbols = self.symbol_list[index]
                dollar_prices = self.dollar_price_list[index]
                rial_prices = self.rial_price_list[index]
                marketcaps = self.marketcap_list[index]
                volumes = self.trade_volume_list[index]
                dates = date_list[index]
            except IndexError as Error:
                print(bcolors.FAIL + "This index number is not in available between given outputs." + bcolors.ENDC)

            if symbols or dollar_prices or rial_prices or marketcaps or volumes or dates:
                query = "INSERT INTO testTable(name, dollar_price, rial_price, marketcap, volume, date) VALUES (%s, %s, %s, %s, %s, %s)"
                new_cursor.execute(query, (symbols, dollar_prices, rial_prices, marketcaps, volumes, dates))
            else:
                condition = False

        if condition:
            new_connection.commit()
            new_cursor.close()
            new_connection.close()
            print(
                bcolors.HEADER + bcolors.BOLD + "Your selected data has been inserted to database successfully" + bcolors.ENDC)
        else:
            print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)


class BourseDB(Bourse):
    def database_bourse(self):
        condition, symbols, final_prices, trade_prices, trade_values, volumes, marketcaps, dates = True, 0, 0, 0, 0, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE mytest3")
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="mytest3"
            )

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE testTable (symbol VARCHAR(30), final_price VARCHAR(20), trade_price VARCHAR(20), trade_value VARCHAR(30), volume VARCHAR(30),  marketcap VARCHAR(30), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input("Enter index numbers from above outputs which you desire to save into database: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        selected_opt = [int(idx.strip()) - 1 for idx in user_input.split(',')]

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
                print(bcolors.FAIL + "This index number is not in available between given outputs." + bcolors.ENDC)

            if symbols or final_prices or trade_prices or trade_values or volumes or marketcaps or dates:
                query = "INSERT INTO testTable(symbol, final_price, trade_price, trade_value, volume, marketcap, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                new_cursor.execute(query, (symbols, final_prices, trade_prices, trade_values, volumes, marketcaps, dates))
            else:
                condition = False

        if condition:
            new_connection.commit()
            new_cursor.close()
            new_connection.close()
            print(
                bcolors.HEADER + bcolors.BOLD + "Your selected data has been inserted to database successfully" + bcolors.ENDC)
        else:
            print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)

    def database_index(self):
        condition, symbols, amounts, dates = True, 0, 0, 0
        try:
            # Connecting to DB and creating database.
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
            )

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE mytest3")
        except mysql.connector.errors.DatabaseError as dbError:
            pass

        try:
            # Connecting to DB and creating table.
            new_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="maria1402",
                database="mytest3"
            )

            new_cursor = new_connection.cursor()
            new_cursor.execute("CREATE TABLE testTable2 (symbol VARCHAR(40), amount VARCHAR(20), date VARCHAR(20))")

        except mysql.connector.errors.ProgrammingError as tbError:
            pass

        date = jdatetime.datetime.now()
        current_date = str(date)
        date_list = []
        for i in range(0, len(self.index_symbol_list)):
            date_list.append(current_date[:16])

        user_selection = input("Enter index numbers from above outputs which you desire to save into database: ")
        user_input = re.sub(r'[^,\d]', "", user_selection)
        selected_opt = [int(idx.strip()) - 1 for idx in user_input.split(',')]

        for index in selected_opt:
            try:
                symbols = self.index_symbol_list[index]
                amounts = self.index_amount_list[index]
                dates = date_list[index]
            except IndexError as Error:
                print(bcolors.FAIL + "This index number is not in available between given outputs." + bcolors.ENDC)

            if symbols or amounts or dates:
                query = "INSERT INTO testTable2(symbol, amount, date) VALUES (%s, %s, %s)"
                new_cursor.execute(query, (symbols, amounts, dates))
            else:
                condition = False

        if condition:
            new_connection.commit()
            new_cursor.close()
            new_connection.close()
            print(
                bcolors.HEADER + bcolors.BOLD + "Your selected data has been inserted to database successfully" + bcolors.ENDC)
        else:
            print(bcolors.WARNING + "Nothing has been inserted!!" + bcolors.ENDC)
