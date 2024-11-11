import tkinter as tk
from tkinter import messagebox



def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura_cm = float(entry_altura.get())
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)


        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade Grau I"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III ou Mórbida"


        resultado_texto = f"IMC: {imc:.2f}\nClassificação: {classificacao}"
        resultado_label.config(text=resultado_texto)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura.")



def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_label.config(text="")



def sair():
    janela.quit()



janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("400x400")


tk.Label(janela, text="Nome do Paciente:").pack(pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()


tk.Label(janela, text="Endereço Completo:").pack(pady=5)
entry_endereco = tk.Entry(janela, width=40)
entry_endereco.pack()


tk.Label(janela, text="Altura (cm):").pack(pady=5)
entry_altura = tk.Entry(janela, width=20)
entry_altura.pack()


tk.Label(janela, text="Peso (kg):").pack(pady=5)
entry_peso = tk.Entry(janela, width=20)
entry_peso.pack()


btn_calcular = tk.Button(janela, text="Calcular", command=calcular_imc)
btn_calcular.pack(pady=10)


btn_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar)
btn_reiniciar.pack(pady=5)


btn_sair = tk.Button(janela, text="Sair", command=sair)
btn_sair.pack(pady=5)


resultado_label = tk.Label(janela, text="", font=("Arial", 10), fg="blue")
resultado_label.pack(pady=15)


janela.mainloop()
