from enum import Enum

OFFER_DAYS = [0, 1, 2, 3, 4]  # the days in a week 0 is Monday and 4 is Friday -> weekday aka working hours
LUNCH_BEGIN = 11
LUNCH_BEGIN_MINUTE = 0
LUNCH_END_HOUR = 17
LUNCH_END_MINUTE = 0
DEFINE_DISH_ORDER = ["Soup", "Grey", "Green", "Yellow", "Red", "Blue"]


class Menu(Enum):
    menu_values = {
        'Grey': 4.95,
        'Green': 3.95,
        'Yellow': 2.95,
        'Soup': 2.50,
        'Red': 1.95,
        'Blue': 0.95}
