frutas = ['maçã','banana','laranja','uva','morango']
print(frutas)
print(frutas[3])

frutas.append('melancia') #adiciona um item sempre no final
print(frutas)

frutas.insert(2,'manga') #insere um item no lugar que eu decidir
print(frutas)

frutas.remove('banana') #remove um item pelo nome 
print(frutas)

frutas.pop() #remove o ultimo item da lista 
print(frutas)

frutas.pop(1) #remove o item do lugar que eu decidir
print(frutas)

for fruta in frutas:
    print(fruta)
frutas[0] = 'caqui'

aluno = {"nome":"Pedro", "idade":18, "RA":20241010}
print(aluno['nome'])
aluno['idade'] = 19
print(aluno['idade'])
aluno['curso'] = 'Engenharia de Software'
print(aluno)
aluno['notas'] = [9.5,10,5,7]
print(aluno)
del aluno['notas'] #deletar 
aluno['medias'] = [9.5,10,5,7]
print(aluno)
aluno['medias'][1] = 2
print (aluno)
print(aluno.keys())

for elem in aluno.keys():
    print(aluno[elem])


lista_musicas = [
        {"nome":"Musica1", "Artista": "Artista1", "Genero": "Genero1"},
        {"nome":"Show das poderosas", "Artista": "Anitta", "Genero": "Funk"},
        {"nome":"Empreguetes", "Artista": "3 marias", "Genero": "POP"},
]

for elem in lista_musicas:
    print(elem["nome"])
    print(elem["Artista"])
    print(elem["Genero"])
    print('-------------------------------------')