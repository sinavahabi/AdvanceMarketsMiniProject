# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install bs4
# pip install requests
# pip install jdatetime
import requests
from bs4 import BeautifulSoup
import jdatetime
from ColorsClass.colors import bcolors
# After importing all the essential packages that we need, our program is ready to begin.


class Local:
    def __init__(self):
        # For all data except currencies.
        self.symbol_list, self.price_list = [], []
        # For currencies data only.
        self.currency_symbol_list, self.currency_price_list = [], []

    def get_data(self):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        # Gold and Silver data.
        response = requests.get("https://www.tgju.org/gold-chart")
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', attrs={'data-tab-id': '1'})
        thead_tag = tables[0].find('thead')
        title = thead_tag.find('th')
        # Gold shekel.
        shekel_row = tables[1].find('tr', attrs={'data-market-row': 'mesghal'})
        shekel_symbol = shekel_row.find('th')
        shekel_price = shekel_row.find('td', {'class': 'nf'})
        print(bcolors.HEADER + bcolors.BOLD + "1." + title.nextSibling.nextSibling.text + " " + shekel_symbol.text[:-1]
              + ": " + bcolors.ENDC + bcolors.OKBLUE + shekel_price.text + " ریال" + bcolors.ENDC +
              " |" + ' تاریخ:' + date[:16])
        # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
        self.symbol_list.append(shekel_symbol.text[:-1])
        self.price_list.append(shekel_price.text  + " ریال")

        # Golds.
        gold_tbody_tag = tables[0].find('tbody')
        gold_rows = gold_tbody_tag.find_all('tr')
        counter = 1
        for gr in gold_rows:
            gold_prices = gr.find_all('td', attrs={'class': 'nf'})
            gold_symbols = gr.find_all('th')
            for gs in gold_symbols:
                counter += 1
                print(bcolors.HEADER + bcolors.BOLD + str(counter) + "." + title.nextSibling.nextSibling.text + " " + gs.text, end=": " +
                                                                                                              bcolors.ENDC)
            for gp in gold_prices[0]:
                print(bcolors.OKBLUE + gp.text + " ریال" + bcolors.ENDC + " |" + ' تاریخ:' + date[:16])
            # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
            for s in gold_symbols:
                self.symbol_list.append(s.text)

            for p in gold_prices[0]:
                self.price_list.append(p.text  + " ریال")

        # Silvers.
        silver_tbody_tag = tables[3].find('tbody')
        silver_rows = silver_tbody_tag.find_all('tr')
        counter2 = counter
        for sr in silver_rows:
            silver_prices = sr.find_all('td', attrs={'class': 'nf'})
            silver_symbols = sr.find_all('th')
            for ss in silver_symbols:
                counter2 += 1
                print(bcolors.HEADER + bcolors.BOLD + str(counter2) + "." + title.nextSibling.nextSibling.text + " " + ss.text, end=": " +
                                                                                                              bcolors.ENDC)
            for sp in silver_prices[0]:
                print(bcolors.OKBLUE + sp.text + " ریال" + bcolors.ENDC + " |" + ' تاریخ:' + date[:16])
            # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
            for s in silver_symbols:
                self.symbol_list.append(s.text)

            for p in silver_prices[0]:
                self.price_list.append(p.text + " ریال")

    def get_ounce(self):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        # International ounces.
        response = requests.get("https://www.tgju.org/gold-global")
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', attrs={'class': 'data-table'})
        tbody_tag = tables[0].find('tbody')
        thead_tag = tables[0].find('thead')
        title = thead_tag.find('th')
        rows = tbody_tag.find_all('tr')
        counter = 0
        for r in rows:
            prices = r.find_all('td', attrs={'class': 'nf'})
            symbols = r.find_all('th')

            for s in symbols:
                counter += 1
                print(bcolors.HEADER + bcolors.BOLD + str(counter) + "." + title.nextSibling.nextSibling.text + " " + s.text[:-1], end=": " +
                                                                                                                  bcolors.ENDC)
            for p in prices[0]:
                print(bcolors.OKBLUE + p.text + " ریال" + bcolors.ENDC + " |" + ' تاریخ:' + date[:16])
            # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
            for s in symbols:
                self.symbol_list.append(s.text)

            for p in prices[0]:
                self.price_list.append(p.text + " ریال")

    def get_gold_coin(self):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        # Gold coins.
        response = requests.get("https://www.tgju.org/coin")
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', attrs={'class': 'data-table'})
        # Same title for all.
        thead_tag = tables[0].find('thead')
        title = thead_tag.find('th')
        # First table.
        tbody_tag = tables[0].find('tbody')
        rows = tbody_tag.find_all('tr')
        counter = 0
        for r in rows:
            prices = r.find_all('td')
            symbols = r.find_all('th')
            for s in symbols:
                counter += 1
                print(bcolors.HEADER + bcolors.BOLD + str(counter) + "." + title.nextSibling.nextSibling.text + " " + s.text, end=": " +
                                                                                                             bcolors.ENDC)
            for p in prices[0]:
                print(bcolors.OKBLUE + p.text + " ریال" + bcolors.ENDC + " |" + ' تاریخ:' + date[:16])
            # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
            for s in symbols:
                self.symbol_list.append(s.text)

            for p in prices[0]:
                self.price_list.append(p.text + " ریال")

        # Second table.
        tbody_tag2 = tables[2].find('tbody')
        rows2 = tbody_tag2.find_all('tr')
        counter2 = counter
        for r2 in rows2:
            prices2 = r2.find_all('td')
            symbols2 = r2.find_all('th')
            for s2 in symbols2:
                counter2 += 1
                print(bcolors.HEADER + bcolors.BOLD + str(counter2) + "." + title.nextSibling.nextSibling.text + " " + s2.text, end=": " +
                                                                                                              bcolors.ENDC)
            for p2 in prices2[0]:
                print(bcolors.OKBLUE + p2.text + " ریال" + bcolors.ENDC + " |" + ' تاریخ:' + date[:16])
            # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
            for s2 in symbols2:
                self.symbol_list.append(s2.text)

            for p2 in prices2[0]:
                self.price_list.append(p2.text + " ریال")

    def get_currencies(self):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        # All main currencies for different countries.
        response = requests.get("https://www.tgju.org/currency")
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', attrs={'class': 'data-table'})
        # Same title for all.
        thead_tag = tables[0].find('thead')
        title = thead_tag.find('th')
        # First table.
        tbody_tag = tables[0].find('tbody')
        rows = tbody_tag.find_all('tr')
        counter = 0
        for r in rows:
            prices = r.find_all('td', attrs={'class': 'nf'})
            symbols = r.find_all('th')
            for s in symbols:
                counter += 1
                print(bcolors.HEADER + bcolors.BOLD + str(counter) + "." + title.nextSibling.nextSibling.text + " " + s.text, end=": " +
                                                                                                             bcolors.ENDC)
            for p in prices[0]:
                print(bcolors.OKBLUE + p.text + " ریال" + bcolors.ENDC + " |" + ' تاریخ:' + date[:16])

            # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
            for s in symbols:
                self.currency_symbol_list.append(s.text)

            for p in prices[0]:
                self.currency_price_list.append(p.text + " ریال")

        # Second table.
        tbody_tag2 = tables[1].find('tbody')
        rows2 = tbody_tag2.find_all('tr')
        counter2 = counter
        for r2 in rows2:
            prices2 = r2.find_all('td', attrs={'class': 'nf'})
            symbols2 = r2.find_all('th')
            for s2 in symbols2:
                counter2 += 1
                print(bcolors.HEADER + bcolors.BOLD + str(counter2) + "." + title.nextSibling.nextSibling.text + " " + s2.text, end=": " +
                                                                                                              bcolors.ENDC)
            for p2 in prices2[0]:
                print(bcolors.OKBLUE + p2.text + " ریال" + bcolors.ENDC + " |" + ' تاریخ:' + date[:16])

            # Creating target lists ("symbol_list", "price_list") for inserting our data to mysql database.
            for s2 in symbols2:
                self.currency_symbol_list.append(s2.text)

            for p2 in prices2[0]:
                self.currency_price_list.append(p2.text + " ریال")
