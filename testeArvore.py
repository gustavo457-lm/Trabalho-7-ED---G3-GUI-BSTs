from Arvore import BST
from Node import Node

def separaTexto():
    print("-"*50)

def main():
    tree = BST()
    tree.insert(tree.root, 5)
    tree.insert(tree.root, 12)
    tree.insert(tree.root, 3)
    tree.insert(tree.root, 7)
    tree.insert(tree.root, 11)
    tree.insert(tree.root, 15)
    tree.insert(tree.root, 16)


    tree.insertLote("dados .txt")

    entrada_usuario = "25" 
    tree.insertIndividual(entrada_usuario)

    entrada_usuario2 = "5"
    tree.insertIndividual(entrada_usuario2)

    separaTexto()
    print("Travessia em-ordem: ")
    tree.EmOrder(tree.root)
    print()
    separaTexto()
    print("Travessia pós-ordem: ")
    tree.posOrder(tree.root)
    print()
    separaTexto()
    print("Travessia pré-ordem: ")
    tree.preOrder(tree.root)
    print()
    separaTexto()
    print(f"Altura da árvore: {tree.height(tree.root)}")
    separaTexto()
    print(f"Tamanho da árvore: {tree.size(tree.root)}")
    separaTexto()
    print(f"Maior elemento da árvore: {tree.buscaMaiorElement(tree.root)}")
    separaTexto()
    print(f"Menor elemento da árvore: {tree.buscaMenorElement(tree.root)}")
    separaTexto()
    print(f"Comprimento Interno: {tree.buscaComprimentoInterno(tree.root)}")

    tree.verificaArvoreBalanceada(tree.root)
    #tree.limparArvore() metodo que limpa a arvore, (modificar os valores vazios)

main()
