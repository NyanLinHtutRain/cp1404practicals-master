# function main()
#     get num items
#     while num items < 0
#         display Invalid
#         get num items
#
#     prices = []
#     for i in range(num items)
#         get price
#         while price < 0
#             display Invalid
#             get price
#
#         prices.append(price)
#
#     total price = calculate total price(num items, prices)
#
#     display total_price
#
#
# function calculate total price(num items, prices)
#     total price = sum(prices)
#
#     if total price > 100
#         discount = 0.10 * total_price
#         total_price -= discount
#
#     return total price
#
#
# main()
#

def main():
    # Input validation loop for the number of items
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid input! Please enter a valid integer.")
        num_items = int(input("Number of items: "))

    prices = []
    for i in range(num_items):
        price = float(input(f"Price of item {i + 1}: "))
        while price < 0:
            print("Invalid input! Please enter a valid number.")
            price = float(input(f"Price of item {i + 1}: "))

        prices.append(price)

    total_price = calculate_total_price(num_items, prices)

    print(f"Total price for {num_items} items is ${total_price:.2f}")


def calculate_total_price(num_items, prices):
    total_price = sum(prices)

    if total_price > 100:
        discount = 0.10 * total_price
        total_price -= discount

    return total_price


main()
