distancia = float(input("Informe a distância entre os pontos em km:"))
velocidade_kmh = float(input("Informe a velocidade do objeto em km/h:"))
tempo = distancia / velocidade_kmh
velocidade_ms = velocidade_kmh / 3.6
print(f"O tempo médio é de {tempo:.2f}h e a velocidade em m/s é de {velocidade_ms:.2f}m/s")