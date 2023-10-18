import string
import random 
import tkinter as tk

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = int(entry.get())
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    password = ("".join(s[0:passlen]))
    result_label.config(text=password)

# Create the GUI
root = tk.Tk()
root.title("Password Generator")

# Create the input field
label = tk.Label(root, text="Enter the length of password:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create the button to generate the password
button = tk.Button(root, text="Generate Password", command=gen)
button.pack()

# Create the label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI
root.mainloop()