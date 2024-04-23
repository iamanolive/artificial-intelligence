import string

def solution(total_money, quantity, price):
    result = "I have {total_money} {value1} so I can buy {quantity} {value2} for {price:.2f} {value3}"
    quantities = ["dollar", "football", "dollar"]
    if total_money != 1:
        quantities[0] = "dollars"
    if quantity != 1:
        quantities[1] = "footballs"
    if price != 1:
        quantities[2] = "dollars"

    print(result.format(total_money = total_money, value1 = quantities[0], quantity = quantity, value2 = quantities[1], price = price, value3 = quantities[2]))

total_money_input = int(input())
quantity_input = int(input())
price_input = float(input())

solution(total_money_input, quantity_input, price_input)