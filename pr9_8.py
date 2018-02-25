class User():
    def __init__(self, first_name, last_name):
        self.first = first_name.title()
        self.last = last_name.title()
        self.login_attempts = 0
        
    def describe_user(self):
        print(self.first + " " + self.last)
        print(self.login_attempts)
    
    def greet_user(self):
        print("Hello " + self.first + " " + self.last + " !")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self):
        self.privileges = [
            'can add post',     
            'can delete post', 
            'can ban user',
        ]
        
    def show_privileges(self):
        for privilege in self.privileges:
            print("admin ".title() + privilege)
            

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
        self.privileges.show_privileges()
            
            
admin1 = Admin("albert", 'einstein')


