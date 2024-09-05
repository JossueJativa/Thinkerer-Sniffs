import customtkinter as ctk
import tkinter as tk
from pages import create_home_page, create_login_page, create_register_page, create_products_page, create_users_page, edit_products_page, edit_users_page
from data.controllerData import create_tables
from widgets import Colors

class mainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Facturador Sniffs")
        self.fullscreen = False
        self.pages = {}
        self.configure(bg=Colors.white)

        self.setup_window()
        self.create_widgets()
        self.show_frame("login")
        
    def setup_window(self):
        logo_path = "img/logo.png"
        self.iconphoto(False, tk.PhotoImage(file=logo_path))
        self.resizable(False, False)
    
    def create_widgets(self):
        self.pages["login"] = create_login_page(self, self.show_frame)
        self.pages["login"].grid(row=0, column=0, sticky="nsew")
        self.pages["register"] = create_register_page(self, self.show_frame)
        self.pages["register"].grid(row=0, column=0, sticky="nsew")
        self.pages["home"] = create_home_page(self, self.show_frame)
        self.pages["home"].grid(row=0, column=0, sticky="nsew")
        self.pages["products"] = create_products_page(self, self.show_frame)
        self.pages["products"].grid(row=0, column=0, sticky="nsew")
        self.pages["users"] = create_users_page(self, self.show_frame)
        self.pages["users"].grid(row=0, column=0, sticky="nsew")
        self.pages["editarProducto"] = edit_products_page(self, self.show_frame)
        self.pages["editarProducto"].grid(row=0, column=0, sticky="nsew")
        self.pages["editarUsuario"] = edit_users_page(self, self.show_frame)
        self.pages["editarUsuario"].grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        for page, frame in self.pages.items():
            if page == page_name:
                frame.grid()
            else:
                frame.grid_remove()

if __name__ == "__main__":
    create_tables()
    app = mainApp()
    app.mainloop()