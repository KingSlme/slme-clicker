import customtkinter

class MainWindow:
    def __init__(self, root, autoclicker):
        self.root = root
        self.autoclicker = autoclicker
        self.average_cps_slider = None
        self.variance_slider = None
        self.average_cps_value_label = None
        self.variance_value_label = None
        self.entry = None
        self.create_main_window()

    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def average_cps_slider_callback(self, *_):
        value = round(self.average_cps_slider.get(), 1)
        self.average_cps_value_label.configure(text=value)
        self.autoclicker.set_cps(value)

    def variance_slider_callback(self, *_):
        value = round(self.variance_slider.get(), 1)
        self.variance_value_label.configure(text=value)
        self.autoclicker.set_variance(value)
    
    def on_entry_click(self, event):
        self.entry.delete(0, "end")

    def on_entry_key(self, event):
        if len(self.entry.get()) > 1:
            self.entry.delete(0, len(self.entry.get())-1)
        self.average_cps_value_label.focus_force()
        self.autoclicker.set_toggle_key(self.entry.get())

    def create_main_window(self):
        # Main Window
        self.root.title("SlmeClicker")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        MainWindow.center_window(self.root, 400, 200)
        self.root.resizable(width=False, height=False)
        # Frame
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=10, padx=10, fill="both", expand=True)
        # Progress Bars
        self.average_cps_slider = customtkinter.CTkSlider(master=frame, width=300, height=25, progress_color="#0288f5", from_=0, to=20, hover=False, command=self.average_cps_slider_callback)
        self.average_cps_slider.grid(row=1, column=0, padx=10, pady=0)
        self.variance_slider = customtkinter.CTkSlider(master=frame, width=300, height=25, progress_color="#0288f5", from_=0, to=5, hover=False, command=self.variance_slider_callback)
        self.variance_slider.grid(row=3, column=0, padx=10, pady=0)
        # Labels
        average_cps_label = customtkinter.CTkLabel(master=frame, text="Average CPS:", font=customtkinter.CTkFont("Inter", 20))
        average_cps_label.grid(row=0, column=0, padx=20, pady=(5, 0), sticky="w")
        self.average_cps_value_label = customtkinter.CTkLabel(master=frame, text=self.average_cps_slider.get(), font=customtkinter.CTkFont("Inter", 20))
        self.average_cps_value_label.grid(row=1, column=1, padx=(0, 5), pady=0, sticky="w")
        variance_label = customtkinter.CTkLabel(master=frame, text="Variance:", font=customtkinter.CTkFont("Inter", 20))
        variance_label.grid(row=2, column=0, padx=20, pady=0, sticky="w")
        self.variance_value_label = customtkinter.CTkLabel(master=frame, text=self.variance_slider.get(), font=customtkinter.CTkFont("Inter", 20))
        self.variance_value_label.grid(row=3, column=1, padx=(0, 5), pady=0, sticky="w")
        key_bind_label = customtkinter.CTkLabel(master=frame, text="Key:", font=customtkinter.CTkFont("Inter", 20))
        key_bind_label.grid(row=4, column=0, padx=0, pady=(0, 5))
        # Entry
        self.entry = customtkinter.CTkEntry(master=frame, width=30)
        self.entry.grid(row=5, column=0, padx=0, pady=(0, 5))
        self.entry.bind("<Button-1>", self.on_entry_click)
        self.entry.bind("<KeyRelease>", self.on_entry_key)