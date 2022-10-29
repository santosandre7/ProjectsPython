#Lambda é uma função anônima que já tem dentro dela um return.

# def func(item):
#     return item[1]
# lista.sort(key=func)

# Isso em cima é a mesma coisa disso aqui:

# lista.sort(key=lambda item: item[1])



lista = [
    ['P1', 5],
    ['P2', 4],
    ['P3', 3],
    ['P4', 2],
    ['P5', 1],
]

# def func(item):
#     return item[1]
# lista.sort(key=func)

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

