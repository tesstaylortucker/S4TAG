import random
import string
from tkinter import *
import functions

# Initialize trait and aspiration lists
adultTraits = functions.initialize_adult_trait_list()
teenTraits = functions.initialize_teen_trait_list()
childTraits = functions.initialize_child_trait_list()
toddlerTraits = functions.initialize_toddler_trait_list()
childAspirations = functions.make_list_from_file("ChildAspirations.txt")
aspirations = functions.make_list_from_file("Aspirations.txt")

# Create a tkinter window
root = Tk()
root.title("Sims 4 Trait & Aspiration Generator")
root.geometry('500x300')

# Create window label
l = Label(root, text = "Generate Random Aspirations and Traits")
l.config(font = ("Arial", 14))

# Create text box for button output
T = Text(root, height = 1, width = 40)
T.tag_configure("center", justify='center')
T.tag_add("center", 1.0, "end")

# Function to center and assign text into the text box T
def center_text(text):
    T.tag_configure("center", justify='center')
    T.insert("1.0", text)
    T.tag_add("center", "1.0", "end")

# Event for the Adult Trait button
def btn1():
    T.delete('1.0', END)
    center_text(functions.generate_random_item_from_list(adultTraits))

# Event for the Teen Trait button
def btn2():
    T.delete('1.0', END)
    center_text(functions.generate_random_item_from_list(teenTraits))

# Event for the Child Trait button
def btn3():
    T.delete('1.0', END)
    center_text(functions.generate_random_item_from_list(childTraits))

# Event for the Toddler Trait button
def btn4():
    T.delete('1.0', END)
    center_text(functions.generate_random_item_from_list(toddlerTraits))

# Event for the Child Aspiration button
def btn5():
    T.delete('1.0', END)
    center_text(functions.generate_random_item_from_list(childAspirations))

# Event for the Aspiration button
def btn6():
    T.delete('1.0', END)
    center_text(functions.generate_random_item_from_list(aspirations))

# Create adult trait button
adult_trait_btn = Button(root, text = "Adult Trait", bd = '5', width = '20',
                        command = btn1)
# Create teen trait button
teen_trait_btn = Button(root, text = "Teen Trait", bd = '5', width = '20',
                        command = btn2)
# Create child trait button
child_trait_btn = Button(root, text = "Child Trait", bd = '5', width = '20',
                         command = btn3)
# Create toddler trait button
toddler_trait_btn = Button(root, text = "Toddler Trait", bd = '5', width = '20',
                        command = btn4)
# Create child aspiration button
child_aspr_btn = Button(root, text = "Child Aspiration", bd = '5', width = '20',
                        command = btn5)
# Create adult aspiration button
adult_aspr_btn = Button(root, text = "Aspiration", bd = '5', width = '20',
                        command = btn6)

# Set the position of the label & buttons
l.pack()
adult_trait_btn.pack()
teen_trait_btn.pack()
child_trait_btn.pack()
toddler_trait_btn.pack()
child_aspr_btn.pack()
adult_aspr_btn.pack()
T.pack()

mainloop()





