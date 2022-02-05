import os

from constants import DEFINE_DISH_ORDER, OFFER_DAYS, LUNCH_BEGIN, LUNCH_BEGIN_MINUTE, \
    LUNCH_END_MINUTE, LUNCH_END_HOUR, Menu

from quote import Bill
from service import single_price_calculator

# basic input verification although parsing it not needed and this could be better implemented with unittests or pytest


def check_input_parser(lines):
    orders = []
    orders_count = []
    # Simple format check (just to help  in case of typos in the .txt provided)
    for line in lines:
        line_elements = line.split(',')
        is_int = True
        try:
            orders_count = list(map(int, line_elements))

        except ValueError:

            is_int = False

        if len(line_elements) != len(Menu.menu_values.value) or not is_int:
            raise Exception(
                "Wrong input format. The following line in the input does not have {} "
                "comma-separated integers: {}".format(len(Menu.menu_values.value), line))
        orders.append(orders_count)
    if len(orders) == 0:
        raise Exception("There's no customer order in the input file")

    return orders


def get_dict_from_order(order):

    # associate quantity values to dish names in a dictionary
    # zipping dictionary is adding some sort of complexity to this, but I'm using later default-dict to retrain data

    zip_iterator = zip(DEFINE_DISH_ORDER, order)
    dictionary_with_orders = dict(zip_iterator)

    return dictionary_with_orders


def get_bills_from_input(input_txt_path):
    # print(OrderA.__dict__.values())

    if not os.path.isfile(input_txt_path):
        raise Exception("File not found: {}".format(input_txt_path))
    try:
        with open(input_txt_path, 'r') as f:
            lines = f.readlines()
    except IOError:
        raise Exception('Problem reading input file: % s Check expected format in README.MD' % input_txt_path)

    orders = check_input_parser(lines)

    bills = []
    for order in orders:
        # associate dish names and quantity values into a dictionary
        dictionary_with_orders = get_dict_from_order(order)

        bills.append(Bill(Menu.menu_values.value, dictionary_with_orders))

    return bills


def lunch_time():
    # as you can see this is a basic function to calculate the time using a defined format
    my_string = '2022-01-27 13:25:56'

    from datetime import datetime
    my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M:%S")

    day = datetime.today().weekday()  # is it during the week?

    is_menu_day = day in OFFER_DAYS  # the check for time in the list
    date_time = datetime.now()

    start = date_time.replace(
        hour=int(LUNCH_BEGIN), minute=int(LUNCH_BEGIN_MINUTE))
    end = date_time.replace(hour=int(LUNCH_END_HOUR),
                            minute=int(LUNCH_END_MINUTE))
    date_time_now = datetime.now()
    is_lunch_time = start <= date_time_now < end

    is_lunch_menu_available = is_menu_day and is_lunch_time
    # hacking -> there is no kill switch so here we have by default always menu time
    is_lunch_menu_available = True
    date_time_now = my_date
    
    return is_lunch_menu_available, date_time_now


def print_single_quote(bill):
    # calculate a single bill for the group
    (is_lunch_menu_available, billing_date_time) = lunch_time()

    optimal_price = single_price_calculator(
        bill.orders, is_lunch_menu_available)

    print('\n')
    print("Bill date and time: {}".format(billing_date_time.strftime("%Y-%m-%d %H:%M")))
    print("Optimized price = {:.2f} Euro".format(optimal_price))
    print("Checking what you have ordered: {}".format(bill.orders))
    print('\n')


def print_group_quote(bills):

    # here we just have one case where we have the group bill and the single bill, but it's using the same methods
    (is_lunch_menu_available, billing_date_time) = lunch_time()

    cumulative_bill = Bill(Menu.menu_values.value, {})  # we instantiate the bill object inside the Bill class
    price_sum_of_separate_bills = 0
    for bill in bills:
 
        price_sum_of_separate_bills += single_price_calculator(
            bill.orders,  is_lunch_menu_available)
       
        cumulative_bill.join_bills_together(bill)

    optimal_group_price = single_price_calculator(
        cumulative_bill.orders, is_lunch_menu_available)
    # currently, the time is mocked -> I had no time to implement a
    # kill switch to have the current date or the menu date
    print('\n')
    
    print("Bill date and time: {}".format(
        billing_date_time.strftime("%Y-%m-%d %H:%M")))
    print("Sum of per person optimized prices: {:.2f} Euro".format(
        price_sum_of_separate_bills))

    if price_sum_of_separate_bills - optimal_group_price < 0:
        print("Actually this is not an Optimized price = {:.2f} Euro".format(optimal_group_price))
        print("Paying together you saved NOTHING -> someone's greedy and this is a negative number: {:.2f} Euro".format(
            price_sum_of_separate_bills - optimal_group_price))
    else:
        print("Actually this is an Optimized price = {:.2f} Euro".format(optimal_group_price))
        print("Paying together you really saved: {:.2f} Euro".format(
            price_sum_of_separate_bills - optimal_group_price))

    print("Checking what you have ordered: {}".format(cumulative_bill.orders))
   
    print('\n')


def print_bill(bills):
    if len(bills) > 1:  
        # if it is a group calculate cumulative optimized costs which are not always optimized as 
        # there could be cases when the result is negative so if you order separately you'll have cheaper options
        print_group_quote(bills)
    else:

        print_single_quote(bills[0])
