# faca um programa que gera tabela de mutiplicacao,o programa deve pergintar ao usuario qual tabuada ele quer e até que valor da tabuada sera mostrado, sempre comecando pelo zero ( geralmente é do zero ao dez )

# tabuada = int(input('qual numero voce quer calcular? '))
# numero_maximo = int(input('Até que valor voce quer calcular? '))

# for i in range(numero_maximo + 1):
#     resultado = tabuada * i

#     print(f'{tabuada} x {i} = {resultado}')

# ou mais curto e direto

# numero_tabuada = int(input('qual numero voce quer calcular? '))
# tabuada_maxima = int(input('Até que valor voce quer calcular? '))
# for numero in range(0, tabuada_maxima+1):
#     print(f'{numero_tabuada}x{numero}={numero_tabuada*numero}')

# faca um programa que calcule o énesimo elemento da serie de fibonacci, lembrando que a serie comeca dessa forma 1,1,2,3,5,8...
# n = int(input('qual element0 deve ser mostrado?'))

# # corrigir depois
# def fibonacci(n):
#     if n <= 0:
#         return "A posição deve ser um número inteiro positivo."
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         a = 1
#         b = 1
#         for _ in range(3, n + 1):
#             proximo_termo = a + b
#             a = b
#             b = proximo_termo
#         return b

n = int(input('qual element0 deve ser mostrado?'))
a = 1
b = 1

if n == 1 or n == 2:
    print(1)

else:
    for _ in range(2, n):
        elemento = a + b
        b = a
        a = elemento
        print(elemento) # remover da identacao para mostrar somente so o numero desejado
