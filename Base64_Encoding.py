import base64

z1 = str(input("Data : "))
z2 = z1.encode("ascii")

z3 = base64.b85encode(z2)
z4 = z3.decode("ascii")



print(z4)