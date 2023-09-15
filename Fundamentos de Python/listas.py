lista_nome = ['Teste', 'Daniel', 'Teste2']
lista_num = [1, 6, 2, 0, 6, 44, 323.12, 345.11, 2.029387, 234, 12, 2, 2, 634]
print(lista_nome)

# Procurando elementos na lista
# procurado = 'Teste'
# procurado2 = 'Daniel'
# if procurado or procurado2 in lista_nome:
#    print(f'Achei {procurado} ou {procurado2} na lista!')

# Possível ordenar uma lista através do método sort()
# O mesmo serve para strings e números
lista_nome.sort()
lista_num.sort()
print(lista_nome,'\n',lista_num)

# Usando o método count() é possível contar elementos em listas
# print(lista_nome.count('Daniel'))
# print(lista_num.count(2))

# Usando o método append() é possível adicionar elementos em listas
# OBS: só é possível adicionar um por vez
# lista_nome.append('Laryssa') # Adicionando elementos únicos
lista_nome.append(['Igor', 'Cris']) # Adicionando lista dentro da lista
lista_nome.extend(['Surama', 'David']) # Adicionando diferentes elementos separados dentro da lista

# Identifica listas dentro de listas
# if 'Daniel' and 'Teste' in lista_nome and 2 and 1 in lista_num:
#     print('Entrou no IF') 
# else:
#     print('Não entrou no IF')

# Iserindo elemento na lista informando a posição do índice
# OBS: Isso NÃO substitui o índice já existente, ele apenas é empurrado para a direta -> na memória
lista_nome.insert(2, 'Alisson')

# Juntando duas listas
lista_geral = []
# lista_geral = lista_nome + lista_num
# lista_gerak.extedn(lista_nome)
# lista_geral.extend([lista_nome, lista_num])

print(lista_nome,'\n', lista_geral)
