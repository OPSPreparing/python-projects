from tkinter import *
import speedtest 

def speedcheck():
    sp =speedtest.Speedtest()
    sp.get_server()
    down = str(round(sp.download()/(10**6))) + "MBPS"
    up = str(round(sp.upload()/(10**6))) + "MBPS"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp =Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="blue")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 20, "bold"), bg ="blue", fg="white")
lab.place(x=80,y=20, height=30, width=380)

lab = Label(sp, text="Download Speed", font=("Times New Roman", 20, "bold"), bg ="blue", fg="white")
lab.place(x=80,y=70,height=30, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 20, "bold"), bg ="blue", fg="white")
lab_down.place(x=80,y=110,height=30, width=380)

lab = Label(sp, text="Upload Speed", font=("Times New Roman", 20, "bold"), bg ="blue", fg="white")
lab.place(x=80,y=160,height=30, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 20, "bold"), bg ="blue", fg="white")
lab_up.place(x=80,y=200,height=30, width=380)

button = Button(sp, text= "Check Speed", font=("Times New Roman", 20, "bold"),relief=RAISED, bg="Red", command=speedcheck)
button.place(x=80,y=260,height=50, width=380)
sp.mainloop()