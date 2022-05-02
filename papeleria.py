"""Papelería"""

print("\n--------------------------------------")
print("--------------PAPELERÍA---------------")
print("--------------------------------------\n")

# input

X =int(input("\nPrecio producto: "))

# processing

if X < 3000:
    msj = (f"EL precio de venta es igual a: {X + X*15/100}")
elif 3000 < X < 6000:
    msj = (f"EL precio de venta es igual a: {X + 500}")
else:
    msj = (f"EL precio de venta es igual a: {X + X*25/100}")

# output

print("\n"+msj)