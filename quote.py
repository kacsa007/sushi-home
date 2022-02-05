from collections import Counter


class Bill:

    def __init__(self, menu, dictionary_with_orders):
        self.menu = menu
        self.orders = {}
        self.validate_input(dictionary_with_orders)

    def join_bills_together(self, other_bill):

        self.orders = dict(Counter(self.orders) + Counter(other_bill.orders))
        return 0

    def print_order(self):
        print("This is what you have ordered: {}".format(self.orders))

    def check_dict_validity(self, dict_to_check):

        for key in dict_to_check.keys():      
            if key not in self.menu.keys():
                # item can't be found in the menu
                return False
            if not isinstance(dict_to_check[key], int):
                return False
        return True
    
    def add_items_to_order(self, items_to_add_dict):

        if len(items_to_add_dict) == 0: 
            return 0
        if not self.check_dict_validity(items_to_add_dict): 
            return -1
        self.orders = dict(Counter(self.orders) + Counter(items_to_add_dict))
        return 0

    def validate_input(self, dictionary_with_orders):
        if self.add_items_to_order(dictionary_with_orders) != 0:
            raise ValueError("Bill object initialization failed: Your input is not valid.")
