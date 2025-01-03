def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            print("Acertou!")
            return meio
        if chute > item:
            print(f"Chute: {chute}")
            alto = meio - 1
        else:
            print(f"Chute: {chute}")
            baixo = meio + 1

    return None


minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
