prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("Hello, " + name + "!")

def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')

def get_fornatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()
    

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
        
    formatted_name = get_fornatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

