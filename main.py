import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")



class Profile:
    profiles = []
    
    def __init__(self, name):
        self.name = name
        
    def create_profile(cls, name):
        if any(profile.name == name for profile in cls.profiles):
            print(f"You already have a to-do list with {name}. Please try again")
            return
        
        new_profile = Profile(name)
        cls.profiles.append(new_profile)
        print(f"To-Do list {name} has been created!")
        
    def del_profile(cls, name):
        for profile in cls.profiles:
            if profile.name == name:
                cls.profiles.remove(profile)
                print(f"To-Do list: {name} has been deleted.")
        print(f"To-Do list {name} was not found, please try again.")

    def list_profiles(self):
        ...
        
    def list_todos(self):
        ...
    
class Todos:
    def __init__(self, title, priority, description):
        self.title = title
        self.priority = priority
        self.description = description
        ...
        
# class Unknowntodoerror(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
        
        
# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
        
#         self.title("To-Do List")
#         self.geometry("600x900")
        
#         optionmenu = customtkinter.CTkOptionMenu(self, values=["Profile 1", "Profile 2", "Profile 3", "Profile 4"])
#         optionmenu.pack(pady=10, padx=10)
        
    
#     def optionmenu_callback(self):
#         print("Optionmenu dropdown clicked:", self.choice)
        

if __name__ == "__main__":
    Profile("Fuckasaurus").list_todos()
    
    # app = App()
    # app.mainloop()