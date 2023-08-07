import tkinter as tk
from tkinter import messagebox

class UserRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")
        
        self.user_data = {}

        # Logo
        self.logo = tk.PhotoImage(file="logo.png")  # Substitua "logo.png" pelo caminho da imagem da logo
        self.logo_label = tk.Label(root, image=self.logo)
        self.logo_label.pack()

        # Nome
        self.name_label = tk.Label(root, text="Nome:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # Botão de Cadastro
        self.register_button = tk.Button(root, text="Cadastrar", command=self.register_user)
        self.register_button.pack()

    def register_user(self):
        name = self.name_entry.get()
        
        if name in self.user_data:
            messagebox.showerror("Erro", "Usuário já cadastrado!")
        else:
            self.user_data[name] = True
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserRegistrationApp(root)
    root.mainloop()