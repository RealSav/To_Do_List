import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")



class Profile:
    def __init__(self, name):
        self.name = name
        
    def create_profile(self):
        self.name
        ...
        
    def del_profile(self):
        ...

    def list_profiles(self):
        ...
        
    def list_todos(self):
        ...
    
class Todos:
    def __init__(self, name):
        self.name = name
        ...
        
class Unknowntodoerror(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("To-Do List")
        self.geometry("600x900")
        
        optionmenu = customtkinter.CTkOptionMenu(self, values=["Profile 1", "Profile 2", "Profile 3", "Profile 4"])
        optionmenu.pack(pady=10, padx=10)
        
    
    def optionmenu_callback(self):
        print("Optionmenu dropdown clicked:", self.choice)
        

if __name__ == "__main__":
    Profile("Fuckasaurus").list_todos()
    
    app = App()
    app.mainloop()