primeiro_segmento = float(input("Digite o comprimento em metros do primeiro segmento:"))
segundo_segmento = float(input("Digite o comprimento em metros do segundo segmento:"))
terceiro_segmento = float(input("Digite o comprimento em metros do terceiro segmento:"))
try: 
#poderia ter usado a função 'and' para simplificar o codigo do que essa bagunça toda
    if primeiro_segmento < segundo_segmento + terceiro_segmento:
      print("Com estes comprimentos é possível formar um triângulo")
    elif segundo_segmento < primeiro_segmento + terceiro_segmento:
      print("Com estes comprimentos é possível formar um triângulo")
    elif terceiro_segmento < primeiro_segmento + segundo_segmento:
      print ("Com estes comprimentos é possível formar um triângulo")
    else:
      print("Não é possível formar um triângulo com estes comprimentos")

except ValueError:
 print("Entrada inválida. Digite um número!")


