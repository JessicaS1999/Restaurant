MUFFIN= 5.95
KINGCAKE =4.95
CROISSANT =3.95
SCONE = 3.75
SALES_TAX = 0.0945

subtotal = 0.00

print( "b and t bakery")
print("1. Muffin: $" , MUFFIN)
print("2. Kingcake: $" , KINGCAKE)
print("3. Croissant: $" , CROISSANT)
print("4. Scone: $" , SCONE)
print("-----------------\n")


response = input( "what would you like to order ")

while(response.upper() != "DONE"):
    if(int(response) == 1):
        quant = float(input("how many would you like? "))
        print("you have ordered" , quant, "muffin(s) for $" , MUFFIN, "each")
        subtotal += quant*MUFFIN
    elif(int(response) == 2):
        quant = float(input("how many would you like? "))
        print("you have ordered" , quant, "kingcake(s) for $" , KINGCAKE, "each")
        subtotal += quant*KINGCAKE
    elif(int(response) == 3):
        quant = float(input("how many would you like? "))
        print("you have ordered" , quant, "croissant(s) for $" , CROISSANT, "each")
        subtotal += quant*CROISSANT
    elif(int(response) == 4):
        quant = float(input("how many would you like? "))
        print("you have ordered" , quant, "scone(s) for $" , SCONE, "each")
        subtotal += quant*SCONE
        
    response = input( "what would you like to order ")

total = subtotal  + (subtotal *SALES_TAX)
print(f'Your total is ${total:.2f}')
