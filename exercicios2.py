# for c in range (1,10):
#     print(c)
# print('Fim!')
# OU
# c=1
# while c<10:
#     print(c)
#     c+=1

# n=1
# par=impar=0
# while n!=0:
#     n=int(input('DIgite um valor:'))
#     if n!=0:
#         if n%2==0:
#             par+=1
#         else:
#             impar+=1
# print(f'vc digitou {par} numeros pares e {impar} numeros impares')

# sexo=str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
# while sexo not in 'MF':
#     print('Dados invalidos. Por favor digite novamente')
# print(f'Sexo {sexo} registrado com sucesso')


# import random
# from random import randint
# computador=randint(1,10)
# print('Sou seu computador...')
# print('Acabei de pensar em um numero de 0 a 10 \n Sera que vc consegue adivinhar qual foi?')
# acertou= False
# palpites=0
# while not acertou:
#     jogador = int(input('Qual o seu palpite?:'))
#     palpites += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#              print('Mais... Tente denovo')
#         elif jogador > computador:
#                 print('Menos... Tente denovo')
# print(f'Acertou! Com {palpites} palpites')


