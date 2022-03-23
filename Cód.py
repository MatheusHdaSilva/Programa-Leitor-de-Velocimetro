vel = float(input('Qual é a velocidade atual do carro?'))
if vel >= 80:
    print('Multado! voçê 4excedeu o limite que é de 80km/h')
multa = (vel - 80) * 7
print('você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um Bom Dia! Diríja com segurança')