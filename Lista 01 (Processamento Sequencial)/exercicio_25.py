'''Considerando uma eleição de apenas 02 candidatos, elabore um algoritmo que, a partir da leitura do
número total de eleitores, do número de votos do primeiro candidato e do número de votos do segundo
candidato, apresente. Em seguida, o algoritmo deverá apresentar o percentual de votos de cada um dos
candidatos e o percentual de votos nulos'''
votos_candidato_01 = int(input("Insira a quantidade de votos do candidato 01:"))
votos_candidato_02 = int(input("Insira a quantidade de votos do candidato 02:"))
votos_totais =  int(input("Insira a quantidade de votos total:"))
porcentagem_01 = (votos_candidato_01 / votos_totais) * 100
porcentagem_02 = (votos_candidato_02 / votos_totais) * 100
porcentagem_nula = 100 - (porcentagem_01 + porcentagem_02)
print(f"A porcentagem de votos do candidato 01 é: {porcentagem_01:.1f}%\nA porcentagem de votos do candidato 02 é: {porcentagem_02:.1f}%\nA porcentagem de votos nulos é: {porcentagem_nula:.1f}%")