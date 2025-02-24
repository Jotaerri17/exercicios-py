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

# n=int(input('Digite um numero:'))
# for c in range(0,n+1):
#     print(c)
# print('Fim')

 # Contagem regressiva
# from time import sleep
# for c in range(10,-1,-1):
#     print(c)
#     sleep(1)
# print('Fim')

# Contagem de numeros pares
# for n in range(2,51,2):
#      print(n, end=' ')
# print('Acabou')

# soma=0
# cont=0
# for c in range(1,501,2):
#     if c%3==0:
#         cont=cont+1
#         soma = soma+c
# print(f'A soma de todos os {cont} valores solicitados é {soma}')

# Tabuada v2.0
# num=int(input('Digite um numero para ver sua tabuada:'))
# for n in range(1,11):
#     print(f'{num} * {n} = {num*n}')

# Soma dos numeros pares
# soma=0
# cont=0
# for n in range(1,7):
#     num=int(input('Digite um numero:'))
#     if num%2==0:
#         soma=soma+num
#         cont=cont+1
# print(f'Voce informou {cont} numeros e a soma entre eles foi {soma}')

#P.A
# pm=int(input('Digite o primeiro termo:'))
    # razão=int(input('Qual a razão?:'))
    # decimo= pm+(11-1)*razão
    # for c in range(pm,decimo,razão):
    #     print(c, end=' -- ')
    # print('Fim!')

#Numeros primos
# num=int(input('Digite um numero: '))
# tot=0
# for c in range(1,num+1):
#     if num % c ==0:
#         print('\033[33m ', end=' ')
#         tot+= 1
#     else:
#         print('\033[31m',end=' ')
#     print(c, end=' ')
# print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
# if tot == 2:
#       print(f'{num} é primo')
# else:
#      print(f'{num} nao é primo')

#Detector de palindromo
# frase=str(input('Digite uma frase:')).strip().upper()
# palavras=frase.split()
# junto=''.join(palavras)
# inverso=''
# for letra in range(len(junto)-1,-1,-1):
#     inverso+=junto[letra]
# print(inverso)
# if inverso==junto:
#     print('Temos um palindromo')
# else:
#     print('A frase digitada nao e um palindromo')

# Grupo da maioridade
# import datetime
# atual=datetime.date.today().year
# totmaior=0
# totmenor=0
# for pess in range (1,8):
#     nasc = int(input(f'Em que ano {pess} pessoa nasceu?:'))
#     idade = atual - nasc
#     print(f'Essa pessoa tem {idade} anos')
#     if idade>=18:
#         totmaior+=1
#         print('Essa pessoa e maior de idade')
#     else:
#         totmenor+=1
#         print('Essa pessoa e menor de idade')
# print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
# print(f'E tivemos {totmenor} pessoas menores de idade')

#Maior e menos peso
# maior=0
# menor=0
# for p in range(1,8):
#     peso=float(input(f'Qual o peso da {p} pessoa?:'))
#     if p==1:
#         maior=peso
#         menor=peso
#     else:
#         if peso>maior:
#             maior=peso
#         if peso<menor:
#             menor=peso
# print(f'O maior peso lido foi de {maior}Kg')
# print(f'O menor peso lido foi de {menor}Kg')

# somaidade=0
# mediaidade=0
# maioridadehomem=0
# nomevelho=''
# totmulher20=0
# for p in range(1,5):
#     print(f'------- {p} PESSOA -------')
#     nome=str(input('Nome:')).strip()
#     idade=int(input('Idade:'))
#     sexo=str(input('Sexo [M/F]:')).strip()
#     somaidade+=idade
#     if p==1 and sexo in 'Mm':
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Mm' and idade>maioridadehomem:
#         maioridadehomem=idade
#         nomevelho = nome
#     if sexo in 'Ff' and idade<20:
#         totmulher20+=1
# mediaidade=somaidade/4
# print(f'A media de idade do grupo e de {mediaidade}')
# print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
# print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')