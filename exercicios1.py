'''
#1 informe o valor lógico (true ou false) para as proposições lógicas abaixo:
a - (true) 2*4 == 24/3
b - (false) (15 % 4)<(19 % 6)
c - (true) !(2<5)!=(8 == 8)
d - (false) True or False
e - (true | 2**2 == math.pow(2,2)
f - (false) False and ((7/2)>3.5)
g - (true) (math.ceil(2.5) == 3 and (math.sqrt(9)==3)
'''

#2 tamanho em milimitros
m_metro = float(input("Digite o valor em metro: "))
print("O valor em milímetros é: ", m_metro*1000)

#-----------------------------------------------------

#3 calculo, dias, horas, minutos e segundos do usuario
dias = float(input("Digite o número dias: "))
horas = float(input("Digite o número horas: "))
minutos = float(input("Digite o número minutos: "))
segundos = float(input("Digite o número segundos: "))
total = dias*86400+horas*3600+minutos*60+segundos
print("A quantidade total em segundos fica: ", total)

#-----------------------------------------------------

#4 aumento salarial
salario_atual = float(input("Digite seu salário atual: ")) 
porcento_aumento_salarial = float(input("Digite a porcentagem recebida em sua promoção: ")) 
salario_com_aumento = float(porcento_aumento_salarial / 100 * salario_atual) 
print("Você recebeu um aumento de:",porcento_aumento_salarial*salario_atual/100,"seu salário passou a ser: ",salario_com_aumento+salario_atual)

#-----------------------------------------------------
a
#5 preço desconto
preco_mercadoria = float(input("Digite o preço da mercadoria: ")) 
desconto = float(input("Digite a porcentagem de desconto: ")) 

mercadoria_com_desconto = float(preco_mercadoria / 100 * desconto) 

print("Você recebeu um desconto de:",preco_mercadoria*desconto/100,"Total a ser pago: ",preco_mercadoria-mercadoria_com_desconto)

#-----------------------------------------------------

#6 tempo viagem 6
distancia_viagem = float(input("Digite a distância da sua viagem em km: "))
tempo_viagem = float(input("Digite a velocidade que pretende ir: "))
print("Nesta velocidade Sem paradas você levará : ", distancia_viagem/tempo_viagem, "horas para chegar lá")

#-----------------------------------------------------

#7 temperatura celsius > fahrenheit 7
temperatura_celsius = 27
print("A temperatura atual em célcius é: ", temperatura_celsius, "graus, já em Fahrenheit é: ",9*temperatura_celsius/5+32,"graus")

#-----------------------------------------------------

#8 quilometros percorridos 
distancia_viagem = float(input("Digite a distância da sua viagem em km: "))
dias_viagem = float(input("Digite a quantidade de dias que pretende utilizar o carro: "))
print("Nesta viajem você utilizou: R$",dias_viagem*60, "em",dias_viagem,"em diárias, e R$",distancia_viagem*0.15, "no total de",distancia_viagem,"km rodados no período.")

#-----------------------------------------------------

#9 tempo em dias de vida perdidos por fumante
qntCigarros = int(input("Qnts cigarros por dia: "))
anosFumando = int(input("Anos fumando: "))

totalCigarros = (anosFumando * 365)*qntCigarros
diasPerdidos = (totalCigarros * 10)/24

print ('Dias perdidos %d' %diasPerdidos )

#-----------------------------------------------------

import match

metros_a_pintar = int(input('qual o tamanho a pintar'))
litros_necessarios = (metros_a_pintar / 6)

#questao a)
latas_necessarias = math.ceil(litros_necessarios / 18)
print(latas_necessarias)

#questao b)
galoes_necessarios = math.ceil(litros_necessarios / 3.6)
print("sera necessario: ", galoes_necessarios, " galoes")

#questao c)
latas_necessarias = int(litros_necessarios / 18)
faltou = litros_necessarios % 18
galoes_necessarios = math.ceil(faltou / 3.6)

print("foram necessarios ", latas_necessarias, "latas")























