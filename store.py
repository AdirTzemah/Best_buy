from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_counter_items = 0
        for item in self.products:
            total_counter_items += item.get_quantity()
        return total_counter_items

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products:
                total_price += product.buy(quantity)
        return total_price

# def main():
#     import products
#     product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
#                     products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                     products.Product("Google Pixel 7", price=500, quantity=250),
#                    ]

#     store = Store(product_list)
#     products = store.get_all_products()
#     print(store.get_total_quantity())
#     print(store.order([(products[0], 1), (products[1], 2)]))

# if __name__ == "__main__":
#     main()
from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_counter_items = 0
        for item in self.products:
            total_counter_items += item.get_quantity()
        return total_counter_items

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products:
                total_price += product.buy(quantity)
        return total_price

