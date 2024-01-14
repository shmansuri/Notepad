import tkinter as Tk
from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import *

root=Tk()
root.geometry("1200x800")

root.title("My Notepad")

def myfunc():
    print("i'm saddam hussain mansuri")

def New():
    global File
    root.title("Untitled-Notepad")
    file=None
    text_msg.delete(1.0,END)
    
def NewWindow():
    pass
def open():
    global File
    file=askopenfilename(defaultextension=".txt", 
                     filetypes=[("all types","*.*"),
                                ("Text Document","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        text_msg.delete(1.0,END)
        f=open(file,"r")
        text_msg.insert(1.0,f.read())
        f.close()


    
def save():
    global file
    if file == None:
        file=asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                               filetypes=[("All Files","*.*"),
                                          ("Text Document" ,"*.txt")])
        if file == "":
            file=None

        else:
            #save as a new file
            f1=open(file,"w")
            f1.write(text_msg.get(1.0,END))
            f1.close()

            root.title(os.path.basename(file)+"-Notepad")
            print("file save")

    else:
        #save the file
        f1.open(file,"w")
        f1.write(text_msg.get(1.0,END))
        f1.close() 



def save_as():
    pass
def page_set_up():
    pass
def print_page():
    pass
def exit_page():
    pass


#for edit menu
def undo():
    text_msg.event_generate(("<<Undo>>"))

def cut():
    text_msg.event_generate(("<<Cut>>"))

def copy():
    text_msg.event_generate(("<<Copy>>"))

def paste():
    text_msg.event_generate(("<<Paste>>"))

def delete():
 text_msg.delete("1.0","end")



My_Menu=Menu(root)
#this part working on the File
sub_menu=Menu(My_Menu, tearoff=0)

sub_menu.add_command(label="New",command=New)
sub_menu.add_command(label="New window",command=NewWindow)
sub_menu.add_command(label="open",command=open)
sub_menu.add_command(label="Save",command=save)
sub_menu.add_command(label="Save as",command=save_as)
sub_menu.add_separator()
sub_menu.add_command(label="page set_up",command=page_set_up)
sub_menu.add_command(label="print",command=print_page)
sub_menu.add_separator()
sub_menu.add_command(label="Exit",command=exit_page)

root.config(menu=My_Menu)

My_Menu.add_cascade(label="File", menu=sub_menu)

#second Edit bar

edit_menu=Menu(My_Menu, tearoff=0)

edit_menu.add_command(label="Undo",command=undo)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)
edit_menu.add_command(label="Delete",command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Search with Bing...",command=myfunc)
edit_menu.add_command(label="find",command=myfunc)
edit_menu.add_command(label="Find Next",command=myfunc)
edit_menu.add_command(label="Find Previous",command=myfunc)
edit_menu.add_command(label="Replace",command=myfunc)
edit_menu.add_command(label="Go To...",command=myfunc)
edit_menu.add_separator()
edit_menu.add_command(label="Select All",command=myfunc)
edit_menu.add_command(label="Time/Date",command=myfunc)

root.config(menu=My_Menu)

My_Menu.add_cascade(label="Edit", menu=edit_menu)

#This part working on the Formate bar

Format_Menu=Menu(My_Menu, tearoff=0)
Format_Menu.add_command(label="Word Wrap", command=myfunc)
Format_Menu.add_command(label="Font...",command=myfunc)

My_Menu.add_cascade(label="Format",menu=Format_Menu )

#This part working on the View bar in My Notepad

View=Menu(My_Menu,tearoff=0)
View.add_command(label="Zoom",command=myfunc)
View.add_command(label="Status Bar..",command=myfunc)
My_Menu.add_cascade(label="View", menu=View)

#this part is working for the Help menu

help_menu=Menu(My_Menu, tearoff=0)
help_menu.add_command(label="View Help",command=myfunc)
help_menu.add_command(label="Send Feedback", command=myfunc)
help_menu.add_separator()
help_menu.add_command(label="About Notepad", command=myfunc)
My_Menu.add_cascade(label="Help",menu=help_menu)

#fot the scrollbar

scroll_bar=Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)

#for the text area

text_msg=Text(root, yscrollcommand=scroll_bar.set)
file=None
text_msg.pack(expand=True,fill=BOTH)
scroll_bar.config(command=text_msg.yview)

root.mainloop()
