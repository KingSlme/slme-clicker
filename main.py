import customtkinter
from main_window import MainWindow
from autoclicker import Autoclicker

if __name__ == "__main__":
    root = customtkinter.CTk()
    ac = Autoclicker()
    root.after(0, ac.autoclick, root)
    root.after(0, ac.set_varied_delay_loop, root)
    main_window = MainWindow(root, ac)
    root.mainloop()
