from tkinter import *
import xlrd

root=Tk()
root.title("Valentin, MercadoLibre Inventory")
root.geometry("1000x500")

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
my_entry = Entry(root, font=("Helvetica",15), width=50)
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=100, height=200)
my_list.pack(pady=40)

#Create a list
products=[]
"""
with open("database.txt") as database:
    lines=database.readlines()
    for line in lines:
        products.append(line)
"""

path="Publicaciones-2022_07_23-22_30.xls"
excel_workbook = xlrd.open_workbook(path)
excel_worksheet = excel_workbook.sheet_by_index(3)
number_cols=excel_worksheet.ncols
number_rows=excel_worksheet.nrows
print("cols :"+ str(number_cols) + ", rows: " + str(number_rows))

for row in range(1,number_rows):
    for col in range(0,1):
        #print(excel_worksheet.cell_value(row,col))
        products.append(excel_worksheet.cell_value(row,col))


update(products)

#Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>",fillout)

#create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()
