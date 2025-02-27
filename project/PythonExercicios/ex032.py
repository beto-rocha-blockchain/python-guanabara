import tkinter as tk
from tkinter import messagebox
from datetime import date

# Função para verificar se um ano é bissexto
def verificar_bissexto():
    try:
        ano = entrada_ano.get()
        if not ano:  # Se o usuário não inserir nada, usa o ano atual
            ano = date.today().year
        else:
            ano = int(ano)

        # Regras do ano bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            resultado = f"O ano {ano} é BISSEXTO."
        else:
            resultado = f"O ano {ano} NÃO é bissexto."

        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um ano válido.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Verificador de Ano Bissexto")
janela.geometry("350x200")
janela.resizable(False, False)
janela.configure(bg="#f0f0f0")

# Rótulo de instrução
label = tk.Label(janela, text="Digite um ano (ou deixe em branco para usar o atual):", font=("Arial", 11), bg="#f0f0f0")
label.pack(pady=10)

# Campo de entrada
entrada_ano = tk.Entry(janela, font=("Arial", 12), justify="center")
entrada_ano.pack(pady=5)

# Botão de verificação
botao_verificar = tk.Button(janela, text="Verificar", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                            padx=10, pady=5, command=verificar_bissexto)
botao_verificar.pack(pady=15)

# Rodando a interface
janela.mainloop()
