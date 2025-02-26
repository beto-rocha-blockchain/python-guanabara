import tkinter as tk
from tkinter import messagebox

def calculate_side():
    try:
        side1 = float(entry_side1.get())
        side2 = float(entry_side2.get())
        missing_side = var.get()

        if missing_side == "Hipotenusa":
            result = (side1**2 + side2**2) ** 0.5
        else:  # Calcula o cateto
            result = abs((side1**2 - side2**2) ** 0.5)

        messagebox.showinfo("Resultado", f"O lado calculado é: {result:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da interface gráfica
app = tk.Tk()
app.title("Calculadora de Triângulo Retângulo")

tk.Label(app, text="Insira os dois lados conhecidos:").pack()

entry_side1 = tk.Entry(app)
entry_side1.pack()

entry_side2 = tk.Entry(app)
entry_side2.pack()

var = tk.StringVar(value="Hipotenusa")
tk.Radiobutton(app, text="Calcular Hipotenusa", variable=var, value="Hipotenusa").pack()
tk.Radiobutton(app, text="Calcular Cateto", variable=var, value="Cateto").pack()

calculate_button = tk.Button(app, text="Calcular", command=calculate_side)
calculate_button.pack()

app.mainloop()