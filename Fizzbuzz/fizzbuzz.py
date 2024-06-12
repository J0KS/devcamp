lista = []
for i in range(1,100):
  if i%3 == 0 and i%5 == 0:
    lista.append("Fizz Buzz")
  elif i%3 == 0:
    lista.append("Fizz")
  elif i%5 == 0:
    lista.append("Buzz")
  else:
    lista.append(i)

print(lista)