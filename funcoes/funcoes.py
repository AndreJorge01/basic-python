# funcoes
# funcoes sao codigos que podemos chamar a todo momento no programa temos que sempre tpmar o cuidado de definir a funcao antes de chamá-la documentar a funcao (docstring) é uma das boas praticas de programacao

# funcao sem retorno e sem passagem de parametro
def ola_mundo():
    'retorna a mensagem padrao na tela'
    print('Olá Mundo')


ola_mundo()
help(ola_mundo)

# funcao sem retorno e com passagem de parametro
# name = input('Qual é o seu nome ? ')


# def bot(name):
#     'mensagem de introducao e apresentacao do bot'
#     print(f'Olá {name} eu sou o bot')


# bot(name)

# funcao com retorno e com passagem de parametro


def soma(a, b):
    'funcao que recebe dois numero e faz a soma entre eles'
    return a+b


resultado = soma(2, 2)

print(resultado)

