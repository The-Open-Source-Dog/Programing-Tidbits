#Sort People into even groops and retern the amount of people left over.
try:
    a=int(input("How Many People?: "))
    b=int(input("How Many Groops?: "))
except:
    a=2
    b=4
print((a -(b * (a // b)))
