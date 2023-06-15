import tkinter as tk
from tkinter import messagebox



def opcion_realizar_consulta():
    consulta = messagebox.askquestion("Realizar una consulta", "¿Deseas hacer una consulta?")
    if consulta == 'yes':
        messagebox.showinfo("Consulta", "Procesando tu consulta...")
        # Lógica para procesar la consulta con tu IA


def opcion_inicio():
    import BoB 


def opcion_salir():
    ventana.quit()


ventana = tk.Tk()
ventana.title("Menú de la IA")


boton_inicio = tk.Button(ventana, text="inicio", command=opcion_inicio)
boton_inicio.pack()

boton_consulta = tk.Button(ventana, text="Realizar una consulta", command=opcion_realizar_consulta)
boton_consulta.pack()


boton_salir = tk.Button(ventana, text="salir", command=opcion_salir)
boton_salir.pack()



ventana.mainloop()
