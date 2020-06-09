# Program: couponCalculations.py
# Author: Matthew Gerling
# Last date modified: 06/9/2020


def calculate_price(price, cash_coupon, percent_coupon):

    if int(price) <= 10:
        shipping = 5.95
    elif 30 >= int(price) > 10:
        shipping = 7.95
    elif 50 >= int(price) > 30:
        shipping = 11.95
    elif int(price) > 50:
        shipping = 0

    tempPrice = int(price) - int(cash_coupon)
    Cost = tempPrice - (tempPrice * (int(percent_coupon)/100))
    finalCost = Cost + int(shipping)

    return print(f'The Final Price is {finalCost:0.2f}')


if __name__ == '__main__':
    itemPrice = input('What is the price of the item')

    coupon = input('Will you use a 5 or 10 coupon')

    if int(coupon) == 5:
        percentCoupon = input('Will you use a 10, 15, or 20 % coupon')
        if int(percentCoupon) == 10:
            calculate_price(itemPrice, 5, 10)
        if int(percentCoupon) == 15:
            calculate_price(itemPrice, 5, 15)
        if int(percentCoupon) == 20:
            calculate_price(itemPrice, 5, 20)
    if int(coupon) == 10:
        percentCoupon = input('Will you use a 10, 15, or 20 % coupon')
        if int(percentCoupon) == 10:
            calculate_price(itemPrice, 10, 10)
        if int(percentCoupon) == 15:
            calculate_price(itemPrice, 10, 15)
        if int(percentCoupon) == 20:
            calculate_price(itemPrice, 10, 20)

