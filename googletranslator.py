from tkinter import *
from tkinter import ttk #(combo box)
from googletranslator import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = Sor_txt.get(1.0, END)
    dest_lang = dest_combo.get()
    src_lang = src_combo.get()


root = Tk()
root.title("Translator")
root.geometry("250x500")
root.config(bg="red")

lab_txt =Label(root, text="Translator", font=("Times New Roman", 15, "bold"))
lab_txt.place(x=100,y=40,height=50,width=400)

frame = Frame(root).pack(side=LEFT)

lab_txt = Label(root, text="Source text", font=("Times New Roman", 25, "bold"))
lab_txt.place(x=200,y=300,height=40,width=400)

Sor_txt = Text(frame, font=("Times New Roman", 15, "bold"), wrap=WORD)
Sor_txt.place(x=200,y=400,height=150,width=400)

root.mainloop()