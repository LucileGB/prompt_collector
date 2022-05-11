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

class Interface:
    def menu_bar():
        root.option_add('*tearOff', FALSE)
        menubar = Menu(root)
        root['menu'] = menubar
        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='About')

    def welcome_screen():
        Interface.menu_bar()
        main_frame = ttk.Frame(root, padding="30 30 30 30")
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        left_frame = ttk.Frame(main_frame)
        right_frame = ttk.Frame(main_frame)

        left_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        right_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        ttk.Button(left_frame, text="My collections").grid()
        ttk.Button(left_frame, text="My prompts").grid(row=1)

        ttk.Button(right_frame, text="Look for exchanges").grid()

        for child in main_frame.winfo_children():
            for element in child.winfo_children():
                element.grid_configure(padx=12, pady=12)

        root.bind('<Escape>', lambda e: root.destroy())

Interface.welcome_screen()
root.mainloop()
