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
    print(f'{titulo}: {pergunta["pergunta"]}')
    for i, j in pergunta["alternativas"].items():
        print(f'\t{i}) {j}')
    resposta_usuario = input('Escolha uma alternativa: ')

    if resposta_usuario == pergunta['alternativa_certa']:
        print(f'Parabéns, você acertou!!!\n\nVamos para a próxima pergunta')
        sleep(2.0)
    else:
        print(f'Que pena, você errou!!! \nVamos para a próxima pergunta')
        sleep(2.0)