# Funcoes Built

# abs() -> retorna o valor absoluto de um numero
numeroNegativo = -10
valorNumeroNegativo = abs(numeroNegativo)
print(valorNumeroNegativo)

# min() -> retorna o valor minimo de uma sequencia numerica
minDaSequencia = (6, 7, 8, 9, 10)
valorMin = min(minDaSequencia)
print(valorMin)

# max() -> retorna o valor maximo de uma sequencia numerica

maxDaSequencia = (6, 7, 8, 9, 10)
valorMax = max(maxDaSequencia)
print(valorMax)

# sum() -> retorna a soma de uma sequencia numerica

sumDaSequencia = ({6, 7, 8, 9, 10})
valorSum = sum(sumDaSequencia)
print(valorSum)

# pow() -> exponenciacao
x = 3
y = 3
exponencicao = pow(x, y)
print(exponencicao)

# print() -> mostra o valor de saida de uma variavel
nome = 'andre'
print(nome)

# input() -> le um valor digitado no teclado do usuario
# seuNome = input('qual é o seu nome?')
# print(seuNome)

# help() -> mostra as funcionalidades de uma funcao
# help(max)

# exercicio

# calcule a soma dos numeros do 10 ao 14

calculo1 = ({10, 11, 12, 13, 14})
resultado1 = sum(calculo1)
print(resultado1)

# calcule a media entre os numeros 10, 15, 20
calculo2 = ({10, 15, 20})
resultado2 = sum(calculo2)
media = resultado2//3
print(media)

# peca para o usuario digitar duas notas de zero a dez e o peso das notas calcule a media ponderada entre elas
# exemplo(nota1*peso1+nota2*peso2)/(peso1+peso2)
# lembrando que a soma dos pesos tem que dar dez

nota1 = input('Digite o valor da nota1:')
nota1 = eval(nota1)
nota2 = input('Digite o valor da nota2:')
nota2 = eval(nota2)
peso1 = input('Digite o peso da nota1:')
peso1 = eval(peso1)
peso2 = input('Digite o peso da nota2:')
peso2 = eval(peso2)

media = (nota1*peso1+nota2*peso2) // (peso1+peso2)
print(f'a media final é: {media}')
