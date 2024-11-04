import tkinter as tk
from tkinter import colorchooser
from tkinter import PhotoImage

root = tk.Tk()
root.title("Tabla de șah")

# Culorile implicite pentru tabla de șah
color1 = 'white'
color2 = 'black'

# Variabile pentru stările butoanelor de setare
setari_vizibile_color = False
setare_vizibilitate_history = False

# Panou pentru istoricul mutărilor
move_list = tk.Frame(root, borderwidth=2, relief="sunken")
listbox = tk.Listbox(move_list)
scrollbar = tk.Scrollbar(move_list, orient="vertical", command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

    
# Funcția care construiește tabla de șah
def tabla_de_sah():
    for i in range(1, 9):
        for j in range(1, 9):
            patrat = tk.Button(root, width=5, height=2, command=lambda i=i, j=j: adauga_mutare(i, j))
            if (i + j) % 2 == 0:
                patrat.config(bg=color1)
            else:
                patrat.config(bg=color2)
            patrat.grid(row=i+2, column=j)  # Plasăm tabla începând de la rândul 3

    for j in range(1, 9):
        tk.Label(root, width=5, height=2, text=chr(64 + j)).grid(row=2, column=j)
        tk.Label(root, width=5, height=2, text=chr(64 + j)).grid(row=11, column=j)
    for i in range(1, 9):
        tk.Label(root, width=5, height=2, text=str(i)).grid(row=i+2, column=0)
        tk.Label(root, width=5, height=2, text=str(i)).grid(row=i+2, column=9)
    

def adauga_mutare(i, j):
    coordonata = f"Mutare la: {chr(64 + j)}{i}"
    listbox.insert(tk.END, coordonata)  
 
def selecteaza_culoare1():
    global color1
    color1 = colorchooser.askcolor(title="Alege prima culoare")[1]
    tabla_de_sah()  # Reconstruim tabla cu noua culoare

# Funcția pentru a selecta a doua culoare
def selecteaza_culoare2():
    global color2
    color2 = colorchooser.askcolor(title="Alege a doua culoare")[1]
    tabla_de_sah()  # Reconstruim tabla cu noua culoare

def reset_colors():
    global color1,color2
    color1 = 'white'
    color2 = 'black'
    tabla_de_sah()

# Funcția care arată sau ascunde butoanele de alegere a culorilor
def toggle_setari():
    global setari_vizibile_color
    setari_vizibile_color = not setari_vizibile_color
    
    if setari_vizibile_color:
        buton_culoare1.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky="ew")
        buton_culoare2.grid(row=1, column=3, padx=5, pady=5, columnspan=3, sticky="ew")
        button_reset_colors.grid(row=1,column=6,padx=5,pady=5,columnspan=3,sticky="ew")
    else:
        buton_culoare1.grid_forget()
        buton_culoare2.grid_forget()
        button_reset_colors.grid_forget()

# Funcția care afișează sau ascunde panoul cu istoricul mutărilor
def history_of_moves():
    global setare_vizibilitate_history
    setare_vizibilitate_history = not setare_vizibilitate_history
    
    if setare_vizibilitate_history:
        move_list.grid(row=3, rowspan=9, column=10, padx=5, pady=5, sticky="nsew")
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    else:
        listbox.pack_forget()
        scrollbar.pack_forget()
        move_list.grid_forget()


# Butonul de setare care afișează/ascunde opțiunile de alegere a culorilor
buton_setare = tk.Button(root, text="Setare culori", command=toggle_setari)
buton_setare.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

buton_history = tk.Button(root, text="History of moves", command=history_of_moves)
buton_history.grid(row=0, column=2, columnspan=3, padx=5, pady=5, sticky="ew")

# Butoanele pentru selectarea culorilor (inițial ascunse)
buton_culoare1 = tk.Button(root, text="Alege prima culoare", command=selecteaza_culoare1)
buton_culoare2 = tk.Button(root, text="Alege a doua culoare", command=selecteaza_culoare2)
button_reset_colors = tk.Button(root,text="Reset color",command=reset_colors)

# Construim tabla de șah inițial
tabla_de_sah()

root.mainloop()
