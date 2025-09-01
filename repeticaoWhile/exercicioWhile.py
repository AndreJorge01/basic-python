# exercicios

# faca um programa que calcule o fatorial de um numero, fonecido pelo usuario, por exemplo, cinco fatorial 5! = 5*4*3*2*1

numero = int(input('digite um numero para calcular seu fatorial '))
fatorial = 1

while numero > 1:
    fatorial *= numero
    numero -= 1
    print(f'o fatorial é {fatorial}')

# ou essa versao que chega no mesmo resultado mas nao é a forma mais pratica e correta

numero = int(input('digite um numero para calcular seu fatorial '))
fatorial = numero

while numero >= 2:
    fatorial = fatorial * (numero - 1)
    numero -= 1  # numero = numero - 1
    print(fatorial)


numero = eval(input('digite um numero para calcular seu fatorial '))

fatorial = 1

if numero < 0:
    print('Nao existe fatorial para numeros negativos')
elif numero == 0 or numero == 1:
    print(f'Fatorial de {numero} é 1')
else:
    for i in range(1, numero + 1):
        fatorial = fatorial + i
        print(f'O fatorial de {numero} é {fatorial}')


# crie um aplicativo de cofre, onde o usuario tem 3 tentativas de acertar a senha, caso ele erre retorne a mensagem senha incorreta, caso ele acerte retorne senha correta acesso concedido

# senha_correta = 1234 versao com numero inteiro ( nao é o ideal caso a senha tenha letras porque sao string)
senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    # senha = int(input('digite a senha do cofre: ')) para a versao de numero inteiro precisa usar o int() para transforma a string retornada por input() em inteiro
    senha = input('digite a senha do cofre: ')

    if senha == senha_correta:
        print('senha correta acesso concedido')
        break
    else:
        tentativas -= 1
        print('senha incorreta tente novamente')

    if tentativas > 0:
        print(f'voce tem mais {tentativas} tentativas')
    else:
        print('acesso bloqueado voce execeu o numero maximo de tentativas')


# ou

senhaCorreta = "0000"
tentativas = 3

while tentativas != 0:
    tentativa = input('digite sua a senha ')

    if tentativa == senhaCorreta:
        print('senha correta acesso concedido')
        break
    else:
        tentativas -= 1
        print(f'senha incorreta voce tem mais {tentativas} tentativas')
    if tentativas != 0:
        print('tente novamente')
    else:
        print('numero maximo de tentativas execido')
