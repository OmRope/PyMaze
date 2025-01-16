import tkinter as tk

def create_canvas():
    # Create canvas logic here
    print("Canvas created")

def create_form():
    root = tk.Tk()
    root.attributes('-fullscreen', True)

    # Create a frame for the form using grid layout
    form_frame = tk.Frame(root, bg="lightblue", padx=20, pady=20)
    form_frame.grid(row=0, column=0, sticky="nsew")  # Fill the entire window

    # Create a label for the heading
    heading_label = tk.Label(form_frame, text="Maze Game", font=("Arial", 20))
    heading_label.grid(row=0, columnspan=2, pady=10, sticky="w")

    # Create input fields with labels
    label1 = tk.Label(form_frame, text="Rows:")
    label1.grid(row=1, column=0, sticky="e")
    entry1 = tk.Entry(form_frame)
    entry1.grid(row=1, column=1, sticky="w")

    label2 = tk.Label(form_frame, text="Cols:")
    label2.grid(row=2, column=0, sticky="e")
    entry2 = tk.Entry(form_frame)
    entry2.grid(row=2, column=1, sticky="w")

    # ... (Add more input fields as needed)

    # Create a run button
    run_button = tk.Button(form_frame, text="Run", command=create_canvas)
    run_button.grid(row=3, columnspan=2, pady=10, sticky="e")

    root.mainloop()

create_form()