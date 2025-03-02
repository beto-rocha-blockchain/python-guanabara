import tkinter as tk
from tkinter import messagebox
import random

# Função que define a escolha da máquina (computador)
def computador_escolhe():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    return random.choice(opcoes)

# Função que verifica o vencedor
def verificar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (escolha_usuario == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_usuario == "Papel" and escolha_computador == "Pedra") or \
         (escolha_usuario == "Tesoura" and escolha_computador == "Papel"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

# Função chamada quando o usuário faz uma escolha
def escolher(escolha_usuario):
    escolha_computador = computador_escolhe()
    resultado = verificar_vencedor(escolha_usuario, escolha_computador)
    
    # Exibe o resultado em uma caixa de diálogo
    messagebox.showinfo("Resultado", f"Você escolheu: {escolha_usuario}\n"
                                    f"O computador escolheu: {escolha_computador}\n"
                                    f"{resultado}")

# Criação da interface gráfica
root = tk.Tk()
root.title("Jogo de Jokenpô")

# Label de título
label = tk.Label(root, text="Escolha sua opção", font=("Arial", 14))
label.pack(pady=10)

# Botões para escolher Pedra, Papel ou Tesoura
button_pedra = tk.Button(root, text="Pedra", width=15, height=2, command=lambda: escolher("Pedra"))
button_pedra.pack(pady=5)

button_papel = tk.Button(root, text="Papel", width=15, height=2, command=lambda: escolher("Papel"))
button_papel.pack(pady=5)

button_tesoura = tk.Button(root, text="Tesoura", width=15, height=2, command=lambda: escolher("Tesoura"))
button_tesoura.pack(pady=5)

# Inicia a interface gráfica
root.mainloop()