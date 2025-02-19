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

# casa=float(input('Qual o valor da casa?:'))
# salario=float(input('Qual o seu salario?:'))
# m=int(input('Por quanto tempo você quer pagar o emprestimo?:'))
# prestação=casa/m
# if prestação>salario*0.3:
#     print('O emprestimo foi negado')
# else:
#     print('Parabens, o emprestimo foi aprovado!')

# num=int(input('Digite um numero inteiro:'))
# escolha=int(input('Escolha um numero de 1 a 3:'))
# if escolha==1:
#     print(bin(num))
# elif escolha==2:
#     print(oct(num))
# elif escolha==3:
#     print(hex(num))

# n1=int(input('Digite um numero:'))
# n2=int(input('Digite outro numero:'))
# if n1>n2:
#     print(f'{n1} é maior que {n2}')
# elif n1<n2:
#     print(f'{n1} é menor que {n2}')
# else:
#     print('Os valores são iguais')

# Alistamento Militar
# ano=int(input('Em que ano voce nasceu?:'))
# idade=2025-ano
# if idade<18:
#     print(f'Voçê devera se alistar em aproximadamente {18-idade}')
# elif idade>18:
#     print(f'Ja passou o tempo de alistamento, voce esta atrasado {idade-18} ano(s)')
# elif idade==18:
#     print(f'Você precisa se alistar esse ano!')

# n1=float(input('Qual foi sua priemira nota?:'))
# n2=float(input('qual foi sua segunda nota?:'))
# media=(n1+n2)/2
# if media<5.0:
#     print('Reprovado!')
# elif 5<media<6.9:
#     print('Você esta de recuperacao')

# Calculadora de IMC
# massa=float(input('Digite sua massa corporal (kg):'))
# altura=float(input('digite sua altura (m)'))
# imc=massa/(altura**2)
# if imc < 18.5:
#     print('Você está abaixo do peso ideal')
# elif 18.5 <= imc <= 24.9:
#     print('Você está no peso ideal')
# elif 25 <= imc <= 29.9:
#     print('Você está com sobrepeso')
# elif 30 <= imc <= 39.9:
#     print('Você está em obesidade')
# else:
#     print('Você está com obesidade mórbida')

# Loja
# v=float(input('Quanto custa o produto?'))
# print('Escolha uma forma de pagamento abaixo: \n [1] A vista no dinheiro com 10% de desconto \n [2] A vista no cartao com 5% de desconto\n [3] Parcelado em 2x no cartao (sem desconto)\n [4] Parcelado em 3x ou mais no cartão com 20% de juros')
# p=int(input('Sua escolha?'))
# if p==1:
#     total=v-(v*0.10)
# elif p==2:
#     total=v-(v*0.05)
# elif p==3:
#     total=v
# elif p==4:
#     total=v+(v*0.20)
# print(f'O produto vai custar {total}')

# Jokenpo
# from random import randint
# itens=('Pedra','Papel','Tesoura')
# computador=randint(0,2)
# print('''Suas opcões: \n [0] Pedra \n [1] Papel \n [2] Tesoura''')
# jogador=int(input('qual a sua jogada?:'))
# print('=='*16)
# print(f'O computador escolheu {itens[computador]}')
# print(f'Jogador jogou {itens[jogador]}')
# print('=='*16)
# if computador==0:
#     if jogador==0:
#         print('EMAPATE')
#     elif jogador==1:
#         print('Jogador venceu!')
#     elif jogador==2:
#         print('Computador venceu!')
#     else:
#         print('Opção invalida')
# elif computador==1:
#     if jogador == 0:
#         print('Computador venceu!')
#     elif jogador == 1:
#         print('EMPATE')
#     elif jogador == 2:
#         print('Jogador venceu!')
#     else:
#         print('Opção invalida')
# elif computador==2:
#     if jogador == 0:
#         print('Jogador venceu!')
#     elif jogador == 1:
#         print('Computador venceu!')
#     elif jogador == 2:
#         print('EMPATE')
#     else:
#         print('Opção invalida')
