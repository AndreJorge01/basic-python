# if <condicao>
#  <bloco de codigo>
# <intrucoes>

# ou

# if <condicao>
# <bloco de codigo>
# elif <condicao2>
# <bloco de codigo>
# elif <condicao3>
# <bloco de codigo>
# else:
# <ultimo bloco>
# <intrucoes>

temp = eval(input('what is the weather today? '))

if temp >= 35:
    print('it is hot today')
elif temp <= 30:
    print('it is nice today')
elif temp <= 10:
    print('it is cold today')
else:
    print('it is very cold today')


# exercicos

# faca um programa que receba valores de 1 a 10 e retona para o usuario voce esta aprovado ou reprovado

nota = eval(input('what is your first grade?'))
nota2 = eval(input('What is your second grade?'))
media = (nota + nota2) / 2
if media >= 7:                      # ou (nota + nota2) % 2 >= 7:
    print(f'you are aproved wiht the average: {media}')
elif media > 5 and media < 7:        # ou (nota + nota2) % >= 5 <= 7:
    print(f'You need do another exame your average is: {media}')
else:
    print(f'You are reproved with the average: {media}')
