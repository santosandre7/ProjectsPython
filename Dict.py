import copy


#Dicionário é uma coleção que guarda valores multidimensionais para cada índice, diferente de uma lista encadeada,
# que guarda apenas um valor por vez.

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}
#Para imprimir um valor, é só chamar pela sua chave como no exemplo abaixo.

print(d1['str'])
#Se eu chamar um valor que não existe no dicionário o Python vai lançar um erro e não vai continuar o código.
# (ao executar o código descomente a linha com o código inferior.)

# print(d1['chaveNaoExistente'])
# print('Oi')

# Para contornar isso podemos usar o '.get', pois o .get trás um valor 'None' e não interrompe o código.

print(f'Testando o .get {d1.get("chaveNaoExistente")}')
print('Oi')

#Você pode atualizar os valores da seu dicionário.

d1['str'] = 'newValue'
print(d1['str'])

#Você pode adicionar novo valor na sua chave utilizando UPDATE
d1.update({'nova_chave': 'novo_valor'})
print(d1)

#Você pode checar se existe uma chave ou um valor dentro de um dicionário

print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())

# Preste que retorno FALSE para {'valor' in d1.values()}.
# Isso aconteceu porque a gente alterou o dicionário nos passos anteriores para 'newValue'
# Vamos trocar 'valor' > 'newValue'. Agora si

print('str' in d1)
print('str' in d1.keys())
print('newValue' in d1.values())

#Imprimindo os valores do dicionário em um laço FOR.

for k in d1.items():
    print(k)

for k, v in d1.items():
    print(k, v)

#Vamos pra outro exemplo.

clientes = {
    'cliente1': {
        'Nome': 'Luiz',
        'Sobrenome': 'Otávio'
    },
    'cliente2': {
        'Nome': 'Andre',
        'Sobrenome': 'Santos'
    },

}

for clientes_k, clientes_v in clientes.items():
    print(f'Dados do {clientes_k}')
    for chave, valor in clientes_v.items():
        print(f'\t{chave}: {valor}')



#Copiando Dicionário
n = {1: 'a', 2: 'b', 3: 'c'}

n_copy = n.copy()
n_copy[1] = 'Luiz'

print(f'n{n}')
print(f'n_copy{n_copy}')

#Preste atenção que Luiz só foi alterado apenas em "n_copy".
#Vamos pra outro exemplo.

n = {1: 'a', 2: 'b', 3: 'c', 'd': ['Pitico', 'Wendel']}
n_copy = n.copy()

n_copy[1] = 'Luiz'
n_copy['d'][0] = 'Pedrinho'

print(f'n{n}')
print(f'n_copy{n_copy}')

#Vimos que foi alterado 'n' e 'n_copy'.
#Então pra fazer realmente uma cópia, precisamos utilizar o 'import copy' e a função 'deepcopy()'.
#Preste atenção que agora somente 'n_copy' foi alterado.

n = {1: 'a', 2: 'b', 3: 'c', 'd': ['Pitico', 'Wendel']}
n_copy = copy.deepcopy(n)

n_copy[1] = 'Luiz'
n_copy['d'][0] = 'Pedrinho'

print(f'n{n}')
print(f'n_copy{n_copy}')

#Podemos concatenar dois dicionários.
# Se nos dois tiverem a mesma chave, o valor prevalecerá do segundo, no caso o que está sendo adicionado.

n = {1: 'a', 2: 'b', 3: 'c'}
n1 = {1: 'b', 2: 'c', 3: 'd', 4: 'd'}

n.update(n1)
print(n)

