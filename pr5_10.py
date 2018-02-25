current_users = ['admin', 'nutcheer', 'guest', 'Crystal', 'Tiffany']
new_users = ['admin', 'nutcheer', 'Albert' ,'Mclean', 'Han']
for user in new_users:
    if user in current_users or user.lower() in current_users or user.upper() in current_users:
        print(user+"已被占用")
    else:
        print(user+"可用!")
