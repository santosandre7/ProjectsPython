"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 1, 2, 5, 6, 5, 8, 9, 10]]
x = 1
b = 0
c = 1
a = len(lista_de_listas_de_inteiros)

while a >= c:
    for i in range(len(lista_de_listas_de_inteiros[b])):
        for j in range(x, len(lista_de_listas_de_inteiros[b])):
            if i < j:
                if lista_de_listas_de_inteiros[b][i] == lista_de_listas_de_inteiros[b][j]:
                    print(lista_de_listas_de_inteiros[b][j])


    b += 1
    c += 1

