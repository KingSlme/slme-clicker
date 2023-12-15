import customtkinter
from main_window import MainWindow
import autoclicker

def my_mainloop(root):
    print("Hello World!")
    root.after(1000, my_mainloop, root)  # run again after 1000ms (1s)

if __name__ == "__main__":
    root = customtkinter.CTk()
    
    ac = autoclicker.Autoclicker()
    root.after(1, ac.autoclick, root)

    main_window = MainWindow(root, ac)
    root.mainloop()