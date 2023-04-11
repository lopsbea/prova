# A prefeitura de Bebedouro abriu uma linha de crédito para os
# funcionários estatutários. O valor máximo da prestação não poderá ultrapassar
# 30% do salário bruto. Fazer um algoritmo que permita entrar com o salário bruto
# e o valor da prestação, e informar se o empréstimo pode ou não ser concedido.

salary = float(input('Digite o salário bruto: '))
value = float(input('Digite o valor da prestação: '))


if value <= salary * 30 / 100:
  print('Empréstimo pode ser concedido')
else:
  print('Empréstimo não pode ser concedido')