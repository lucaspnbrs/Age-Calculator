import datetime
import tkinter as tk
from PIL import Image, ImageTk
import os

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age

def getInput():
    name = nameEntry.get()
    monkey = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))

    answer = f"Heyy {monkey.name}!!! You are {monkey.age()} years old!!"

    textArea.delete(1.0, tk.END)  # Limpa o conteúdo anterior
    textArea.insert(tk.END, answer)

window = tk.Tk()
window.geometry("620x780")
window.title("Age Calculator App")

name = tk.Label(text="Name")
name.grid(column=0, row=1)

year = tk.Label(text="Year")
year.grid(column=0, row=2)

month = tk.Label(text="Month")
month.grid(column=0, row=3)

date = tk.Label(text="Day")
date.grid(column=0, row=4)

nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)

yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)

monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)

dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)

textArea = tk.Text(master=window, height=10, width=25)
textArea.grid(column=1, row=6)

button = tk.Button(window, text="Calculate Age", command=getInput, bg="pink")
button.grid(column=1, row=5)

script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, 'attack_1.png')

image = Image.open(image_path)
image.thumbnail((300, 300))
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

window.mainloop()

