import itertools as it

def adicionar(l, e):
    l.append(e)
    # print(l)
    return l


def remover(l, e):
    l.remove(e)
    # print(l)
    return l


def pertinencia(l, e):
    if e in l:
        return True
    else:
        return False


def continencia(l1, l2):
    for a in l1:
        if a not in l2:
            return False

    return True


def uniao(l1, l2):
    l3 = []
    for a in l1:
        l3.append(a)
    for e in l2:
        if e not in l3:
            l3.append(e)
    return l3


def complementar(l1, l2):
    C = []
    for a in l1:
        if a not in l2:
            C.append(a)

    return C


def pCartesiano(a, b):
    for x in a:
        for y in b:
            print('(a:{0} b:{1})'.format(x, y))


def intersecao(lista1, lista2):
    lista3 = []
    for n in lista1:
        if n in lista2:
            lista3.append(n)
    return lista3


def diferenca(lista1, lista2):
    lista3 = []
    for n in lista1:
        if n not in lista2:
            lista3.append(n)
    return lista3


def permutations(iterable):
    print(list(it.permutations(iterable, 2)))
    return True

l1 = []
l2 = []

adicionar(l1, "a")
adicionar(l1, "b")
adicionar(l1, "c")
adicionar(l1, "d")

adicionar(l2, "a")
adicionar(l2, "v")
adicionar(l2, "c")

print( permutations(l1))