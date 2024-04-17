from tkinter import *
import bookstore_backend as backend

# Commands
def getSelectedRow(event):
    try:
        index = listbx.curselection()[0]
        global selected
        selected = listbx.get(index)
        entryTitle.delete(0,END)
        entryAuthor.delete(0,END)
        entryYear.delete(0,END)
        entryISBN.delete(0,END)
        entryTitle.insert(END,selected[1])
        entryAuthor.insert(END,selected[2])
        entryYear.insert(END,selected[3])
        entryISBN.insert(END,selected[4])
    except IndexError:
        pass

def viewCommand():
    listbx.delete(0,END)
    for row in backend.view():
        listbx.insert(END,row)
    
def searchCommand():
    listbx.delete(0,END)
    for row in backend.search(tvarTitle.get(),tvarAuthor.get(),tvarYear.get(),tvarISBN.get()):
        listbx.insert(END,row)

def addCommand():
    backend.add(tvarTitle.get(),tvarAuthor.get(),tvarYear.get(),tvarISBN.get())
    listbx.delete(0,END)
    listbx.insert(END,(tvarTitle.get(),tvarAuthor.get(),tvarYear.get(),tvarISBN.get()))

def updateCommand():
    backend.update(selected[0],tvarTitle.get(),tvarAuthor.get(),tvarYear.get(),tvarISBN.get())

def deleteCommand():
    backend.delete(selected[0])

# Initialise tkinter interface & database
window = Tk()
window.wm_title("Bookstore Database")
backend.connect()

# Top of window; User entry boxes
labelTitle = Label(window,text="Title")
labelAuthor = Label(window,text="Author")
labelYear = Label(window,text="Year")
labelISBN = Label(window,text="ISBN")

labelTitle.grid(row=0,column=0)
labelAuthor.grid(row=0,column=2)
labelYear.grid(row=1,column=0)
labelISBN.grid(row=1,column=2)

tvarTitle,tvarAuthor,tvarYear,tvarISBN = StringVar(),StringVar(),StringVar(),StringVar()

entryTitle = Entry(window,textvariable=tvarTitle)
entryAuthor = Entry(window,textvariable=tvarAuthor)
entryYear = Entry(window,textvariable=tvarYear)
entryISBN = Entry(window,textvariable=tvarISBN)

entryTitle.grid(row=0,column=1)
entryAuthor.grid(row=0,column=3)
entryYear.grid(row=1,column=1)
entryISBN.grid(row=1,column=3)



# Bottom left of window; Data box & scrollbar
listbx = Listbox(window,height=6,width=35)
listbx.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

listbx.configure(yscrollcommand=scroll.set)
scroll.configure(command=listbx.yview)

listbx.bind("<<ListboxSelect>>",getSelectedRow)



# Action buttons
buttonView = Button(window,text="View all",width=12,command=viewCommand)
buttonSearch = Button(window,text="Search entries",width=12,command=searchCommand)
buttonAdd = Button(window,text="Add entry ",width=12,command=addCommand)
buttonUpdate = Button(window,text="Update entry",width=12,command=updateCommand)
buttonDelete = Button(window,text="Delete entry",width=12,command=deleteCommand)
buttonExit = Button(window,text="Exit",width=12,command=window.destroy)

buttonView.grid(row=2,column=3)
buttonSearch.grid(row=3,column=3)
buttonAdd.grid(row=4,column=3)
buttonUpdate.grid(row=5,column=3)
buttonDelete.grid(row=6,column=3)
buttonExit.grid(row=7,column=3)


# Run the interface
window.mainloop()