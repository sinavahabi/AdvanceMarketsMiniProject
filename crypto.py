# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install bs4
# pip install requests
# pip install jdatetime
import requests
from bs4 import BeautifulSoup
from ColorsClass.colors import bcolors
import jdatetime
# After importing all the essential packages that we need, our program is ready to begin.

url = "https://arzdigital.com/coins/"
# Crypto Urls
pages_list = [
    'page-1/', 'page-2/', 'page-3/', 'page-4/', 'page-5/',
    'page-6/', 'page-7/', 'page-8/', 'page-9/', 'page-10/',
    'page-11/', 'page-12/', 'page-13/', 'page-14/', 'page-15/',
    'page-16/', 'page-17/', 'page-18/', 'page-19/', 'page-20/'
]


class Crypto:
    def get_crypto_currency(self, value=1):
        numbers = range(0, value)
        # Getting current time (momentary year, month, day, etc).
        current_time = jdatetime.datetime.now()
        date = str(current_time)
        for num in numbers:
            response = requests.get(url + pages_list[num])
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find('table')
            thead = table.find('thead')
            dollar_price_title = thead.find('th', {'class': 'arz-coin-table__price-th'})
            rial_price_title = thead.find('th', {'class': 'arz-coin-table__rial-price-th'})
            market_cap_title = thead.find('th', {'class': 'arz-coin-table__marketcap-th'})
            volume_title = thead.find('th', {'class': 'arz-coin-table__volume-th'})
            tbody = table.find('tbody')
            rows = tbody.find_all('tr')
            for r in rows:
                counts = r.find_all('td', {'class': 'arz-coin-table__number-td'})
                names = r.find_all('td', {'class': 'arz-coin-table__name-td'})
                dollar_prices = r.find_all('td', {'class': 'arz-coin-table__price-td'})
                rial_prices = r.find_all('td', {'class': 'arz-coin-table__rial-price-td'})
                market_cap = r.find_all('td', {'class': 'arz-coin-table__marketcap-td'})
                volume = r.find_all('td', {'class': 'arz-coin-table__volume-td'})
                # Numbers.
                for c in counts:
                    print(bcolors.HEADER + bcolors.BOLD + c.text, end="-" + bcolors.ENDC)
                # Names.
                for n in names:
                    names_span = n.find_all('span')
                    for ns in names_span:
                        print(bcolors.HEADER + bcolors.BOLD + ns.text, end=" --> " + bcolors.ENDC)
                # Dollar prices.
                for dp in dollar_prices:
                    print(bcolors.OKBLUE + dollar_price_title.text + ": " + dp.text, end=" | " + bcolors.ENDC)
                # Rial prices.
                for rp in rial_prices:
                    prices_span = rp.find_all('span')
                    for ps in prices_span[1]:
                        print(bcolors.FAIL + rial_price_title.text + ": " + ps.text + " تومان", end=" | " + bcolors.ENDC)
                # Market cap.
                for m in market_cap:
                    print(bcolors.OKGREEN + market_cap_title.text + ": " + m.text, end=" | " + bcolors.ENDC)
                # Daily trading volume.
                for v in volume:
                    print(bcolors.OKGREEN + volume_title.text + ": " + v.text + "\n" + bcolors.ENDC +
                          " |" + ' تاریخ:' + date[:16])
