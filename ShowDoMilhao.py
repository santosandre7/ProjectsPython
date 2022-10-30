#Teste de GitCommit e GitPush
from time import sleep

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quem abriu o mar vermelho? ',
        'alternativas': {
            'a': 'Abraão',
            'b': 'Moisés',
            'c': 'Faraó',
            'd': 'Jacó',
        },
        'alternativa_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Qual cargo José ocupou no Egito? ',
        'alternativas': {
            'a': 'Escravo',
            'b': 'Governador',
            'c': 'Princípe',
            'd': 'Lutador',
        },
        'alternativa_certa': 'c'
    },
}
for titulo, pergunta in perguntas.items():
    print(titulo)
    for chave, valor in pergunta.items():
        if chave == 'pergunta':
            print(valor)
        if chave == 'alternativas':
            for i, j in valor.items():
                print(f'\t{i}) {j}')
            n = input('\nDigite a alternativa certa: ')
        if chave == 'alternativa_certa':
            r = valor

            if n == r:
                print('Parabéns, você acertou!!')
                sleep(2.0)

            else:
                print('Você errou')
                sleep(2.0)
