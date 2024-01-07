

### **Tkinter Basics:**
```python
import tkinter as tk

# Create a main window
window = tk.Tk()
window.title("My GUI App")

# Label widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Button widget
def button_click():
    label.config(text="Button clicked!")

button = tk.Button(window, text="Click me", command=button_click)
button.pack()

# Entry widget
entry = tk.Entry(window)
entry.pack()

# Text widget
text_widget = tk.Text(window, height=3, width=30)
text_widget.insert(tk.END, "This is a Text widget.")
text_widget.pack()

# Checkbutton widget
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(window, text="Check me", variable=check_var)
checkbutton.pack()

# Radiobutton widget
radio_var = tk.StringVar()
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
radio_button1.pack()
radio_button2.pack()

# Pack or grid widgets as needed
# window.pack()  # if using pack()
# window.grid()  # if using grid()

# Run the Tkinter event loop
window.mainloop()
```

### **Event Handling:**
```python
def handle_event(event):
    print("Event Type:", event.type)

# Bind events to widgets
button.bind("<Button-1>", handle_event)
entry.bind("<Return>", lambda event: print("Enter key pressed"))

# Additional Events: "<Motion>", "<Enter>", "<Leave>", "<KeyPress>", "<KeyRelease>", etc.
```

### **Dialogs:**
```python
from tkinter import messagebox

# Message Box
result = messagebox.showinfo("Info", "This is an information message.")

# Ask Yes/No Question
response = messagebox.askyesno("Question", "Do you want to proceed?")
if response:
    print("User clicked Yes")
else:
    print("User clicked No")
```

### **File Dialog:**
```python
from tkinter import filedialog

# Open File Dialog
file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

# Save File Dialog
file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save file")
```
