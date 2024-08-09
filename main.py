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
        raise Unknowntodoerror("No To-Dos found")
    
class Todos:
    def __init__(self, name):
        self.name = name
        ...
        
class Unknowntodoerror(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

if __name__ == "__main__":
    Profile("Fuckasaurus").list_todos()