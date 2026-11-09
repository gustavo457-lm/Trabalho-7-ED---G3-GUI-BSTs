import tkinter as tk
from Arvore import BST
from GUI import InterfaceBST

def main():

    tree = BST()
    root = tk.Tk()
    InterfaceBST(root, tree)

    root.mainloop()


if __name__ == "__main__":
    main()