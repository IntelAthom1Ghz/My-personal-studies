import math
a = float(input("Digite o valor de a: "))
Letra_a = str(a) + 'X**2'
b = float(input("Digite o valor de b: "))
Letra_b = str(b) + 'X'
c = float(input("Digite o valor de c: "))
Letra_c = str(c)


print(f" Sua equação inteira é {Letra_a} + {Letra_b}+ {Letra_c}")
 
try:
    calculo_delta = b**2 - 4*a*c
    if calculo_delta < 0:
     print("Esta equação não apresenta Solução nos reais")
    elif calculo_delta > 0:
     calculo_raiz_X1= (-b + math.sqrt(calculo_delta))/(2*a)
     calculo_raiz_X2 = (-b - math.sqrt(calculo_delta))/(2*a)
     print(f"Esta equação apresenta 2 soluções reais, sendo estas {calculo_raiz_X1} e {calculo_raiz_X2}")
    else:
      calculo_raiz_deltazero = -b /(2*a)
      print(f" Esta equação apresenta apenas uma solução, sendo esta {calculo_raiz_deltazero}")

except ValueError:
     print("Insira um valor válido")
