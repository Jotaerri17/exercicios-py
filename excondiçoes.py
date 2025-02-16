# carro=int(input('Quantos anos seu carro tem?:'))
# if carro<=3:
#     print('seu carro é novo')
# else:
#     print('Seu carro esta velho')
#     print('Seu carro é novo' if carro<=3 else 'Seu carro esta velho')

# nota1=float(input('Qual foi a sua primeira nota?:'))
# nota2=float(input('Qual foi a segunda nota'))
# m=(nota1 + nota2)/2
# print(f'Sua media foi {m}')
# if m>=6:
#     print('Voce foi aprovado parabens!')
# else:
#     print('Voce foi reprovado')

# import random
# from random import randint
# numero_sorteado=randint(0, 5)
# chute=int(input('Chute um numero de 0 a 5:'))
# if chute==numero_sorteado:
#     print('Parabéns voce acertou!')
# else:
#     print('Nao foi dessa vez, tente denovo')
#     print(f'O numero sorteado era {numero_sorteado}')

# v=int(input('quantos km/h estava o carro?:'))
# multa= 65*(v-80)
# if v>80:
#     print(f'Voce foi multado em {multa} reais por execesso de velocidade')
# else:
#     print('Voce nao foi multado')

# distancia=float(input('Quantos kilometros vc vai percorrer?:'))
# if distancia<200:
#     p=0.50*distancia
#     print(f'O preço da passagem sera {p}')
# if distancia>200:
#     p2=0.45*distancia
#     print(f'O preço da passagem sera {p2}')

# n1=float(input('Digite um numero qualquer:'))
# n2=float(input('Digite outro numero:'))
# n3=float(input('Digite mais um numero:'))
# maior=max(n1,n2,n3)
# menor=min(n1,n2,n3)
# print(f'O maior numero entre os 3 é {maior} e o menor é {menor}')

# salario=float(input('Qual o valor do seu salario atual?:'))
# if salario>1250:
#     ns=salario+(salario*0.1)
#     print(f'Seu novo salario sera de {ns} reais')
# if salario<=1250:
#     ns=salario+(salario*0.15)
#     print(f'Seu novo salario sera de {ns} reais')

# a=float(input('Digite o valor da primeira reta:'))
# b=float(input('Digite o valor da segunda reta:'))
# c=float(input('Digite o valor da terceira reta:'))
# if a+b>c and a+c>b and c+b>a:
#     print('Pode ser formado um triangulo com esses segmentos')
# else:
#     print('Nao pode ser formado um triangulo com esses segmentos')