from Arvore import BST
from Node import Node


def separaTexto():
    print("-"*50)

def main():
    tree = BST()
    tree.root=Node(10)
    tree.insert(tree.root, 5)
    tree.insert(tree.root, 12)
    tree.insert(tree.root, 3)
    tree.insert(tree.root, 7)
    tree.insert(tree.root, 11)
    tree.insert(tree.root, 15)
    tree.insert(tree.root, 16)

    '''
    # 1. Inserindo um lote inicial a partir de um arquivo txt
    #tree.insertLote("dados .txt")

    2. Usuário digita um valor em um campo de texto na interface
    entrada_usuario = "25" 
    tree.insertIndividual(entrada_usuario)

    # 3. Usuário digita outro valor
    entrada_usuario2 = "5"
    tree.insertIndividual(entrada_usuario2)'''

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
    print("Travessia em nível: ")
    tree.levelOrder(tree.root)
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
    separaTexto()
    tree.verificaArvoreBalanceada(tree.root)
    separaTexto()
    #tree.limparArvore() metodo que limpa a arvore, (modificar os valores vazios)

main()

