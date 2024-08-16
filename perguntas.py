import pandas as pd
# Lista de perguntas

perguntas = [
    ['Complete with the Simple Present:\n What time _________ the banks _________ in Italy ? (to close)',
    'does - close', 'do - close', 'is - close','generally - closes', 2 ],

    ['Choose the correct alternative:\n The Olympic Games __________________ every four years.',
    'happen', 'happens', 'happened', 'happening', 1],

    ['Complete corretamente a frase:\n The population of the world is ____________.', 'going', 'covering', 'finding', 'growing', 4],

    ['Complete corretamente a frase:\n The whole word ____________ against drugs now.', 'is fighting', 'fought', 'had been fighting', 'has fought', 1 ],

    ['Em inglês, “Você está esperando alguma carta?” seria:',
    'Have you been waiting for a chart?', 'Are you attending any lecture?', 'Are you expecting a letter?', 'Are you staying for the lecture?', 3],

    ['A tradução da frase "What are you doing?" é: ', 'O que você conseguiu fazer?', 'O que você fez?', 'O que você está fazendo?', 'O que você vai fazer?', 3],

    ['Complete as lacunas corretamente:\n __________ you __________ caviar, Helen?', 'Has ... ate', 'Have ... ate', 'Have ... eaten', 'Has ... eaten', 3],

    ['Marque a alternativa que preencha a lacuna corretamente:\n She __________ to Italy since 2010.', 'have travel', 'has travel', 'have traveled', 'has traveled', 4],

    ['Marque a alternativa que preencha as lacunas corretamente:\n He __________ never __________ a car before.', 'has - drive', 'has - driven', 'has not - driven', 'have - driven', 2],

    ['Marque a alternativa que preencha as lacunas corretamente:\n __________ you __________ the news today?', 'Have - hear', 'Have - heard', 'Have - to hear', 'Have - to heard', 2]


]

# Dataframe do pandas
df = pd.DataFrame(perguntas, columns=['Perguntas', 'Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', 'Resposta'])

# Salvando arquivo no excel 
df.to_excel('questoes.xlsx', index=False)

print('Questões inseridas com sucesso.')