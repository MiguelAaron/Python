N = input("Escribe un numero: ")
F = 0
U = N
t = 0

while U > 1:
  
  if U == N:
    F += U
  else:
    F = F*U
  
  U = U-1

print "El factorial de", N, "es:", F

