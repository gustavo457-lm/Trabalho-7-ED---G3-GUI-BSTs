from Node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x, item):
        if x is None:
            return Node(item)
        elif item>x.item:
            x.right=self.insert(x.right, item)
        elif item<x.item:
            x.left=self.insert(x.left, item)

        return x

    def size(self, x):
        if x is None:
            return 0
        else:
           return 1 + self.size(x.left)+self.size(x.right)
        
    def height(self, x):
        if x is None:
            return -1
        else:
            return 1+max(self.height(x.left), self.height(x.right))

    def EmOrder(self, node):
        if node is None:
            return node
        self.EmOrder(node.left)
        print(f"{node.item} ", end='')
        self.EmOrder(node.right)

    def preOrder(self, node):
        if node is None:
            return node
        print(f"{node.item} ", end='')
        self.preOrder(node.left)
        self.preOrder(node.right)

    def posOrder(self, node):
        if node is None:
            return node
        self.posOrder(node.left)
        self.posOrder(node.right)
        print(f"{node.item} ", end='')

    #def levelOrder(self, node):
        #for i in range(self.size(node)):
    def depht(self, num):
        x = self.root
        depht = 0
        while x:
            if x.item == num:
                return depht
            
            depht += 1

            if num < x.item:
                x = x.left
            else:
                x = x.right 
        return -1

    def buscaMaiorElement(self, x):
        if x is None:
            return -99999
        maior = x.item
        maiorRight = self.buscaMaiorElement(x.right)
        maiorLeft = self.buscaMaiorElement(x.left)
        if maior < maiorRight and maiorLeft < maiorRight:
            maior = maiorRight
        elif maior < maiorLeft and maiorRight < maiorLeft:
            maior = maiorLeft
        return maior

    def buscaMenorElement(self, x):
        if x is None:
            return 99999
        menor = x.item
        menorRight = self.buscaMenorElement(x.right)
        menorLeft = self.buscaMenorElement(x.left)
        if menor > menorRight and menorLeft > menorRight:
            menor = menorRight
        elif menor > menorLeft and menorRight > menorLeft:
            menor = menorLeft
        return menor

    def consultaChave(self, node, valor):
        if node is None:
            print(f"{valor} não foi encontrado na árvore")
            return node

        if valor == node.item:
            print(f"{valor} foi encontrado na árvore")
        
        elif valor < node.item:
            self.consultaChave(node.left, valor) 

        elif valor > node.item:
            self.consultaChave(node.right, valor) 

    def limparArvore(self):
        self.root = None

    def buscaComprimentoInterno(self, node):
        if node is None:
            return 0
        return self.depht(node.item) + self.buscaComprimentoInterno(node.left) + self.buscaComprimentoInterno(node.right)
    
    def verificaArvoreBalanceada(self, node):
        hLeft = self.height(node.left) + 1
        hRight = self.height(node.right) + 1
        if (hLeft - hRight) > 1 or (hRight - hLeft) > 1:
            print("Arvore não Balanceada")
        else:
            print("Arvore Balanceada")


