from Node import Node
from Arvore import BST
import tkinter as tk
from tkinter import ttk, messagebox
from io import StringIO
from contextlib import redirect_stdout
from tkinter import filedialog
import re


class InterfaceBST:

    def __init__(self, root, tree):
        self.root = root
        self.tree = tree

        self.root.title("Visualizador de Árvore Binária de Busca")
        self.root.geometry("1050x750")
        self.root.configure(bg="#20252b")

        self.criar_interface()
        self.atualizar_interface()

    def criar_interface(self):

        titulo = tk.Label(
            self.root,
            text="Árvore Binária de Busca (BST)",
            font=("Arial", 20, "bold"),
            bg="#20252b",
            fg="white"
        )
        titulo.pack(pady=15)

        # Área de inserção
        frame_insercao = tk.Frame(self.root, bg="#20252b")
        frame_insercao.pack(pady=10)


        tk.Label(
            frame_insercao,
            text="Novo elemento:",
            font=("Arial", 12),
            bg="#20252b",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)

        self.entrada = tk.Entry(frame_insercao, font=("Arial", 12), width=12)
        self.entrada.pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_insercao,
            text="Inserir",
            command=self.inserir,
            bg="#2878c8",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_insercao,
            text="Selecionar arquivo",
            command=self.inserirArquivo,
            bg="#2878c8",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(side=tk.LEFT, padx=5)

        frame_busca = tk.Frame(self.root, bg="#20252b")
        frame_busca.pack(pady=5)

        tk.Label(
            frame_busca,
            text="Consultar Chave: ",
            font=("Arial", 12),
            bg="#20252b",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)

        self.entrada_busca = tk.Entry(frame_busca, font=("Arial", 12), width=12)
        self.entrada_busca.pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_busca,
            text="Consultar",
            command=self.buscar,
            bg="#2878c8",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(side=tk.LEFT, padx=5)

        # Área principal
        frame_principal = tk.Frame(self.root, bg="#20252b")
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Informações
        frame_info = tk.LabelFrame(
            frame_principal,
            text="Informações da BST",
            font=("Arial", 12, "bold"),
            bg="#303943",
            fg="white",
            padx=10,
            pady=10
        )
        frame_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.informacoes = tk.Text(
            frame_info,
            font=("Consolas", 11),
            bg="#20252b",
            fg="#eeeeee",
            wrap=tk.WORD,
            width=43
        )
        self.informacoes.pack(fill=tk.BOTH, expand=True)

        # Desenho da árvore
        frame_arvore = tk.LabelFrame(
            frame_principal,
            text="Representação da árvore",
            font=("Arial", 12, "bold"),
            bg="#303943",
            fg="white"
        )
        frame_arvore.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.canvas = tk.Canvas(
            frame_arvore,
            bg="#20252b",
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        tk.Button(
            self.root,
            text="Atualizar informações",
            command=self.atualizar_interface,
            bg="#2878c8",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(pady=10)
        tk.Button(
            self.root,
            text="Limpar Árvore",
            command=self.limparArvore,
            bg="#2878c8",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(pady=5)

    def limparArvore(self):
        self.tree.limparArvore()
        self.atualizar_interface()

    def inserir(self):

        valor = self.entrada.get()

        try:
            valor = int(valor)

            self.tree.insert(self.tree.root, valor)

            self.entrada.delete(0, tk.END)
            self.atualizar_interface()

        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro.")

    def inserirArquivo(self):
        arquivo = filedialog.askopenfilename(
            title= "Selecione um arquivo que possua uma sequência de dígitos",
            filetypes=[("Arquivos de Texto", "*.txt")]
        )
        if arquivo:
            with open(arquivo, "r", encoding="UTF-8") as arquivo_numeros:
                numeros = arquivo_numeros.read()
                possui_letra = any(char.isalpha() for char in numeros)
                if possui_letra:
                    messagebox.showerror("Caractere indesejado", "O arquivo deve conter somente números")
                    return
                array_numeros = [x for x in re.split(r'[.,;:!?+\s/+-]', numeros)]
                for num in array_numeros:
                    if num != '':
                        self.tree.insert(self.tree.root, int(num))
        self.atualizar_interface()

    def buscar(self):
        valor = self.entrada_busca.get()

        try:
            valor = int(valor)
            presente = self.tree.consultaChave(self.tree.root, valor)
            if presente:
                messagebox.showinfo("Encontrado", f"O elemento {valor} está presente na BST, profundidade: {self.tree.depht(valor)}")
                return
            messagebox.showinfo("Não encontrado", f"O elemento {valor} não está presente na BST")
        except ValueError:
            messagebox.showerror("ERRO", "Digite um número inteiro")


    def capturar_travessia(self, metodo):

        saida = StringIO()

        with redirect_stdout(saida):
            metodo(self.tree.root)

        return saida.getvalue().strip()

    def atualizar_interface(self):


        # Captura as travessias
        em_ordem = self.capturar_travessia(self.tree.EmOrder)
        pos_ordem = self.capturar_travessia(self.tree.posOrder)
        pre_ordem = self.capturar_travessia(self.tree.preOrder)
        level_ordem = self.capturar_travessia(self.tree.levelOrder)

        # Informações gerais
        altura = self.tree.height(self.tree.root)
        tamanho = self.tree.size(self.tree.root)

        maior = self.tree.buscaMaiorElement(self.tree.root)

        menor = self.tree.buscaMenorElement(self.tree.root)
        if self.tree.root is None:
            maior = "Árvore vazia"
            menor = "Árvore vazia"

        comprimento = self.tree.buscaComprimentoInterno(self.tree.root)
        balanceamento = self.tree.verificaArvoreBalanceada(self.tree.root)
        if self.tree.root is not None:
            informacoes = f"""

TRAVESSIAS
--------------------------------------------

Em-ordem:
{em_ordem}

Pré-ordem:
{pre_ordem}

Pós-ordem:
{pos_ordem}

Level-ordem:
{level_ordem}


ESTATÍSTICAS
--------------------------------------------

Altura: {altura}
Tamanho: {tamanho}
Maior elemento: {maior}
Menor elemento: {menor}
Comprimento interno: {comprimento}
Balanceada?: {balanceamento}
"""
        else:
            informacoes = ""


        self.informacoes.delete("1.0", tk.END)
        self.informacoes.insert(tk.END, informacoes)

        self.desenhar_arvore()

    def desenhar_arvore(self):

        self.canvas.delete("all")

        largura = self.canvas.winfo_width()

        if largura < 50:
            largura = 500

        def desenhar(no, x, y, distancia):

            if no is None:
                return

            raio = 20

            # Desenha as conexões primeiro
            if no.left is not None:
                self.canvas.create_line(
                    x, y,
                    x - distancia, y + 75,
                    fill="white",
                    width=2
                )

                desenhar(
                    no.left,
                    x - distancia,
                    y + 75,
                    distancia / 2
                )

            if no.right is not None:
                self.canvas.create_line(
                    x, y,
                    x + distancia, y + 75,
                    fill="white",
                    width=2
                )

                desenhar(
                    no.right,
                    x + distancia,
                    y + 75,
                    distancia / 2
                )

            # Desenha o nó
            self.canvas.create_oval(
                x - raio, y - raio,
                x + raio, y + raio,
                fill="#2878c8",
                outline="white",
                width=2
            )

            self.canvas.create_text(
                x, y,
                text=str(no.item),
                fill="white",
                font=("Arial", 11, "bold")
            )

        desenhar(self.tree.root, largura // 2, 50, largura // 4)


def main():

    tree = BST()
    root = tk.Tk()
    InterfaceBST(root, tree)

    root.mainloop()


if __name__ == "__main__":
    main()

