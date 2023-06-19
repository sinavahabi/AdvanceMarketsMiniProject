"""
    Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
    Commands:
        pip install bs4
        pip install requests
        pip install jdatetime
"""

import re
import requests
from bs4 import BeautifulSoup
from ColorsClass.colors import bcolors
import jdatetime
# After importing all the essential packages that we need, our program is ready to begin.


class Bourse:
    def __init__(self):
        self.symbol_list, self.final_price_list, self.trade_price_list, self.trade_value_list, self.trade_volume_list, self.marketcap_list = [], [], [], [], [], []
        self.index_symbol_list, self.index_amount_list = [], []
        self.req_error = True

    # Scraping main data from target web.
    def get_stock_exchange_data(self, url):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        # This is where we make our method responsive with user interacts.
        try:
            # Handle if requests response status code is not OK.
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                result = soup.find('tbody')
                rows = result.find_all('tr')
                counter = 0
                # Reading symbols,final prices, trade prices, volume and market value of each share.
                for r in rows:
                    symbols = r.find_all('td', attrs={'data-col': 'info.symbol'})
                    final_prices = r.find_all('td', attrs={'data-col': 'info.last_price.PClosing'})
                    trade_prices = r.find_all('td', attrs={'data-col': 'info.last_trade.PDrCotVal'})
                    volume = r.find_all('td', attrs={'data-col': 'trades.QTotTran5J'})
                    trade_value = r.find_all('td', attrs={'data-col': 'trades.QTotCap'})
                    market_value = r.find_all('td', attrs={'data-col': 'trades.arzesh_bazar'})

                    for s in symbols:
                        counter += 1
                        symbols_output = re.sub(r'\s', '', s.text)
                        print(bcolors.BOLD + bcolors.HEADER + str(counter) + "." + 'نماد: ' + symbols_output + bcolors.ENDC, end=" |")
                    # Creating target lists ("symbol_list") for inserting our data to mysql database.
                    for s in symbols:
                        symbols_output = re.sub(r'\s', '', s.text)
                        self.symbol_list.append(symbols_output)

                    for p in final_prices:
                        prices_output = re.sub(r'\s', '', p.text)
                        print(bcolors.OKBLUE + ' قیمت پایانی: ' + prices_output + " ریال" + bcolors.ENDC,
                              end=" |")
                    # Creating target lists ("final_price_list") for inserting our data to mysql database.
                    for p in final_prices:
                        prices_output = re.sub(r'\s', '', p.text)
                        self.final_price_list.append(prices_output + " ریال")

                    for tp in trade_prices:
                        trade_prices_output = re.sub(r'\s', '', tp.text)
                        print(bcolors.OKBLUE + ' قیمت آخرین معامله: ' + trade_prices_output + " ریال" + bcolors.ENDC, end=" |")
                    # Creating target lists ("trade_price_list") for inserting our data to mysql database.
                    for tp in trade_prices:
                        trade_prices_output = re.sub(r'\s', '', tp.text)
                        self.trade_price_list.append(trade_prices_output + " ریال")

                    for tv in trade_value:
                        trade_value_amount = re.sub(r'[^,.0-9]', '', tv.text)
                        trade_value_unit = tv.next_element.next_element.text
                        print(bcolors.FAIL + ' ارزش معاملات: ' + trade_value_amount + " " + trade_value_unit + " ریال" +
                              bcolors.ENDC, end=" |")
                    # Creating target lists ("trade_value_list") for inserting our data to mysql database.
                    for tv in trade_value:
                        trade_value_amount = re.sub(r'\s', '', tv.text)
                        self.trade_value_list.append(trade_value_amount  + " ریال")

                    for v in volume:
                        volume_amount = re.sub(r'[^,.0-9]', '', v.text)
                        volume_unit = v.next_element.next_element.text
                        print(bcolors.FAIL + ' حجم معاملات: ' + volume_amount + " " + volume_unit +
                              bcolors.ENDC, end=" |")
                    # Creating target lists ("trade_volume_list") for inserting our data to mysql database.
                    for v in volume:
                        volume_amount = re.sub(r'\s', '', v.text)
                        self.trade_volume_list.append(volume_amount)

                    for m in market_value:
                        market_value_amount = re.sub(r'[^,.0-9]', '', m.text)
                        market_value_unit = m.next_element.next_element.text
                        print(bcolors.OKGREEN + ' ارزش بازار: ' + market_value_amount + " " + market_value_unit + " ریال" +
                              bcolors.ENDC + " |" + ' تاریخ:' + date[:16])
                    # Creating target lists ("marketcap_list") for inserting our data to mysql database.
                    for m in market_value:
                        market_value_amount = re.sub(r'\s', '', m.text)
                        self.marketcap_list.append(market_value_amount + " ریال")
            # If requests response receives an error "req_error" value will change to False and database module methods won't be called and ran.
            else:
                print(bcolors.WARNING + "Request error:", str(response.status_code) + bcolors.ENDC)
                self.req_error = False
        except requests.exceptions.RequestException as Error:
            pass

    def get_indicators(self):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        try:
            # Handle if requests response status code is not OK.
            response = requests.get("https://www.shakhesban.com/markets/index")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                result = soup.find('tbody')
                rows = result.find_all('tr')
                counter = 0
                # Reading symbols and amounts of each index.
                for r in rows:
                    symbols = r.find_all('td', attrs={'data-col': 'title'})
                    amounts = r.find_all('td', attrs={'data-col': 'value'})
                    for s in symbols:
                        counter += 1
                        symbols_outputs = s.find_all('h2')
                        for so in symbols_outputs:
                            print(bcolors.HEADER + bcolors.BOLD + str(counter) + "." + so.text + bcolors.ENDC, end=": ")
                        # Creating target lists ("index_symbol_list") for inserting our data to mysql database.
                        for so in symbols_outputs:
                            self.index_symbol_list.append(so.text)

                    for a in amounts:
                        amounts_outputs = re.sub(r'[^,.0-9]', '', a.text)
                        amounts_unit = a.next_element.next_element.text
                        amounts_unit_outputs = re.sub(r'\s', '', amounts_unit)
                        print(bcolors.OKGREEN + amounts_outputs + " " + amounts_unit_outputs + bcolors.OKGREEN + bcolors.ENDC +
                              " |" + ' تاریخ:' + date[:16])
                    # Creating target lists ("index_amount_list") for inserting our data to mysql database.
                    for a in amounts:
                        amounts_outputs = re.sub(r'[^,.0-9]', '', a.text)
                        amounts_unit = a.next_element.next_element.text
                        amounts_unit_outputs = re.sub(r'\s', '', amounts_unit)
                        self.index_amount_list.append(amounts_outputs + amounts_unit_outputs)
            # If requests response receives an error "req_error" value will change to False and database module methods won't be called and ran.
            else:
                print(bcolors.WARNING + "Request error:", str(response.status_code) + bcolors.ENDC)
                self.req_error = False

        except requests.exceptions.RequestException as Error:
            pass
