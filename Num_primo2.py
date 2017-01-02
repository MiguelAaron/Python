min = input("Escribir a partir de que numero se comenzara: ")
max = input("Escribir hasta que numero se terminara: ")
R = range(min, (max+1))
s = 0 #+1 si la division tiene un residuo igual a 0
c = 1 #Dividendos del numero a verificar

for n in R: #n es el numero a verificar
  
  while c <= max: #Dividendos, desde 1 hasta n
  
    if n%c == 0:
      s += 1
    
    c += 1
    
  if s == 2:
    print(n, "Numero primo")
  
  s = 0
  c = 1
