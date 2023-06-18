"""
    Program: Advance Market Status
    Author: sina vahabi
    Copyright: 2023/05
"""

# Importing classes from other modules.
from database import LocalDB
from database import CryptoDB
from database import BourseDB
from ColorsClass.colors import bcolors

# Creating objects from imported classes.
local_obj = LocalDB()
crypto_obj = CryptoDB()
bourse_obj = BourseDB()

print(bcolors.BOLD + bcolors.HEADER + "Welcome to advance market status program. Choose one of the options bellow"
                                      " to start" + bcolors.ENDC)
print(bcolors.WARNING + "******************************************************************"
                        "******************************************" + bcolors.ENDC)

"""
Bourse and Fara-bourse data ordering list:
{without ordering, ordering by market value, ordering by final price, ordering by final trade, ordering by trade volume, 
ordering by trade value}
"""
bourse_urls = [
    "https://www.shakhesban.com/markets/stock?flow=1",
    "https://www.shakhesban.com/markets/stock?flow=1&sort=20&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=1&sort=2&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=1&sort=1&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=1&sort=5&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=1&sort=6&sort_type=desc"
]
fara_bourse_urls = [
    "https://www.shakhesban.com/markets/stock?flow=2",
    "https://www.shakhesban.com/markets/stock?flow=2&sort=20&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=2&sort=2&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=2&sort=1&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=2&sort=5&sort_type=desc",
    "https://www.shakhesban.com/markets/stock?flow=2&sort=6&sort_type=desc"
]
run = True


# Defining main function to make our program interactive with some primary options.
def running():
    global run
    user_input, user_input1, user_input2, user_input3, user_input_bourse, user_input_fara_bourse = 0, 0, 0, 0, 0, 0
    print(bcolors.OKBLUE + bcolors.BOLD + "1-Local Iran market." + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.BOLD + "2-Tehran Stock Exchange market [Bourse]" + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.BOLD + "3-Crypto Currency market" + bcolors.ENDC)
    print(bcolors.FAIL + bcolors.BOLD + "'Type 0 number to exit.'" + bcolors.ENDC)

    # Avoiding user invalid inputs.
    while True:
        try:
            user_input = int(input('Enter your choice: '))
            # If user intend to quit the program.
            if user_input == 0:
                print(bcolors.WARNING + "GOODBYE." + bcolors.ENDC)
                run = False
            # If user intend to go back from 'Iran Local' market menu.
            if user_input1 == 5:
                continue
            # If user intend to go back from 'Tehran Stock Exchange' market menu.
            if user_input2 == 4:
                continue
            # If user intend to go back from 'Crypto Currency' market menu.
            if user_input3 == 5:
                continue
            if user_input > 3:
                print(bcolors.FAIL + "Please Either choose number 1, 2 or 3. You can also choose '0'"
                                     " to exit" + bcolors.ENDC)
                continue
            if user_input < 0:
                print(bcolors.FAIL + "Please Either choose number 1, 2 or 3. You can also choose '0'"
                                     " to exit" + bcolors.ENDC)
                continue
        except:
            print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
            continue
        break

    # Checking some conditions.
    # If user chose Iran Local market option.
    if user_input == 1:
        print(bcolors.OKBLUE + bcolors.BOLD + "1: Gold and Silver price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "2: International Ounces price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "3: Gold Coins price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "4: International Currencies price." + bcolors.ENDC)
        print(bcolors.WARNING + bcolors.BOLD + "5: Type '5' to go back through menu." + bcolors.ENDC)
        print(bcolors.FAIL + bcolors.BOLD + "'Type 0 to exit.'" + bcolors.ENDC)
        while True:
            try:
                user_input1 = int(input('Enter your choice: '))
                # If user intend to quit the program.
                if user_input1 == 0:
                    print(bcolors.WARNING + "GOODBYE." + bcolors.ENDC)
                    run = False
                if user_input1 > 5:
                    print(bcolors.FAIL + "Please Either choose number 1, 2, 3 or 4. You can also choose '0' to exit or"
                                         " type '5' in order to go back through menu" + bcolors.ENDC)
                    continue
                if user_input1 < 0:
                    print(bcolors.FAIL + "Please Either choose number 1, 2, 3 or 4. You can also choose '0' to exit or"
                                         " type '5' in order to go back through menu" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
                continue
            break

        # If user chose 'Gold and Silver price' option.
        if user_input1 == 1:
            local_obj.get_data()
            local_obj.data_database()
            local_obj.symbol_list, local_obj.price_list = [], []
        # If user chose 'International Ounces price' option.
        if user_input1 == 2:
            local_obj.get_ounce()
            local_obj.data_database()
            local_obj.symbol_list, local_obj.price_list = [], []
        # If user chose 'Gold Coin price' option.
        if user_input1 == 3:
            local_obj.get_gold_coin()
            local_obj.data_database()
            local_obj.symbol_list, local_obj.price_list = [], []
        # If user chose 'International Currencies price' option.
        if user_input1 == 4:
            local_obj.get_currencies()
            local_obj.currencies_database()

    # If user chose Tehran Stock Exchange market option.
    if user_input == 2:
        print(bcolors.OKBLUE + bcolors.BOLD + "1: Bourse." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "2: Fara-Bourse." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "3: Indexes." + bcolors.ENDC)
        print(bcolors.WARNING + bcolors.BOLD + "4: Type '4' to go back through menu." + bcolors.ENDC)
        print(bcolors.FAIL + bcolors.BOLD + "'Type 0 number to exit.'" + bcolors.ENDC)
        while True:
            try:
                user_input2 = int(input('Enter your choice: '))
                # If user intend to quit the program.
                if user_input2 == 0:
                    print(bcolors.WARNING + "GOODBYE." + bcolors.ENDC)
                    run = False
                if user_input2 > 4:
                    print(bcolors.FAIL + "Please Either choose number 1, 2 or 3 You can also choose '0' to exit or"
                                         " type '4' in order to go back through menu" + bcolors.ENDC)
                    continue
                if user_input2 < 0:
                    print(bcolors.FAIL + "Please Either choose number 1, 2 or 3 You can also choose '0' to exit or"
                                         " type '4' in order to go back through menu" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
                continue
            break

        # If user chose 'Bourse' option.
        if user_input2 == 1:
            print(bcolors.OKGREEN + "1.Without Ordering:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "2.Ordering by Market Value:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "3.Ordering by Final Price:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "4.Ordering by Final Trade:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "5.Ordering by Trade Volume:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "6.Ordering by Trade Value:" + bcolors.ENDC)
            print(bcolors.WARNING + "7.Type '7' to go back through menu." + bcolors.ENDC)
            print(bcolors.FAIL + "'Type 0 number to exit.'" + bcolors.ENDC)
            while True:
                try:
                    user_input_bourse = int(input('Enter your choice: '))
                    # If user intend to quit the program.
                    if user_input_bourse == 0:
                        print(bcolors.WARNING + "GOODBYE." + bcolors.ENDC)
                        run = False
                    if user_input_bourse > 7:
                        print(bcolors.FAIL + "Please Either choose number between 1 to 6. You can also choose '0'"
                                             " to exit or type '7' in order to go back through menu" + bcolors.ENDC)
                        continue
                    if user_input_bourse < 0:
                        print(bcolors.FAIL + "Please Either choose number between 1 to 6. You can also choose '0'"
                                             " to exit or type '7' in order to go back through menu" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
                    continue
                break
            # If user chose 'Without Ordering' option in 'Bourse'.
            if user_input_bourse == 1:
                bourse_obj.get_stock_exchange_data(bourse_urls[0])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Market Value' option in 'Bourse'.
            if user_input_bourse == 2:
                bourse_obj.get_stock_exchange_data(bourse_urls[1])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Final Price' option in 'Bourse'.
            if user_input_bourse == 3:
                bourse_obj.get_stock_exchange_data(bourse_urls[2])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Final Trade' option in 'Bourse'.
            if user_input_bourse == 4:
                bourse_obj.get_stock_exchange_data(bourse_urls[3])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Trade Volume' option in 'Bourse'.
            if user_input_bourse == 5:
                bourse_obj.get_stock_exchange_data(bourse_urls[4])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Trade Value' option in 'Bourse'.
            if user_input_bourse == 6:
                bourse_obj.get_stock_exchange_data(bourse_urls[5])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []

        # If user chose 'Fara-Bourse' option.
        if user_input2 == 2:
            print(bcolors.OKGREEN + "1.Without Ordering:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "2.Ordering by Market Value:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "3.Ordering by Final Price:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "4.Ordering by Final Trade:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "5.Ordering by Trade Volume:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "6.Ordering by Trade Value:" + bcolors.ENDC)
            print(bcolors.OKGREEN + "7.Type '7' to go back through menu." + bcolors.ENDC)
            print(bcolors.FAIL + "'Type 0 number to exit.'" + bcolors.ENDC)
            while True:
                try:
                    user_input_fara_bourse = int(input('Enter your choice: '))
                    # If user intend to quit the program.
                    if user_input_fara_bourse == 0:
                        print(bcolors.WARNING + "GOODBYE." + bcolors.ENDC)
                        run = False
                    if user_input_fara_bourse > 7:
                        print(bcolors.FAIL + "Please Either choose number between 1 to 6. You can also choose '0'"
                                             " to exit or type '7' in order to go back through menu" + bcolors.ENDC)
                        continue
                    if user_input_fara_bourse < 0:
                        print(bcolors.FAIL + "Please Either choose number between 1 to 6. You can also choose '0'"
                                             " to exit or type '7' in order to go back through menu" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
                    continue
                break

            # If user chose 'Without Ordering' option in 'Fara-Bourse'.
            if user_input_fara_bourse == 1:
                bourse_obj.get_stock_exchange_data(fara_bourse_urls[0])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Market Value' option in 'Fara-Bourse'.
            if user_input_fara_bourse == 2:
                bourse_obj.get_stock_exchange_data(fara_bourse_urls[1])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Final Price' option in 'Fara-Bourse'.
            if user_input_fara_bourse == 3:
                bourse_obj.get_stock_exchange_data(fara_bourse_urls[2])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Final Trade' option in 'Fara-Bourse'.
            if user_input_fara_bourse == 4:
                bourse_obj.get_stock_exchange_data(fara_bourse_urls[3])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Trade Volume' option in 'Fara-Bourse'.
            if user_input_fara_bourse == 5:
                bourse_obj.get_stock_exchange_data(fara_bourse_urls[4])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []
            # If user chose 'Ordering by Trade Value' option in 'Fara-Bourse'.
            if user_input_fara_bourse == 6:
                bourse_obj.get_stock_exchange_data(fara_bourse_urls[5])
                bourse_obj.database_bourse()
                bourse_obj.symbol_list, bourse_obj.final_price_list, bourse_obj.trade_price_list, bourse_obj.trade_value_list, bourse_obj.trade_volume_list, bourse_obj.marketcap_list = [], [], [], [], [], []

        # If user chose 'Indexes' option.
        if user_input2 == 3:
            bourse_obj.get_indicators()
            bourse_obj.database_index()

    # If user chose Crypto Currency market option.
    if user_input == 3:
        print(bcolors.OKBLUE + bcolors.BOLD + "1: First 50 top crypto currencies." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "2: First 100 crypto currencies." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "3: First 500 crypto currencies." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "4: First 1000 crypto currencies." + bcolors.ENDC)
        print(bcolors.WARNING + bcolors.BOLD + "5: Type '5' to go back through menu." + bcolors.ENDC)
        print(bcolors.FAIL + bcolors.BOLD + "'Type 0 number to exit.'" + bcolors.ENDC)
        while True:
            try:
                user_input3 = int(input('Enter your choice: '))
                # If user intend to quit the program.
                if user_input3 == 0:
                    print(bcolors.WARNING + "GOODBYE." + bcolors.ENDC)
                    run = False
                if user_input3 > 5:
                    print(
                        bcolors.FAIL + "Please Either choose number 1, 2 or 3 You can also choose '0' to exit or"
                                       " type 3 in order to go back through menu" + bcolors.ENDC)
                    continue
                if user_input3 < 0:
                    print(
                        bcolors.FAIL + "Please Either choose number 1, 2 or 3 You can also choose '0' to exit or"
                                       " type 3 in order to go back through menu" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
                continue
            break

        # If user chose 'First 50 top Crypto Currencies' option.
        if user_input3 == 1:
            crypto_obj.get_crypto_currency(1)
            crypto_obj.database()
            crypto_obj.symbol_list, crypto_obj.dollar_price_list, crypto_obj.rial_price_list, crypto_obj.trade_volume_list, crypto_obj.marketcap_list = [], [], [], [], []
        # If user chose 'First 100 Crypto Currencies ' option.
        if user_input3 == 2:
            crypto_obj.get_crypto_currency(2)
            crypto_obj.database()
            crypto_obj.symbol_list, crypto_obj.dollar_price_list, crypto_obj.rial_price_list, crypto_obj.trade_volume_list, crypto_obj.marketcap_list = [], [], [], [], []
        # If user chose 'First 500 Crypto Currencies ' option.
        if user_input3 == 3:
            crypto_obj.get_crypto_currency(10)
            crypto_obj.database()
            crypto_obj.symbol_list, crypto_obj.dollar_price_list, crypto_obj.rial_price_list, crypto_obj.trade_volume_list, crypto_obj.marketcap_list = [], [], [], [], []
        # If user chose 'First 1000 Crypto Currencies ' option.
        if user_input3 == 4:
            crypto_obj.get_crypto_currency(20)
            crypto_obj.database()
            crypto_obj.symbol_list, crypto_obj.dollar_price_list, crypto_obj.rial_price_list, crypto_obj.trade_volume_list, crypto_obj.marketcap_list = [], [], [], [], []


# Calling last function in a while loop.
while run:
    running()
