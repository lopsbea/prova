# Escreva um algoritmo que leia um número e informe se ele é
# divisível por 10, por 5 ou por 2 ou se não é divisível por nenhum deles

number = float(input('Digite um número: '))

if number % 10 == 0:
  print('É dividível por 10.')
if number % 5 == 0:
  print('É divisível por 5.')
if number % 2 == 0:
  print('É divisível por 2.')
if number % 2 != 0 and number % 5 != 0 and number % 10 != 0:
  print('Não é divisível por nenhum.')