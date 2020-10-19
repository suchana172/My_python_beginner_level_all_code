birthday_months = {
    'Suchana': 'December',
    'Santona': 'December',
    'Biplob': 'September',
    'Bornil': 'March'
}
for name in birthday_months.keys():
    print(name.title())
for months in birthday_months.values():
    print(months.title())
for months in set(birthday_months.values()):
    print(months.title())