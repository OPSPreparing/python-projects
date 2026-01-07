import tkinter as tk
import random

root = tk.Tk()
root.geometry("400x400")
root.title("Love Calculator")

# Add a Label to display the result
result = tk.Label(root, text="Calculate love percentage")
result.pack()

def calculate_love():
    st ='0123456789'
    digit = 2
    temp = random.sample(st, digit)
    result.config(text=''.join(temp))

heading = tk.Label(root, text="How much she/he loves you?")
heading.pack()

person1 = tk.Label(root, text="Enter name?")
person1.pack()

name1 = tk.Entry(root)
name1.pack()

person2 = tk.Label(root, text="Enter partner name?")
person2.pack()

name2 = tk.Entry(root)
name2.pack()

# Add a button to trigger the function
button = tk.Button(root, text="Calculate Love", command=calculate_love)
button.pack()

result = tk.Label(root, text="Love Percentage between two people is:")
result.pack()
root.mainloop()