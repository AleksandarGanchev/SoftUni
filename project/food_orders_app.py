from project.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        ...

    def add_meals_to_menu(self, *meals: Meal):
        ...

    def show_menu(self):
        ...

    def add_meals_to_shopping_cart(self, client_phone_number: str, ** meal_names_and_quantities):
        ...

    def cancel_order(self, client_phone_number: str):
        ...

    def finish_order(self, client_phone_number: str):
        ...

    def __str__(self):
        ...
