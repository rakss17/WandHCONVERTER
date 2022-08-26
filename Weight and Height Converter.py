import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from PIL import ImageTk,Image
from datetime import date
from datetime import datetime
import time
import tkinter as tk
import tkinter.scrolledtext as st
import threading


def back():
    global root
    root.destroy()
    mainwindow()

def back2():
    global hroot
    hroot.destroy()
    mainwindow()

def about():
    win = tk.Tk()
    win.title("About")
    win.geometry("400x400")
    win.config(bg="light cyan3")

# SCROLL BAR
    tk.Label(win, text="What is weight and height converter?", font=("Arial", 15), background='cornsilk3', foreground="black").grid(
        column=0, row=1)
    text_area = st.ScrolledText(win, width=36, height=15, font=("Times New Roman", 15), bg="light cyan3",
                                foreground='black')
    text_area.grid(column=0, pady=10, padx=10)

    text_area.insert(tk.INSERT,
                     """
What is Weight Converter?

This weight converter tool is the best 
tool for converting between different 
weight units. We not only include a 
real-time weight conversion tool, but 
also a weight conversion chart (weight 
conversion table) that allows you to 
easily convert between units, e.g., lbs 
to kg, kg to lbs, oz to stones and so on. 
We will also explain in this article what is 
weight, discuss if weight is a force or not 
and even touch briefly on bodyweight, health 
issues and how to lose weight (and how to 
gain weight) for those who are interested.

What is Height Converter?

This length converter is a tool that enables 
quick conversion between length units in both 
imperial and metric. Height is measure of 
vertical distance, either vertical extent (how 
"tall" something or someone is) or vertical 
position (how "high" a point is). For example, 
"The height of that building is 50 m" or "The 
height of an airplane in-flight is about 
10,000 m". When the term is used to describe 
vertical position (of, e.g., an airplane) from 
sea level, height is more often called altitude. 
Furthermore, if the point is attached to the 
Earth (e.g., a mountain peak), then altitude 
(height above sea level) is called elevation.
                 """)

    text_area.configure(state='disabled')
    win.mainloop()

def formula():
    forwin = Tk()
    forwin.title("Height Formula")
    forwin.geometry("400x300")
    forwin.config(bg="light cyan3")

# DIALOG HANDLING
    def save_file():
        file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text file","*.txt")])
        filetext = str(text2.get(1.0,END))
        file.write(filetext)
        file.close()
# DIALOG BOX
        messagebox.showinfo('Info', "Saved Successfully")
    text3 = ("Height Conversion Formula\n\n"
             "Kilometer (km) to Meter (m)\n"
             "km * 1,000 m\n\n"
             "Kilometer (km) to Centimeter (cm)\n"
             "km * 100,000 cm")
    savebtn = Button(forwin, text="Save Formula",command=save_file)
    savebtn.pack()
    text2 = Text(forwin)
    text2.insert(tk.INSERT, text3)
    text2.configure(state="disabled")
    text2.pack()

    forwin.mainloop()

# Height Function

def heightconverter():
    global window
    window.destroy()
    OPTIONS = ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Foot (ft)", "Inch (in)"]
    global hroot
    hroot = Tk()
    hroot.title("Height")
    hroot.geometry("500x500")
    hroot.config(bg="light cyan3")

# MENU
    menubar = Menu(hroot)
    heightmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu",menu =heightmenu)
    heightmenu.add_command(label="Formula", command=formula)
    heightmenu.add_command(label="About",command=about)
    heightmenu.add_separator()
    heightmenu.add_command(label="Back",command=back2)

    hroot.config(menu=menubar)

 # CANVAS
    canvas2 = Canvas(hroot, width=500, height=500, bg="light cyan3")
    canvas2.pack()

    canvass = Canvas(hroot, width=300, height=80, bg="cornsilk3")
    canvass.create_text(150, 40, fill="black", font="Arial 20 bold", text="Height Converter")
    canvass.place(x=90, y=40)

    def reset():
        inputentry.delete(0, END)
        outputentry.delete(0, END)
        inputopt.set("Select a Unit")
        outputopt.set("Select a Unit")
        convertbtn.configure(state='active')

    def popup(e):
        try:
            my_menu.tk_popup(e.x_root, e.y_root)

        finally:
            my_menu.grab_release()

# POP UP MENU
    my_menu = Menu(hroot, tearoff=0)
    my_menu.add_command(label="Convert Again", command=reset)
    my_menu.add_separator()
    my_menu.add_command(label="Exit", command=exit)
# BIND EVENTS
    canvas2.bind("<Button-3>", popup)

# MULTI THREADING
    def thread():
        threading.Thread(target=convert).start()

    def convert():
        my_label = Label(hroot, text='Converting...', fg='black', bg="light cyan3", font=("Arial Bold", 10))
        my_label.place(x=200, y=425)

# ANIMATION
        progress = Progressbar(hroot, orient=HORIZONTAL, length=500, mode='determinate')
        progress.place(x=0, y=450)
        import time
        r = 0
        for i in range(100):
            progress['value'] = r
            hroot.update_idletasks()
            time.sleep(0.03)
            r = r + 1

# EXCEPTION HANDLING
        try:
            inp = float(inputentry.get())
            inp_unit = inputopt.get()
            out_unit = outputopt.get()

            if inp_unit == "Kilometer (km)" and out_unit == "Meter (m)":
                meter = inp * 1000.0
                outputentry.insert(0, meter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Kilometer (km)" and out_unit == "Centimeter (cm)":
                centimeter = inp * 100,000
                outputentry.insert(0, centimeter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Kilometer (km)" and out_unit == "Foot (ft)":
                foot = inp * 3,280.84
                outputentry.insert(0, foot)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Kilometer (km)" and out_unit == "Inch (in)":
                inch = inp * 39,370.0787
                outputentry.insert(0, inch)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Meter (m)" and out_unit == "Kilometer (km)":
                kilometer = inp * 0.001
                outputentry.insert(0, kilometer)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Meter (m)" and out_unit == "Centimeter (cm)":
                centimeter = inp * 100
                outputentry.insert(0, centimeter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Meter (m)" and out_unit == "Foot (ft)":
                foot = inp * 3.28084
                outputentry.insert(0, foot)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Meter (m)" and out_unit == "Inch (in)":
                inch = inp * 39.370
                outputentry.insert(0, inch)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Centimeter (cm)" and out_unit == "Kilometer (km)":
                kilometer = inp * 0.00001
                outputentry.insert(0, kilometer)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Centimeter (cm)" and out_unit == "Meter (m)":
                meter = inp * 0.01
                outputentry.insert(0, meter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Centimeter (cm)" and out_unit == "Foot (ft)":
                foot = inp * 0.03280
                outputentry.insert(0, foot)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Centimeter (cm)" and out_unit == "Inch (in)":
                inch = inp * 0.39370
                outputentry.insert(0, inch)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Foot (ft)" and out_unit == "Kilometer (km)":
                kilometer = inp * 0.0003048
                outputentry.insert(0, kilometer)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Foot (ft)" and out_unit == "Meter (m)":
                meter = inp * 0.3048
                outputentry.insert(0, meter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Foot (ft)" and out_unit == "Centimeter (cm)":
                centimeter = inp * 30.48
                outputentry.insert(0, centimeter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Foot (ft)" and out_unit == "Inch (in)":
                inch = inp * 12
                outputentry.insert(0, inch)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Inch (in)" and out_unit == "Kilometer (km)":
                kilometer = inp * 0.0000254
                outputentry.insert(0, kilometer)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Inch (in)" and out_unit == "Meter (m)":
                meter = inp * 0.0254
                outputentry.insert(0, meter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Inch (in)" and out_unit == "Centimeter (cm)":
                centimeter = inp * 2.54
                outputentry.insert(0, centimeter)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Inch (in)" and out_unit == "Foot (ft)":
                inch = inp * 0.08333
                outputentry.insert(0, inch)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            else:
                my_label.destroy()
                progress.destroy()
                messagebox.showwarning('Warning', "Please select a units")
        except Exception:
            my_label.destroy()
            progress.destroy()
            messagebox.showerror('Error', "Invalid Input")
        inpstring = str(inputentry.get())
        outstring = str(outputentry.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

# FILE HANDLING
        file = open("history.txt", "a", encoding='utf-8')
        file.write("\n\n")
        file.write(" Height Converted History\n")
        file.write("--------------------------\n")
        file.write("Input: ")
        file.write(inpstring)
        file.write("  ")
        file.write(inp_unit)
        file.write("\n")
        file.write("Output: ")
        file.write(outstring)
        file.write("  ")
        file.write(out_unit)
        file.write("\n")
        file.write("Date/Time: ")
        file.write(str(today))
        file.write("   ")
        file.write(str(current_time))
        file.close()



    inputopt = tkinter.StringVar(hroot)
    inputopt.set("Select a Unit")

    outputopt = tkinter.StringVar(hroot)
    outputopt.set("Select a Unit")

    # Widgets
    inputlabel = Label(hroot, text="Input", font=("Arial Bold", 15), background='cornsilk3', foreground="black")
    inputlabel.place(x=180, y=160)

    inputentry = Entry(hroot, justify="center", font="bold")
    inputentry.place(x=100, y=210)

    inputmenu = OptionMenu(hroot, inputopt, *OPTIONS)
    inputmenu.place(x=300, y=205)
    inputmenu.config(font="Arial 10")

    outputlabel = Label(hroot, text="Output", font=("Arial Bold", 15), background='cornsilk3', foreground="black")
    outputlabel.place(x=170, y=260)

    outputentry = Entry(hroot, justify="center", font="bold")
    outputentry.place(x=100, y=310)

    outputmenu = OptionMenu(hroot, outputopt, *OPTIONS)
    outputmenu.place(x=300, y=305)
    outputmenu.config(font="Arial 10")

    convertbtn = Button(hroot, text="Convert", command=thread, padx=80, pady=2)
    convertbtn.place(x=150, y=370)

    hroot.mainloop()

def formula2():
    forwin = Tk()
    forwin.title("Weight Formula")
    forwin.geometry("400x300")
    forwin.config(bg="light cyan3")

# DIALOG HANDLING
    def save_file():
        file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text file","*.txt")])
        filetext = str(text2.get(1.0,END))
        file.write(filetext)
        file.close()
        messagebox.showinfo('Info', "Saved Successfully")
    text3 = ("Weight Conversion Formula\n\n"
             "Kilogram (kg) to Gram (g)\n"
             "kg * 1,000 g\n\n"
             "Kilogram (kg) to Pound (lb)\n"
             "kg * 2.2046 lb")
    savebtn = Button(forwin, text="Save Formula",command=save_file)
    savebtn.pack()
    text2 = Text(forwin)
    text2.insert(tk.INSERT, text3)
    text2.configure(state="disabled")
    text2.pack()

    forwin.mainloop()

# Weight Function
def weightconverter():
    global window
    window.destroy()
    OPTIONS = ["Kilogram (kg)", "Gram (g)", "Pound (lb)", "Ounce (oz)"]
    global root
    root = Tk()
    root.title("Weight")
    root.geometry("500x500")
    root.config(bg="light cyan3")

# MENU
    menubar = Menu(root)
    weightmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu",menu =weightmenu)
    weightmenu.add_command(label="Formula", command=formula2)
    weightmenu.add_command(label="About",command=about)
    weightmenu.add_separator()
    weightmenu.add_command(label="Back",command=back)

    root.config(menu=menubar)

# CANVAS
    canvas2 = Canvas(root, width=500, height=500, bg="light cyan3")
    canvas2.pack()

    canvass = Canvas(root, width=300, height=80, bg="cornsilk3")
    canvass.create_text(150, 40, fill="black", font="Arial 20 bold", text="Weight Converter")
    canvass.place(x=90, y=40)

    def reset():
        inputentry.delete(0, END)
        outputentry.delete(0, END)
        inputopt.set("Select a Unit")
        outputopt.set("Select a Unit")
        convertbtn.configure(state='active')

    def popup(e):
        try:
            my_menu.tk_popup(e.x_root, e.y_root)

        finally:
            my_menu.grab_release()

# POP UP MENU
    my_menu = Menu(root, tearoff=0)
    my_menu.add_command(label="Convert Again", command=reset)
    my_menu.add_separator()
    my_menu.add_command(label="Exit", command=exit)
# BIND EVENTS
    canvas2.bind("<Button-3>", popup)

# MULTI THREADING
    def thread():
        threading.Thread(target=convert).start()

    def convert():
        my_label = Label(root, text='Converting...', fg='black', bg="light cyan3", font=("Arial Bold",10))
        my_label.place(x=200, y=425)

# ANIMATION
        progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
        progress.place(x=0, y=450)
        import time
        r = 0
        for i in range(100):
            progress['value'] = r
            root.update_idletasks()
            time.sleep(0.03)
            r = r + 1

# EXCEPTION HANDLING
        try:
            inp = float(inputentry.get())
            inp_unit = inputopt.get()
            out_unit = outputopt.get()

            if inp_unit == "Kilogram (kg)" and out_unit == "Gram (g)":
                gram = inp * 1000.0
                outputentry.insert(0, gram)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Kilogram (kg)" and out_unit == "Pound (lb)":
                pound = inp * 2.20462
                outputentry.insert(0, pound)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Kilogram (kg)" and out_unit == "Ounce (oz)":
                ounce = inp * 35.2739619
                outputentry.insert(0, ounce)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Gram (g)" and out_unit == "Kilogram (kg)":
                kilogram = inp * 0.001
                outputentry.insert(0, kilogram)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Gram (g)" and out_unit == "Pound (lb)":
                pound = inp * 0.002204
                outputentry.insert(0, pound)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Gram (g)" and out_unit == "Ounce (oz)":
                ounce = inp * 0.035273
                outputentry.insert(0, ounce)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Pound (lb)" and out_unit == "Kilogram (kg)":
                kilogram = inp * 0.453592
                outputentry.insert(0, kilogram)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Pound (lb)" and out_unit == "Gram (g)":
                gram = inp * 453.59237
                outputentry.insert(0, gram)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Pound (lb)" and out_unit == "Ounce (oz)":
                ounce = inp * 16.000
                outputentry.insert(0, ounce)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Ounce (oz)" and out_unit == "Kilogram (kg)":
                kilogram = inp * 0.02835
                outputentry.insert(0, kilogram)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Ounce (oz)" and out_unit == "Gram (g)":
                gram = inp * 453.592374
                outputentry.insert(0, gram)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            elif inp_unit == "Ounce (oz)" and out_unit == "Pound (lb)":
                pound = inp * 0.0625
                outputentry.insert(0, pound)
                my_label.destroy()
                progress.destroy()
                messagebox.showinfo('Info', 'Converted')
                convertbtn.configure(state='disabled')
            else:
                my_label.destroy()
                progress.destroy()
                messagebox.showwarning('Warning', "Please select a units")
        except Exception:
            my_label.destroy()
            progress.destroy()
            messagebox.showerror('Error', "Invalid Input")
        inpstring = str(inputentry.get())
        outstring = str(outputentry.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

# FILE HANDLING
        file = open("history.txt", "a", encoding='utf-8')
        file.write("\n\n")
        file.write(" Weight Converted History\n")
        file.write("--------------------------\n")
        file.write("Input: ")
        file.write(inpstring)
        file.write("  ")
        file.write(inp_unit)
        file.write("\n")
        file.write("Output: ")
        file.write(outstring)
        file.write("  ")
        file.write(out_unit)
        file.write("\n")
        file.write("Date/Time: ")
        file.write(str(today))
        file.write("   ")
        file.write(str(current_time))
        file.close()

    inputopt = tkinter.StringVar(root)
    inputopt.set("Select a Unit")

    outputopt = tkinter.StringVar(root)
    outputopt.set("Select a Unit")

    # Widgets
    inputlabel = Label(root, text="Input", font=("Arial Bold", 15), background='cornsilk3', foreground="black")
    inputlabel.place(x=180, y=160)

    inputentry = Entry(root, justify="center", font="bold")
    inputentry.place(x=100, y=210)

    inputmenu = OptionMenu(root, inputopt, *OPTIONS)
    inputmenu.place(x=300, y=205)
    inputmenu.config(font="Arial 10")

    outputlabel = Label(root, text="Output", font=("Arial Bold", 15), background='cornsilk3', foreground="black")
    outputlabel.place(x=170, y=260)

    outputentry = Entry(root, justify="center", font="bold")
    outputentry.place(x=100, y=310)

    outputmenu = OptionMenu(root, outputopt, *OPTIONS)
    outputmenu.place(x=300, y=305)
    outputmenu.config(font="Arial 10")

    convertbtn = Button(root, text="Convert", command=thread, padx=80, pady=2)
    convertbtn.place(x=150, y=370)

    root.mainloop()


def mainwindow():
    global window
    window = Tk()
    window.title("Weight and Height Converter")
    window.geometry("400x400")
    window.config(bg="light cyan3")

# CANVAS

    canvass = Canvas(window, width=350, height=100, bg="cornsilk3")
    canvass.create_text(170, 50, fill="black", font="Arial 20 bold", text="Weight and Height\n       Converter")
    canvass.place(x=20, y=60)

    btn = Button(window, text="Weight Converter", font="Arial 10", width=13, height=3, command=weightconverter)
    btn.place(x=80, y=200)

    btn2 = Button(window, text="Height Converter", font="Arial 10", width=13, height=3,command=heightconverter)
    btn2.place(x=220, y=200)

# DISPLAYING IMAGE

    image = Image.open("C:\Programming\Python\Weight and Height Converter\window1.jpg")
    resize_image = image.resize((100, 100))
    img = ImageTk.PhotoImage(resize_image)
    img1 = Label(window, image=img)
    img1.image = img
    img1.place(x=10, y=300)

    image = Image.open("C:\Programming\Python\Weight and Height Converter\window2.jpg")
    resize_image = image.resize((100, 100))
    img = ImageTk.PhotoImage(resize_image)
    img1 = Label(window, image=img)
    img1.image = img
    img1.place(x=145, y=300)

    image = Image.open("C:\Programming\Python\Weight and Height Converter\window3.jpg")
    resize_image = image.resize((100, 100))
    img = ImageTk.PhotoImage(resize_image)
    img1 = Label(window, image=img)
    img1.image = img
    img1.place(x=280, y=300)

    window.mainloop()
mainwindow()