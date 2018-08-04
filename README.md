# MatematicaDiscreta-ProjetoAula2

1) Adicionar elemento:
Adiciona um elemento a um conjunto.

Implementação:

def adicionar(l,e):
    l.append(e)
    print(l)
    return l

Nessa função recebe-se de parâmetro o conjunto no qual o elemento será adicionado (l) e o elemento a ser adicionado (e), inserindo-o no conjunto de elemento.

2) Remover elemento:
Remove  um elemento de um conjunto.

Implementação:
def remover(l,e):
    l.remove(e)
    print(l)
    return l

Nessa função recebe-se de parâmetro o conjunto no qual o elemento será removido (l) e o elemento a ser removido  (e), inserindo-o no conjunto de elemento.


3) Verificar pertinência:
Se um elemento a pertence ao conjunto A isso é representado como: a ∈ A. Caso contrário, se a não pertence a A, então representa-se como: a ∉ A.
Exemplo:
B = {a,c,d,e}, então c ∈ B, onde é um elemento.

Implementação:
def pertinencia(l, e):
    if e in l:
        return print("Pertence")
    else:
        return print("Não Pertence")


4) Verificar continência:
Se todos os elementos de um conjunto A também são elementos de um conjunto B, então A está contido em B, o que é representado por: A ⊆  B. Isso também é lido como A é subconjunto de B.
Exemplo: 
{a, b} ⊆ {b, a}

Implementação:
def continencia(l1, l2):
    for a in l1:
        if a not in l2:
            return print("Não contém")
             
    print("Contém")
    
Onde o conjunto 1 (l1) é o conjunto de elementos a ser verificada a continência co conjunto 2 (l2).Se algum elemento de l1 não existir no conjunto l2 retorna ‘Não contém’.


5) Realizar união (com outro conjunto) :
Sejam 𝐴 e 𝐵 dois conjuntos. A união entre eles, 𝐴 ∪ 𝐵, é definida como:
𝐴 ∪ 𝐵 = {𝑥 ∣ 𝑥 ∈ 𝐴 ∨ 𝑥 ∈ 𝐵} 
Exemplo:
Letras = {a,b,c,d}
Numeros = {2,10,12}
Letras ∪ Numeros = {a,b,c,d,2,10,12}

Implementação:
def uniao(l1, l2):
    l3 = []
    for a in l1:
        l3.append(a)
    for e in l2:
        if e not in l3:
            l3.append(e)
    return print(l3)

Onde o conjunto 1 (l1) e o conjunto de elementos 2 (l2 ) serão concatenado em um novo array (l3).



6) Realizar interseção (com outro conjunto):
Intersecção é o resultado dos elementos em comum entre dois conjuntos.
Exemplo:
Dígitos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} b) 
Vogais = {𝑎, 𝑒, 𝑖, 𝑜, 𝑢} c) 
Pares = {0, 2, 4, 6, ...} 
Então: 
Dígitos ∩ Vogais = ∅ 
Dígitos ∩ Pares = {0, 2, 4, 6, 8}

Implementação:
def intersecao(lista1, lista2):
    lista3 = []
    for n in lista1:
        if n in lista2:
            lista3.append(n)
    return lista3


Onde o conjunto 1 (l1) é o conjunto de elementos a ser verificada a intercessão com conjunto 2 (l2) e retornar os elementos em comum.

7) Realizar diferença (com outro conjunto) :
Sejam os conjuntos 𝐴 e 𝐵. A diferença dos conjuntos 𝐴 e 𝐵, denotada por 𝐴 − 𝐵 é definida como: 
𝐴 − 𝐵 = 𝐴∩ ∼ 𝐵
Exemplo:
Digitos = {0, 1, 2, ..., 9}
Vogais = {𝑎, 𝑒, 𝑖, 𝑜, 𝑢} 
Pares = {0, 2, 4, 6, ...}. 
Então:
Digitos − Vogais = Dígitos 
Digitos − Pares = {1, 3, 5, 7, 9}

Implementação:
def diferenca(lista1, lista2):
    lista3 = []
    for n in lista1:
        if n not in lista2:
            lista3.append(n)
    return lista3

Onde o conjunto 1 (lista1) é o conjunto de elementos a ser verificada a diferença com conjunto 2 (lista2) e retornar os elementos que não pertencem ao conjunto lista2.


8) Realizar complemento (em relação a outro conjunto):
Considere o conjunto universo 𝑈. O complemento de um conjunto 𝐴 ⊆ 𝑈.
Exemplos:
Considere o conjunto universo definido por Digitos = {0, 1, 2, ..., 9}. Seja 𝐴 = {0, 1, 2}.
Então, ∼ 𝐴 = {3, 4, 5, 6, 7, 8, 9}

Implementação:
def complementar(l1, l2):
    C = []
    for a in l1:
        if a not in l2:
            C.append(a)
    return print(C)

Onde o conjunto 1 (lista1) é o conjunto de elementos a ser comparado com o conjunto Universo(l2) e adicionar os elementos distintos na lista C.

9) Gerar o conjunto das partes:
Para qualquer conjunto 𝐴 sabe-se que: 
• 𝐴 ⊆ 𝐴 
• ∅ ⊆ 𝐴 
• Para qualquer elemento 𝑎 ∈ 𝐴, é visível que {𝑎} ⊆ 𝐴 
A operação unária chamada conjunto das partes, ao ser aplicada ao conjunto 𝐴, resulta no conjunto de todos os subconjuntos de 𝐴. Suponha um conjunto 𝐴. O conjunto das partes de 𝐴 (ou conjunto potência), denotado por P(𝐴) ou 2 𝐴, é definido por: P(𝐴) = {𝑋 ∣ 𝑋 ⊆ 𝐴}




10) Realizar o produto cartesiano (com outro conjunto):
A operação produto cartesiano é uma operação binária que, quando aplicada a dois conjuntos 𝐴 e 𝐵, resulta em um conjunto constituído de sequências de duas componentes (tuplas), sendo que o primeiro componente de cada sequência é um elemento de 𝐴, e a segunda componente, um elemento de 𝐵.
Exemplo:
Sejam os conjuntos 
A = {𝑎}, 𝐵 = {𝑎, 𝑏} e 𝐶 = {0, 1, 2}
Então:
𝐴 × 𝐵 = {⟨𝑎, 𝑎⟩, ⟨𝑎, 𝑏⟩} 
𝐵 × 𝐶 = {⟨𝑎, 0⟩, ⟨𝑎, 1⟩, ⟨𝑎, 2⟩, ⟨𝑏, 0⟩, ⟨𝑏, 1⟩, ⟨𝑏, 2⟩} 
𝐴2 = {⟨𝑎, 𝑎⟩} 

Implementação:
def pCartesiano(a,b):
    for x in a:
        for y in b:
            print('(a:{0} b:{1})'.format(x,y))

As duas listas foram percorridas e em seguida os valores foram passados com seus respectivos conjuntos usando o format.


11) Realizar a união disjunta (com outro conjunto):
Diferentemente da união, que desconsidera repetições de elementos no conjunto resultante, a união disjunta permite que os elementos do conjunto resultante sejam duplicados, uma vez que seja identificada a sua fonte.



Componentes: João Vitor Moreno, Arthur Gabriel, Renan Bringel, Ismael Pontes , Lucas Anselmo








