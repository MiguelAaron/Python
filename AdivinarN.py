import random

N = random.randint(1,100)
U = 0
I = 6

U = input("Adivina el numero. Escribe un numero: ")

while I > 0 and U != N:
  if(U > N):
    U = input("Escribe un numero menor: ")
  else:
    U = input("Escribe un numero mayor: ")
  I -= 1
  
if U == N:
  print("Acertaste")

if I == 0:
  print "Perdiste. El numero era:",N

