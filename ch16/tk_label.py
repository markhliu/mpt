import tkinter as tk

# Create the root window
root = tk.Tk()
# Specify the title and size of the root window
root.title("A Label Inside A Root Window")
root.geometry("800x200")
# Create a label inside the root window
label = tk.Label(text="this is a label", fg="Red", font=("Helvetica", 80))
label.pack()
# Run the game loop
root.mainloop()

