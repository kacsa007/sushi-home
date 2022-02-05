from constants import Menu
from collections import defaultdict


def set_flags_special_dish(dictionary_with_orders):


    if 'Red' in dictionary_with_orders or 'Blue' in dictionary_with_orders or 'Soup' in dictionary_with_orders:
        return True
    else:
        return False


def menu_tuple(menu_dictionary):

    list_tuple = [(k, v) for k, v in menu_dictionary.items()]

    return list_tuple


def menu_items_by_descending_price():

    menu_dict = Menu.menu_values.value
    return menu_dict


def split_dictionary(orders_dict):

    orders_dict = defaultdict(int, orders_dict)
    not_menu_keys = ["Grey", "Green", "Yellow"]
    menu_dish_keys = ["Soup", "Red", "Blue"]

    # used lambda here to split my dictionary - it can be changed to just a def filter_dictionary(x)
    # where x=not menu_keys or menu_dish_keys
    filter_dictionary = lambda keys: {x: orders_dict[x] for x in keys}

    not_menu_dish = filter_dictionary(not_menu_keys)
    menu_dish = filter_dictionary(menu_dish_keys)
    return not_menu_dish, menu_dish


def single_price_calculator(orders_dict, lunch_menu_available):
    # we narrowed down the requirements from user stories to just one algorithm
    # It was a long and exhausting work to approach this
    # see readme.md for cleared information about the approaches used in this algorithm

    menu_items = (menu_items_by_descending_price())
    sum_order = 0

    orders_dict = defaultdict(int, orders_dict)
    n_dishes = sum(orders_dict.values())
    flag_its_more = False

    # there's no need to have a manu but this can be redundant as my algorithm is robust(hopefully), but I kept it here

    if len(orders_dict) <= 3 or not set_flags_special_dish(orders_dict):
        print("here")
        # exit(1)
        not_optimal_price = sum([menu_items[key] * orders_dict[key] for key in orders_dict])
        print(not_optimal_price)
        # exit(1)
        if not_optimal_price <= 8.5:

            return not_optimal_price
        else:
            # print("irrr")
            # exit(1)
            flag_its_more = True

    if not lunch_menu_available or n_dishes < 5 or not set_flags_special_dish(orders_dict):
        # simple sum without any menu combinations
        # list comprehension is much efficient than using the if/else method with a for loop
        not_optimal_price = sum([menu_items[key] * orders_dict[key] for key in orders_dict])

        return not_optimal_price

    elif set_flags_special_dish(orders_dict) or flag_its_more:

        number_of_soup = orders_dict['Soup']
        number_of_special_dish_red = orders_dict['Red']
        number_of_special_dish_blue = orders_dict['Blue']

        total_special = number_of_special_dish_blue+number_of_special_dish_red+number_of_soup
        number_of_menus = int((total_special*n_dishes)/(total_special*5))
        dish_with_menu = number_of_menus*5

        optimal_price = 8.5 * number_of_menus

        not_special_dishes = split_dictionary(orders_dict)[0]
        special_dishes = split_dictionary(orders_dict)[1]

        used_menu_dishes = 0

        for key_not_special, order_not_special in not_special_dishes.items():
            sum_order += not_special_dishes[key_not_special]

            if sum_order <= dish_with_menu:
                not_special_dishes[key_not_special] = 0
            else:
                not_special_dishes[key_not_special] = (sum_order % 5)+number_of_menus
                used_menu_dishes = int(sum_order/5)

        optimal_price += sum([menu_items[key] * not_special_dishes[key] for key in not_special_dishes])

        if used_menu_dishes == 0:
            used_menu_dishes = dish_with_menu-sum_order

        if special_dishes.get('Soup') != 0:
            while used_menu_dishes != 0:
                special_dishes['Soup'] -= 1
                used_menu_dishes -= 1
                if special_dishes.get('Soup') == 0 or used_menu_dishes == 0:
                    break

        if used_menu_dishes != 0 and special_dishes.get('Red') != 0:

            while used_menu_dishes != 0:
                special_dishes['Red'] -= 1
                used_menu_dishes -= 1
                if special_dishes.get('Red') == 0 or used_menu_dishes == 0:
                    break

        if used_menu_dishes != 0 and special_dishes.get('Blue') != 0:
            while special_dishes.get('Blue') != 0 or used_menu_dishes != 0:
                special_dishes['Blue'] -= 1
                used_menu_dishes -= 1
                if special_dishes.get('Blue') == 0 or used_menu_dishes == 0:
                    break

        individual = sum([menu_items[key] * special_dishes[key] for key in special_dishes])
        optimal_price += individual

        return optimal_price
