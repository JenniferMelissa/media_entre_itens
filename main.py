numeros = [10,5,7,4,6,3,8]

#classifica em ordem decrescente
numeros.sort(reverse=True)

for numero in numeros:
    print(numero,end=' ')

media = sum(numeros) / len(numeros) 
print(f'\nResutado da média: {media:,.2f}')


#codigo pra definir o nro de casas decimais, apos os 2 pontos voce escolhe a qtd de casas decimais



