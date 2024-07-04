# retorno uma lista leftovers com o dinheiro que sobrou de cada transação
def make_purchases(purchase_orders) -> list:
    leftovers = []
    for order in purchase_orders:
        try:
            leftovers.append(purchase(order["price"], order["money_available"]))
        except Exception as e:
            print(e)
    
    return leftovers


def main():
    print("Making purchases...")
    leftovers = make_purchases(
        [
            {"price": 10.00, "money_available": 125.00},
            {"price": 5.00, "money_available": 2.00},
            {"price": 20.01, "money_available": 5.20},
            {"price": 1.04, "money_available": 254.00},
            {"price": 40.20, "money_available": 6.00},
            {"price": 16.00, "money_available": 235.01},
            {"price": 10.70, "money_available": 10.70},
            {"price": 12.00, "money_available": 2.30},
        ]
    )
    print("Purchases complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")
 
 
def purchase(price, money_available) -> list:
    if money_available < price:
        raise Exception(f"{money_available:.2f} is not enough for {price:.2f}")
    return money_available - price
 
 
main()
