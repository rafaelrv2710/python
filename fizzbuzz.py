numero = 1
while numero <= 100:
     if numero % 3 == 0 and numero % 5 == 0:
        print("fizzBuzz")
     elif numero % 5 == 0:
        print("buzz")
     elif numero % 3 == 0:
         print("fizz")
     else:
         print(numero)    
     numero = numero + 1
        
    
