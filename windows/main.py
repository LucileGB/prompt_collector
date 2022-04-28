from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Prompt Manager")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 600
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


def welcome_screen():
    main_frame = ttk.Frame(root, padding="30 30 30 30")
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

    left_frame = ttk.Frame(main_frame)
    right_frame = ttk.Frame(main_frame)

    left_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    right_frame.grid(column=1, row=0, sticky=(N, W, E, S))

    ttk.Button(left_frame, text="Hellooo World").grid()
    ttk.Button(right_frame, text="Hello World").grid()

    for child in main_frame.winfo_children():
        for element in child.winfo_children():
            element.grid_configure(padx=12, pady=12)

    root.bind('<Escape>', lambda e: root.destroy())

welcome_screen()
root.mainloop()
