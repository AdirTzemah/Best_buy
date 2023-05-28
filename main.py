import products
import store


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(best_buy):
  while True:
    print("    Store Menu")
    print("     --------")
    print("1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit")
    domain = input("Please choose a number: ")
    if domain == "1":
      all_products = best_buy.get_all_products()
      for i, product in enumerate(all_products, start = 1):
          print(f"{i}. {product.show()}")
    elif domain == "2":
      total_quantity = best_buy.get_total_quantity()
      print("Total amount in store:", total_quantity)
    elif domain == "3":
      products = best_buy.get_all_products()
      for i, product in enumerate(products, start=1):
          print(f"{i}. {product.show()}")
      print("---------")
      print("When you want to finish order, enter empty text.")
      order_list = []
      while True:
          product_number = input("Which product # do you want? ")
          if not product_number:
              break
          product_index = int(product_number) - 1
          product = products[product_index]
          quantity = int(input("What amount do you want?  "))
          order_list.append((product, quantity))
      if order_list:
          total_price = best_buy.order(order_list)
          print("Order made! Total payment: $", total_price)
    elif domain == "4":
      break

def main():
   start(best_buy)

if __name__ == "__main__":
    main()




