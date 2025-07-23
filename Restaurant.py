MUFFIN= 5.95
KINGCAKE_SLICE =4.95
CROISSANT =3.95
SCONE = 3.75
CATFISH = 14.95
ROAST = 13.95
SAUSAGE = 12.95
GUMBO =5.95
CRAWFISH_SLICE = 3.65
CRAWFISH_PIE = 22
SALES_TAX = 0.0945

subtotal = 0.00
def Menu():
    print( "Boudreaux & Thibodeaux's Restaurant")
    print("1. Croissant: $" , CROISSANT)
    print("2. King Cake Slice: $" , KINGCAKE_SLICE)
    print("3. Crawfish Pie (By the slice): $" ,CRAWFISH_SLICE)
    print("4. Catfish Poboy: $" , CATFISH)
    print("5. Roast Beef Poboy: $" , ROAST)
    print("6. Sausage Poboy: $", SAUSAGE)
    print("7. Gumbo $" , GUMBO)
    print("---------\n")



Menu()

response = input( "What would you like to order? Type the appropriate number of the menu item:  ")

while(response.upper() != "DONE"):
    if(int(response) == 1):
        quant = float(input("how many would you like? "))
        print("Item added: " , quant, "x Croissant - $" , CROISSANT, )
        subtotal += quant*CROISSANT
    elif(int(response) == 2):
        quant = float(input("how many would you like? "))
        print("Item added: " , quant, "x Kingcake Slice - $" , KINGCAKE_SLICE, )
        subtotal += quant*KINGCAKE_SLICE
    elif(int(response) == 3):
        quant = float(input("how many would you like? "))
        print("Item added: " , quant, "x Crawfish Slice - $" , CRAWFISH_SLICE, )
        subtotal += quant*CRAWFISH_SLICE
    elif(int(response) == 4):
        quant = float(input("how many would you like? "))
        print("Item added: " , quant, "x Catfish Poboy - $" , CATFISH,)
        subtotal += quant*CATFISH
    elif(int(response) == 5):
        quant = float(input("Quantity: "))
        print("Item added: " , quant, "x Roast Beef Poboy - $" ,ROAST,)
        subtotal += quant*ROAST
    elif(int(response) == 6):
        quant = float(input("Quantity: "))
        print("Item added: " , quant, "x Sausage Poboy - $" ,SAUSAGE,)
        subtotal += quant*SAUSAGE
    elif(int(response) == 7):
        quant = float(input("Quantity: "))
        print("Item added:",quant, "x Gumbo - $",GUMBO,)
        subtotal += quant*GUMBO

        
    Menu()
    response = input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete: ")




total = subtotal  + (subtotal *SALES_TAX)
print(f'Your total is ${total:.2f}')
