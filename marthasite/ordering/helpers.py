from .models import Order, MainDish, SideDishes, Dessert

def get_dessert_price(order_data):
    dessert_dict={"wadai":"Wadai", "dhal": "Dhal curry", "fish":"Fish curry"}
    price = 0
    for side_dish in  dessert_dict.keys():
        if order_data[side_dish]:
            price += SideDishes.objects.get(side_dish=dessert_dict[side_dish]).side_dish_price

    return price

def calculate_price(order_data):
    price = 0
    price += MainDish.objects.get(dish = order_data["main_dish"]).main_dish_price
    price += Dessert.objects.get(dessert = order_data["dessert"]).dessert_price
    price += get_dessert_price(order_data)
    return price
