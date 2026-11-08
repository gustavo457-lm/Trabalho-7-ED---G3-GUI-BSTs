from Node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x, item):
        if self.root is None:
            self.root = Node(item)
        if x is None:
            return Node(item)
        elif item>x.item:
            x.right=self.insert(x.right, item)
        elif item<x.item:
            x.left=self.insert(x.left, item)

        return x

    def insertIndividual(self, valor_texto):
        try:
            valor = int(valor_texto)
            
            self.root = self.insert(self.root, valor)
            print(f"Elemento {valor} inserido individualmente com sucesso.")
            
        except ValueError:
            print(f"Erro: O valor '{valor_texto}' do campo de texto não é um número válido.")

    def insertLote(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                valores = conteudo.split()

                for val in valores:
                    self.insertIndividual(val)
                    
            print(f"--- Fim da inserção em lote do arquivo '{nome_arquivo}' ---")
            
        except FileNotFoundError:
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

    def size(self, x):
        if x is None:
            return 0
        else:
           return 1 + self.size(x.left)+self.size(x.right)
        
    def height(self, x):
        if x is None:
            return 0
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

    def levelOrder(self, node, nivelAtual=0):
        if node is None:
            return node

        profundidadeNo = self.depht(node.item)

        if profundidadeNo == nivelAtual:
            print(f"{node.item} ", end='')

        elif profundidadeNo < nivelAtual:
            self.levelOrder(node.left, nivelAtual)
            self.levelOrder(node.right, nivelAtual)

        if profundidadeNo == 0 and nivelAtual < self.height(node):
            self.levelOrder(node, nivelAtual + 1)
            
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
        if x.right is None:
            return x.item

        return self.buscaMaiorElement(x.right)
    
    def buscaMenorElement(self, x):
        if x is None:
            return -99999
        if x.left is None:
            return x.item

        return self.buscaMenorElement(x.left)

    def consultaChave(self, node, valor):
        if node is None:
            print(f"{valor} não foi encontrado na árvore")
            return False

        if valor == node.item:
            print(f"{valor} foi encontrado na árvore")
            return True
        
        elif valor < node.item:
            return self.consultaChave(node.left, valor) 

        elif valor > node.item:
            return self.consultaChave(node.right, valor) 

    def limparArvore(self):
        self.root = None

    def buscaComprimentoInterno(self, node):
        if node is None:
            return 0
        return self.depht(node.item) + self.buscaComprimentoInterno(node.left) + self.buscaComprimentoInterno(node.right)
    
    def verificaArvoreBalanceada(self, node):
        if self.root is None:
            return False
        hLeft = self.height(node.left) + 1
        hRight = self.height(node.right) + 1
        if (hLeft - hRight) > 1 or (hRight - hLeft) > 1:
            print("Arvore não Balanceada")
            return False
        else:
            print("Arvore Balanceada")
            return True


