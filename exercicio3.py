# Construa um algoritmo que indique se um número digitado está
# compreendido entre 20 e 90 ou não (20 e 90 não estão na faixa de valores)

number = float(input('Digite um número: '))

if 20 < number < 90:
  print(f'{number} está entre 20 e 90.')
else:
  print(f'{number} não está entre 20 e 90.')
  