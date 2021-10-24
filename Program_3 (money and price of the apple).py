Amountofmoney = int(input("Enter the amount of money: "))
Priceofapple = int(input("Enter the price of the apple: "))

Applesyoucanbuy = int(Amountofmoney / Priceofapple)
Totalamount = int(Applesyoucanbuy * Priceofapple) 

Change = int(Amountofmoney - Totalamount)

print(f'You can buy {Applesyoucanbuy} apples and your change is {Change} pesos.')