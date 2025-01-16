import tkinter as tk

def create_canvas():
    global canvas_created  # Declare canvas_created as a global variable
    if not canvas_created:
        canvas = tk.Canvas(root, width=300, height=300, bg="yellow")
        canvas.pack()
        canvas_created = True  # Set the flag to True

canvas_created = False  # Initialize the flag

root = tk.Tk()
root.title("Canvas Creation")

button = tk.Button(root, text="Click Me", command=create_canvas)
button.pack()

root.mainloop()