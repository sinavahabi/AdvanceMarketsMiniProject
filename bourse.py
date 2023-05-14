# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install bs4
# pip install requests
# pip install jdatetime
import re
import requests
from bs4 import BeautifulSoup
from ColorsClass.colors import bcolors
import jdatetime
# After importing all the essential packages that we need, our program is ready to begin.


class Bourse:
    # Scraping main data from target web.
    def get_stock_exchange_data(self, url):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        # This is where we make our method responsive with user interacts.
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find('tbody')
        rows = result.find_all('tr')
        # Reading symbols,final prices, trade prices, volume and market value of each share.
        for r in rows:
            symbols = r.find_all('td', attrs={'data-col': 'info.symbol'})
            final_prices = r.find_all('td', attrs={'data-col': 'info.last_price.PClosing'})
            trade_prices = r.find_all('td', attrs={'data-col': 'info.last_trade.PDrCotVal'})
            volume = r.find_all('td', attrs={'data-col': 'trades.QTotTran5J'})
            trade_value = r.find_all('td', attrs={'data-col': 'trades.QTotCap'})
            market_value = r.find_all('td', attrs={'data-col': 'trades.arzesh_bazar'})

            for s in symbols:
                symbols_output = re.sub(r'\s', '', s.text)
                print(bcolors.BOLD + bcolors.HEADER + 'نماد: ' + symbols_output + bcolors.ENDC, end=" |")

            for p in final_prices:
                prices_output = re.sub(r'\s', '', p.text)
                print(bcolors.OKBLUE + ' قیمت پایانی: ' + prices_output + " ریال" + bcolors.ENDC,
                      end=" |")

            for tp in trade_prices:
                trade_prices_outputs = re.sub(r'\s', '', tp.text)
                print(bcolors.OKBLUE + ' قیمت آخرین معامله: ' + trade_prices_outputs + " ریال" + bcolors.ENDC, end=" |")

            for tv in trade_value:
                trade_value_amount = re.sub(r'[^,.0-9]', '', tv.text)
                trade_value_unit = tv.next_element.next_element.text
                print(bcolors.FAIL + ' ارزش معاملات: ' + trade_value_amount + " " + trade_value_unit + " ریال" +
                      bcolors.ENDC, end=" |")

            for v in volume:
                volume_amount = re.sub(r'[^,.0-9]', '', v.text)
                volume_unit = v.next_element.next_element.text
                print(bcolors.FAIL + ' حجم معاملات: ' + volume_amount + " " + volume_unit +
                      bcolors.ENDC, end=" |")

            for m in market_value:
                market_value_amount = re.sub(r'[^,.0-9]', '', m.text)
                market_value_unit = m.next_element.next_element.text
                print(bcolors.OKGREEN + ' ارزش بازار: ' + market_value_amount + " " + market_value_unit + " ریال" +
                      bcolors.ENDC + " |" + ' تاریخ:' + date[:16])

    def get_indicators(self):
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        response = requests.get("https://www.shakhesban.com/markets/index")
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find('tbody')
        rows = result.find_all('tr')
        # Reading symbols and amounts of each index.
        for r in rows:
            symbols = r.find_all('td', attrs={'data-col': 'title'})
            amounts = r.find_all('td', attrs={'data-col': 'value'})
            for s in symbols:
                symbols_outputs = s.find_all('h2')
                for so in symbols_outputs:
                    print(bcolors.HEADER + bcolors.BOLD + so.text + bcolors.ENDC, end=": ")
            for a in amounts:
                amounts_outputs = re.sub(r'[^,.0-9]', '', a.text)
                amounts_unit = a.next_element.next_element.text
                amounts_unit_outputs = re.sub(r'\s', '', amounts_unit)
                print(bcolors.OKGREEN + amounts_outputs + " " + amounts_unit_outputs + bcolors.OKGREEN + bcolors.ENDC +
                      " |" + ' تاریخ:' + date[:16])
