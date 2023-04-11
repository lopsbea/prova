# A sequência de Fibonacci tem papel importante na explicação
# de fenômenos naturais. Ela é também bastante utilizada para fins estéticos, pela
# sua reconhecida harmonia. Exemplo disso foi sua utilização na construção do
# Partenon, em Atenas. A sequência dá-se inicialmente por dois números 1. A
# partir do terceiro elemento usa-se a expressão: elemento n = elementon1
# + elementon2. Exemplo de sequência: 1, 1, 2, 3, 5, 8. Construa um
# algoritmo que imprima na tela os 10 primeiros elementos da sequência de
# Fibonacci.

# 1 1 2 3 5 8 13 21 34 55

fibonacci = [1, 1]

for i in range(2, 10):
  n = fibonacci[i - 1] + fibonacci[i - 2]
  
  fibonacci.append(n)
    
print(fibonacci)