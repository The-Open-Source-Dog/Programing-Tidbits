#A simple python password genrator
import random,string
try:r=int(input("Length?:"))
except:r=20
for _ in range(r):print(str(random.choice(string.ascii_letters+string.digits+'!@#$%^&*()?')),end='')
