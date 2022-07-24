from tkinter import *

root=Tk()
root.title("Valentin, MercadoLibre Inventory")
root.geometry("500x300")

#update the Listbox
def update(data):
    #clear the listbox
    my_list.delete(0, END)

    #Add products to my_list
    for item in data:
        my_list.insert(END, item)

#Update entry box with listbox clicked
def fillout(e): #event
    #Delete whatever is in the entry box
    my_entry.delete(0, END)

    #Add clicked list item to entry box
    my_entry.insert(0, my_list.get(ACTIVE))

#create function to check entry vs listbox
def check(e):
    # grab what was typed
    typed= my_entry.get()
    if typed == "":
        data = products
    else:
        data=[]
        for item in products:
            if typed.lower() in item.lower():
                data.append(item)
    #update our listbos with selected items
    update(data)

#create a label
my_label= Label(root, text="Start typing...",
                font=("Helvetica",14), fg="grey")
my_label.pack(pady=20)

#create an entry box
my_entry = Entry(root, font=("Helvetica",12))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

#Create a list
products=[]
with open("database.txt") as database:
    lines=database.readlines()
    for line in lines:
        products.append(line)

update(products)

#Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>",fillout)

#create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()
