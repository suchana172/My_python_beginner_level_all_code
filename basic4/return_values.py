# returning a value in a function
def formated_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
teacher = formated_name('suchana','suchi')
print(teacher)
def get_formated_username(email_address):
    user_name = email_address.strip()
    return user_name
user = get_formated_username('suchana@example.com    ')
print(user)