#making argument optional
def formated_name(first_name,last_name,middle_name=''):
    if middle_name:
       full_name = first_name + " " + middle_name + " " + last_name
    else:
       full_name = first_name + " " + last_name
       return full_name.title()
teacher = formated_name('sheikh','suchana','suchi')
print(teacher)