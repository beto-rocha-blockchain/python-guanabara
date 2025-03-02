import tkinter as tk
import time
import threading

# Função para a contagem regressiva
def contagem_regressiva():
    for i in range(10, -1, -1):
        label_contagem.config(text=str(i))  # Atualiza o texto do rótulo
        time.sleep(1)  # Espera 1 segundo
    label_contagem.config(text="Feliz Ano Novo! 🎉🥳")  # Mensagem final

# Função para iniciar a contagem regressiva em uma thread separada
def iniciar_contagem():
    # Inicia a contagem regressiva em uma thread separada para não travar a interface
    threading.Thread(target=contagem_regressiva, daemon=True).start()

# Criação da janela principal
root = tk.Tk()
root.title("Contagem Regressiva para o Ano Novo")

# Configura o tamanho da janela
root.geometry("300x200")

# Rótulo para mostrar a contagem regressiva
label_contagem = tk.Label(root, text="10", font=("Arial", 48), fg="red")
label_contagem.pack(pady=50)

# Botão para iniciar a contagem regressiva
botao_iniciar = tk.Button(root, text="Iniciar Contagem", font=("Arial", 14), command=iniciar_contagem)
botao_iniciar.pack()

# Inicia a interface gráfica
root.mainloop()