# for c in range (1,10):
#     print(c)
# print('Fim!')
# OU
# c=1
# while c<10:
#     print(c)
#     c+=1
# from math import factorial

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

#Menu de opções
# pn=float(input('Primeiro valor:'))
# sn=float(input('Segundo valor:'))
# opcao=0
# resultado=0
# while  opcao!=5:
#     print(' [1} somar \n [2} multiplicar \n [3} maior \n [4} novos numeros \n [5} sair do programa')
#     opcao = int(input('>>>>> Qual é a sua opção?:'))
#     if opcao==1:
#         resultado=pn+sn
#         print(f'O resultado entre a soma de {pn} e {sn} é {resultado}')
#         break
#     elif opcao==2:
#         resultado=pn*sn
#         print(f'O resultado entre a multiplicação de {pn} e {sn} é {resultado}')
#         break
#     elif opcao==3:
#         resultado=max(pn,sn)
#         print(f'O maior numero entre {pn} e {sn} é {resultado}')
#         break
#     elif opcao==4:
#         print('Informe os numeros novamente:')
#         pn=float(input('Primeiro valor:'))
#         sn=float(input('Segundo valor:'))
#         break
#     elif opcao==5:
#         print('Finalizando...')
#     else:
#          print('Opção invalidade tente novamente')
# print('='*30)

# num=int(input('Digite um numero:'))
# print(f'O fatorial de {num}! é {factorial(num)}')
# Ou
# num=int(input('Digite um numero:'))
# c=num
# print(f'Calculando {num}! = ',end='')
# while c>0:
#     print(f'{c}',end='')
#     print(' x ' if c>1 else ' = ',end='')
#     c-=1
# print( factorial(num))

# num=0
# quanti=0
# soma=0
# while num!=999:
#     num=int(input('Digite um numero [999 para parar]:'))
#     if num==999:
#         break
#     soma+=num
#     quanti+=1
# print(f'A soma dos numeros digitados foi {soma} e a quantidade de numeros digitados foi {quanti}')

# Tabuada v3.0
# while True:
#     num = int(input("Digite um número para ver a tabuada (ou um número negativo para sair): "))
#     if num < 0:
#         print("Programa encerrado.")
#         break
#     print(f"\nTabuada de {num}:")
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")


# Par ou Impar
# import random
# from random import randint
# vitorias=0
# while True:
#     jogador=int(input('Digite um valor:'))
#     escolha=str(input('Escolha par ou impar?[P/I]')).strip().upper()[0]
#     computador=randint(0,10)
#     soma=jogador+computador
#     resultado= 'Par' if soma%2==0 else 'Impar'
#     print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma} -> {resultado} ')
#     if escolha == "P" and resultado == "Par" or(escolha == "I" and resultado == "Impar"):
#         print("🎉 Você venceu! Vamos jogar novamente...\n")
#         vitorias += 1
#     else:
#         print(' Você perdeu! Fim do jogo.')
#         break
# print(f"\nTotal de vitórias consecutivas: {vitorias}")
# Caixa eletronico
# print('='*23)
# print('    Banco do Brasil')
# print('='*23)
# dinheiro=int(input('Quanto voce quer sacar? R$'))
# total= dinheiro
# ced=50
# totced=0
# while True:
#     if total>=ced:
#         total-=ced
#         totced+=1
#     else:
#         if totced>0:
#         print(f'Total de {totced} cedulas de R${ced}')
#         if ced==50:
#             ced=20
#         elif ced==20:
#             ced=10
#         elif ced==10:
#             ced=1
#             totced=0
#         if total==0:
#             break
# print('Volte sempre ao Banco do Brasil! Tenha um bom dia!')

# Contador
# num=('zero','um','dois','tres','quatro','cinco','seis',
# 'sete','oito','nove','dez','onze','doze','treze','quatorze',
#  'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
# while True:
#       n=int(input('Digite um numero entre 0 e 20:'))
#       if 0<=n<=20:
#           break
#       print('tente novamente. ',end='')
# print(f'Voce digitou o numero {num[n]}')


