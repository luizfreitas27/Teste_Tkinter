import tkinter as tk
from tkinter import messagebox

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_email = tk.Label(root, text="E-mail:")
        self.label_email.pack()

        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.button_cadastrar.pack()

        self.label_usuarios_cadastrados = tk.Label(root, text="Usuários Cadastrados:")
        self.label_usuarios_cadastrados.pack()

        self.text_usuarios_cadastrados = tk.Text(root)
        self.text_usuarios_cadastrados.pack()

        self.usuarios = []

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()

        if nome and email:
            self.usuarios.append((nome, email))
            self.atualizar_texto_usuarios()
            self.limpar_campos()
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        else:
            messagebox.showwarning("Cadastro", "Preencha todos os campos.")

    def atualizar_texto_usuarios(self):
        self.text_usuarios_cadastrados.delete(1.0, tk.END)
        for usuario in self.usuarios:
            self.text_usuarios_cadastrados.insert(tk.END, f"Nome: {usuario[0]}\nE-mail: {usuario[1]}\n\n")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
