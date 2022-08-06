import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
root = tk.Tk()
  
canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()

titulo = tk.Label(root, text='Calculadora de condición de aprobación\n Mate 2 - 2do semestre 2022')
titulo.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=titulo)

titulo1 = tk.Label(root, text='Nota 1er parcial')
titulo1.config(font=('Arial', 12))
canvas1.create_window(300, 100, window=titulo1)

titulo2 = tk.Label(root, text='Nota 2do parcial')
titulo2.config(font=('Arial', 12))
canvas1.create_window(300, 120, window=titulo2)
   
nota01 = tk.Entry (root)
canvas1.create_window(450, 100, window=nota01) 
  
nota02 = tk.Entry (root)
canvas1.create_window(450, 120, window=nota02) 
  
def Condicion():
    global nota01
    global nota02
    global condicion
    global promedio
    
    nota1 = float(nota01.get())
    nota2 = float(nota02.get())
    promedio = nota1*0.4 + nota2*0.6
    
    if promedio >= 60:
        if (nota1 >= 50) and (nota2 >= 50):
            condicion = 'Promociona'
        elif nota1 < 50:
            condicion = 'Recupera 1er parcial'
        else:
            condicion = 'Recupera 2do parcial'
    elif (promedio >= 40) or (nota1 >=50) or (nota2 >= 50):
        condicion = 'Final'
    else:
	    condicion = 'Recursa'
	
    res = tk.Label(root, text=condicion)
    res.config(font=('Arial', 12))
    canvas1.create_window(400, 150, width='100p', window=res)       
            
button1 = tk.Button (root, text='Calcular',command=Condicion, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(360, 180, window=button1)

button3 = tk.Button (root, text='Salir', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(430, 180, window=button3)
 
root.mainloop()