import tkinter as tk

def calcular():
    try:
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        operacion = combo_operacion.get()
        
        if operacion == "Sumar":
            resultado = valor1 + valor2
        elif operacion == "Restar":
            resultado = valor1 - valor2
        elif operacion == "Multiplicar":
            resultado = valor1 * valor2
        elif operacion == "Dividir":
            resultado = valor1 / valor2
            
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Error: Ingresa números válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Entradas
entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=0, padx=5, pady=5)
entry2 = tk.Entry(ventana)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Combo box para la operación
opciones_operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]
combo_operacion = tk.StringVar()
combo_operacion.set(opciones_operaciones[0]) # Por defecto, suma
combobox = tk.OptionMenu(ventana, combo_operacion, *opciones_operaciones)
combobox.grid(row=0, column=2, padx=5, pady=5)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Ejecutar ventana
ventana.mainloop()
