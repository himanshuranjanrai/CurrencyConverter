import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title('Currency converter')
root.geometry('500x500')


#creating tabs
my_notebook=ttk.Notebook(root)
my_notebook.pack(pady=5)

#creating 2 frames
currency_frame=Frame(my_notebook,width=480,height=480)
conversion_frame=Frame(my_notebook,width=480,height=480)

currency_frame.pack(fill="both",expand=1)
conversion_frame.pack(fill="both",expand=1)

#adding our tabs
my_notebook.add(currency_frame,text="Currencies")
my_notebook.add(conversion_frame,text="Convert")

#Disable 2nd tab
my_notebook.tab(1,state='disabled')

#############################################
###############CURRENCY####################

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("WARNING!","YOU DIDN'T FILL OUT ALL THE FIELDS")
    else:
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        my_notebook.tab(1,state='normal')
        #change tab field
        amount_label.config(text=f'Amount of {home_entry.get()} To Convert To {conversion_entry.get()}')
        converted_label.config(text=f'Equals This Many {conversion_entry.get()}')
        convert_button.config(text=f'Convert From {home_entry.get()}')
        
def unlock():
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    my_notebook.tab(1,state='disabled')


#currency Frame
home= LabelFrame(currency_frame,text="Your Home Currency")
home.pack(pady=20)

#home currency entry box
home_entry=Entry(home,font=("Helvetica",24))
home_entry.pack(pady=10,padx=10)

#conversion currency frame
conversion=LabelFrame(currency_frame,text="Conversion Currency")
conversion.pack(pady=20)

#convert to label
conversion_label=Label(conversion,text="Currency to convert")
conversion_label.pack(pady=10)

#convert to entry
conversion_entry=Entry(conversion,font=("Helvetica",24))
conversion_entry.pack(pady=10,padx=10)

#rate Label
rate_label=Label(conversion,text="Current conversion rate")
rate_label.pack(pady=10)

#rate entry
rate_entry=Entry(conversion,font=("Helvetica",24))
rate_entry.pack(pady=10,padx=10)

#button Frame
button_frame=Frame(currency_frame)
button_frame.pack(pady=20)

#create buttons in button frame
lock_button=Button(button_frame,text="Lock",command=lock)
lock_button.grid(row=0,column=0,padx=10)

unlock_button=Button(button_frame,text="Unlock",command=unlock)
unlock_button.grid(row=0,column=1,padx=10)

###############################################
#############CONVERSION#####################

def convert():
    #clear converted entry box
    converted_entry.delete(0,END)

    #convert
    conversion=float(rate_entry.get())*float(amount_entry.get())
    conversion=round(conversion,2)
    conversion='{:,}'.format(conversion)
    
    #update Entry box
    converted_entry.insert(0,conversion)
    
def clear():
    amount_entry.delete(0,END)
    converted_entry.delete(0,END)
    
#amount frame
amount_label=LabelFrame(conversion_frame,text="Amount To Convert")
amount_label.pack(pady=20)

#entry box for amount
amount_entry=Entry(amount_label,font=("Helvetica",24))
amount_entry.pack(pady=10,padx=10)

#convert button
convert_button=Button(amount_label,text="Convert",command=convert)
convert_button.pack(pady=20)

#equals frame
converted_label=LabelFrame(conversion_frame,text="Converted Currency")
converted_label.pack(pady=20)

#converted entry
converted_entry=Entry(converted_label,font=("Helvetica",24),bd=0,bg="systembuttonface")
converted_entry.pack(pady=10,padx=10)

#clear button
clear_button=Button(conversion_frame,text="Clear",command=clear)
clear_button.pack(pady=20)
                  
#fake label for exact spacing in frames
spacer=Label(conversion_frame,text="",width=68)
spacer.pack()

root.mainloop()
