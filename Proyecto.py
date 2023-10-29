import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import getpass  # Para obtener el nombre del usuario actual

def calculate_equilibrium():
    fixed_costs = float(fixed_costs_entry.get())
    variable_costs = float(variable_costs_entry.get())
    selling_price = float(selling_price_entry.get())

    equilibrium_quantity = fixed_costs / (selling_price - variable_costs)

    equilibrium_label.config(text=f"Cantidad de Equilibrio: {equilibrium_quantity:.2f} unidades")

    # Crear un gráfico de punto de equilibrio
    plt.clf()
    q = range(0, int(equilibrium_quantity) + 1)
    revenue = [q_i * selling_price for q_i in q]
    costs = [fixed_costs + q_i * variable_costs for q_i in q]

    plt.plot(q, revenue, label='Ingresos')
    plt.plot(q, costs, label='Costos')
    plt.axvline(x=equilibrium_quantity, color='r', linestyle='--', label='Cantidad de Equilibrio')
    plt.xlabel('Cantidad (unidades)')
    plt.ylabel('Quetzales Guatemaltecos (GTQ)')
    plt.legend()

    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Punto de Equilibrio")

# Configurar el color de fondo
root.configure(bg='#EAEAEA')  # Gris claro

# Crear y configurar el marco de entrada
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

fixed_costs_label = ttk.Label(input_frame, text="Costos Fijos (GTQ):")
fixed_costs_label.grid(row=0, column=0)

fixed_costs_entry = ttk.Entry(input_frame)
fixed_costs_entry.grid(row=0, column=1)

variable_costs_label = ttk.Label(input_frame, text="Costos Variables (GTQ):")
variable_costs_label.grid(row=1, column=0)

variable_costs_entry = ttk.Entry(input_frame)
variable_costs_entry.grid(row=1, column=1)

selling_price_label = ttk.Label(input_frame, text="Precio de Venta (GTQ):")
selling_price_label.grid(row=2, column=0)

selling_price_entry = ttk.Entry(input_frame)
selling_price_entry.grid(row=2, column=1)

calculate_button = ttk.Button(input_frame, text="Calcular", command=calculate_equilibrium)
calculate_button.grid(row=3, column=0, columnspan=2)

# Crear y configurar el marco de salida
output_frame = ttk.Frame(root)
output_frame.grid(row=0, column=1, padx=10, pady=10)

# Obtener el nombre de usuario actual
username = getpass.getuser()
welcome_label = ttk.Label(output_frame, text=f"Bienvenido {username}!")
welcome_label.grid(row=0, column=0)

equilibrium_label = ttk.Label(output_frame, text="")
equilibrium_label.grid(row=1, column=0)

# Crear el gráfico Matplotlib
figure, ax = plt.subplots()
canvas = FigureCanvasTkAgg(figure, master=output_frame)
canvas.get_tk_widget().grid(row=2, column=0)

root.mainloop()

